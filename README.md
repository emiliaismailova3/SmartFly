# ✈ SmartFly - Flight Price Predictor

A web application for predicting airline ticket prices using Machine Learning (Random Forest algorithm).

## 🎯 Features
- Price prediction based on route, date, airline, and other parameters
- User-friendly web interface
- Real-time predictions

## 🛠 Technologies
- *Python* - Core programming language
- *Flask* - Web framework
- *Random Forest* - Machine Learning algorithm
- *Scikit-learn* - ML library
- *Pandas* - Data processing
- *HTML/CSS* - Frontend

## 📊 About the Model
- *Algorithm*: Random Forest Regressor
- *Model Size*: 472 MB
- *Features*: route, departure date, airline, service class

## 🚀 Installation and Setup

### 1. Clone the repository
bash
git clone https://github.com/nazrinsultanova1/SmartFly.git
cd SmartFly


### 2. Install dependencies
bash
pip install flask pandas scikit-learn numpy


### 3. Download trained models
Models are stored separately due to large file size (472 MB total).

📥 **[Download all models from Google Drive](https://drive.google.com/drive/folders/1GDkFQlbJY7krBDZPhQy_hdoPj25-NaqC?usp=drive_link)**

Create a models/ folder and place the downloaded files there:

SmartFly/
└── models/              ← create this folder
    ├── random_forest_model.pkl
    ├── label_encoders.pkl
    └── features.pkl


### 4. Run the application
bash
python app.py


Open your browser: http://localhost:5000

## 📁 Project Structure

SmartFly/
├── app.py                      # Main Flask application
├── models/                     # ML models (download separately)
│   ├── random_forest_model.pkl # Trained Random Forest model
│   ├── label_encoders.pkl      # Label encoders for categorical features
│   └── features.pkl            # Feature list
├── templates/                  # HTML templates
│   ├── index.html             # Main page
│   └── predict.html           # Results page
└── static/                     # Static files
    └── style.css              # Styling


## 📈 Model Performance
- *Algorithm*: Random Forest Regressor
- *Training Data*: Large dataset of flight records
- *Model Size*: 472 MB of trained parameters

## 💡 How It Works
1. User inputs flight details (route, date, airline, etc.)
2. Model processes the input using trained Random Forest algorithm
3. System returns predicted price range
4. Results displayed in user-friendly interface

## 🖼 Screenshots
![Изображение WhatsApp 2025-11-25 в 15 38 09_c7d8e494](https://github.com/user-attachments/assets/44fdddac-dd03-4f0e-a0c1-1b75d81bfae5)
![Изображение WhatsApp 2025-11-25 в 15 38 09_616d2d21](https://github.com/user-attachments/assets/c0f134a1-53ee-487e-b631-cc20a9523c8b)
![Изображение WhatsApp 2025-11-25 в 15 38 08_04175ff5](https://github.com/user-attachments/assets/4590cfae-9800-4bf9-957f-d0c885614b13)
![Изображение WhatsApp 2025-11-25 в 15 38 08_12aaa6c1](https://github.com/user-attachments/assets/10416ad1-8b53-40eb-99f8-a28d27261964)






## 👤 Author
*Emilyia Ismailova*

[LinkedIn](http://www.linkedin.com/in/emiliya-ismailova-b16202370) | [GitHub](https://github.com/ismailovaemilia615-desing)
## 📝 Note
Models are not included in the repository due to GitHub file size limitations. Please download them from the Google Drive link above.

## 🔒 License
This project was created for educational purposes.
```


