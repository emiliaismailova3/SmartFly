from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle
from datetime import datetime, timedelta
import os
import time

app = Flask(__name__)

CATEGORICAL_FEATURES = ['airline', 'source_city', 'departure_time',
                        'stops', 'destination_city', 'class']

def get_css_version():
    css_path = 'static/style.css'
    if os.path.exists(css_path):
        return int(os.path.getmtime(css_path))
    return int(time.time())

try:
    with open('models/random_forest_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    with open('models/label_encoders.pkl', 'rb') as f:
        encodings = pickle.load(f)
    
    with open('models/features.pkl', 'rb') as f:
        feature_columns = pickle.load(f)
    
    print("✅ Model loaded successfully!")
    
except FileNotFoundError:
    print("❌ Model files not found.")
    model = None
    encodings = {}
    feature_columns = []

model_comparison = {
    'RandomForest': {'R2': 0.9834, 'RMSE': 34.60, 'MAE': 13.15},
    'GradientBoosting': {'R2': 0.9570, 'RMSE': 55.77, 'MAE': 33.43},
    'XGBoost': {'R2': 0.9808, 'RMSE': 37.29, 'MAE': 20.38},
    'LightGBM': {'R2': 0.9759, 'RMSE': 41.74, 'MAE': 24.13},
    'AdaBoost': {'R2': 0.9349, 'RMSE': 68.62, 'MAE': 43.02},
    'CatBoost': {'R2': 0.9802, 'RMSE': 37.84, 'MAE': 20.85},
    'LinearRegression': {'R2': 0.9057, 'RMSE': 82.59, 'MAE': 55.18}
}

@app.context_processor
def inject_css_version():
    return {'css_version': get_css_version()}

@app.route('/')
def index():
    return render_template('index.html', models=model_comparison)

@app.route('/predict')
def predict_page():
    today = datetime.now().date()
    max_date = today + timedelta(days=365)
    return render_template('predict.html', 
                          min_date=today.isoformat(),
                          max_date=max_date.isoformat())

# Label each predicted price as Cheap / Average / Expensive
# relative to the other prices in the same 30-day window.
def classify_prices(prices, base_price=None):
    if not prices:
        return []

    prices_array = np.array(prices)
    mean_price = np.mean(prices_array)
    std_dev = np.std(prices_array)
    
    # Cheap < mean - 0.5*std, Expensive > mean + 0.5*std
    threshold_cheap = mean_price - 0.5 * std_dev
    threshold_expensive = mean_price + 0.5 * std_dev
    
    categories = []
    for price in prices:
        if price < threshold_cheap:
            categories.append("Cheap")
        elif price > threshold_expensive:
            categories.append("Expensive")
        else:
            categories.append("Average")
    return categories

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({'success': False, 'error': 'Model not loaded'})
        
        data = request.get_json(silent=True) or {}
        missing = [f for f in CATEGORICAL_FEATURES if not data.get(f)]
        if missing:
            return jsonify({'success': False, 'error': f"Missing fields: {', '.join(missing)}"}), 400

        # 1. Predict a price for each of the next 30 days
        raw_predictions = []
        current_date = datetime.now()
        
        for days_left in range(1, 31):
            input_data = {}
            for feature in feature_columns:
                if feature in CATEGORICAL_FEATURES:
                    value = data.get(feature)
                    encoder = encodings.get(feature)
                    if encoder is not None and value in encoder.classes_:
                        input_data[feature] = encoder.transform([value])[0]
                    else:
                        input_data[feature] = 0
                elif feature == 'days_left':
                    input_data[feature] = days_left
                else:
                    input_data[feature] = data.get(feature, 0)
            
            # Make sure all model features are present and in the right order
            features_df = pd.DataFrame([input_data]).reindex(columns=feature_columns, fill_value=0)
            
            price_usd = model.predict(features_df)[0]
            price_inr = price_usd * 84
            flight_date = current_date + timedelta(days=days_left)
            
            raw_predictions.append({
                'days_until_flight': days_left,
                'flight_date': flight_date.strftime('%d.%m.%Y'),
                'price_usd': max(20, round(price_usd, 2)),
                'price_inr': max(1680, round(price_inr))
            })
            
        # 2. Classify prices within the window
        price_list_usd = [p['price_usd'] for p in raw_predictions]
        price_categories = classify_prices(price_list_usd)
        
        # 3. Attach the category to each prediction
        final_predictions = []
        for i, pred in enumerate(raw_predictions):
            pred['price_category'] = price_categories[i]
            final_predictions.append(pred)
            
        return jsonify({
            'success': True,
            'predictions': final_predictions,
            'route': f"{data['source_city']} → {data['destination_city']}",
            'flight_class': data['class'],
            'airline': data['airline'],
            'departure_time': data['departure_time']
        })
        
    except Exception as e:
        app.logger.exception("Prediction error")
        return jsonify({'success': False, 'error': 'Prediction failed'}), 500

if __name__ == '__main__':
    print("🚀 Starting Flight Price Predictor...")
    # Debug mode only when FLASK_DEBUG=1 is set
    app.run(debug=os.environ.get('FLASK_DEBUG') == '1', port=5000)