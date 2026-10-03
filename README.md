# ✈ SmartFly — Flight Price Predictor

A Flask web app that predicts airline ticket prices for Indian domestic flights with a Random Forest regression model, and shows how the price changes over the next 30 days so the user can pick the cheapest day to fly.

Capstone project of the Coders Azerbaijan Data Science Bootcamp (2025).

![SmartFly screenshot 1](https://github.com/user-attachments/assets/44fdddac-dd03-4f0e-a0c1-1b75d81bfae5)

## Features

- Price prediction from airline, route, departure time, number of stops and travel class
- 30-day price forecast, with every day labelled **Cheap / Average / Expensive**
- Cheapest and most expensive day highlighted
- Model comparison table on the home page

## Model

Seven regression models were trained and compared; Random Forest gave the best results on the test set:

| Model | R² | RMSE | MAE |
|---|---|---|---|
| **Random Forest** | **0.9834** | **34.60** | **13.15** |
| XGBoost | 0.9808 | 37.29 | 20.38 |
| CatBoost | 0.9802 | 37.84 | 20.85 |
| LightGBM | 0.9759 | 41.74 | 24.13 |
| Gradient Boosting | 0.9570 | 55.77 | 33.43 |
| AdaBoost | 0.9349 | 68.62 | 43.02 |
| Linear Regression | 0.9057 | 82.59 | 55.18 |

**Features:** airline, source city, destination city, departure time, stops, class, days left before departure. Categorical features are label-encoded.

## Tech Stack

Python · scikit-learn · pandas · NumPy · Flask · HTML/CSS/JavaScript

## Run Locally

```bash
git clone https://github.com/emiliaismailova3/SmartFly.git
cd SmartFly
pip install -r requirements.txt
```

The trained model files (~472 MB) are too large for GitHub. [Download them from Google Drive](https://drive.google.com/drive/folders/1GDkFQlbJY7krBDZPhQy_hdoPj25-NaqC?usp=drive_link) and put them in a `models/` folder:

```
models/
├── random_forest_model.pkl
├── label_encoders.pkl
└── features.pkl
```

Then start the app and open http://localhost:5000:

```bash
python app.py
```

## Project Structure

```
SmartFly/
├── app.py              # Flask app: loads the model, serves pages and /api/predict
├── templates/
│   ├── index.html      # Home page with model comparison
│   └── predict.html    # Prediction form and 30-day results
├── static/
│   └── style.css
├── models/             # Model files (download separately, not in Git)
├── requirements.txt
└── README.md
```

## Screenshots

![SmartFly screenshot 2](https://github.com/user-attachments/assets/c0f134a1-53ee-487e-b631-cc20a9523c8b)
![SmartFly screenshot 3](https://github.com/user-attachments/assets/4590cfae-9800-4bf9-957f-d0c885614b13)
![SmartFly screenshot 4](https://github.com/user-attachments/assets/10416ad1-8b53-40eb-99f8-a28d27261964)

## Author

**Emiliya Ismailova**
[LinkedIn](https://linkedin.com/in/emiliya-ismailova) · [GitHub](https://github.com/emiliaismailova3)

This project was created for educational purposes.
