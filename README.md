✈️ SmartFly – Flight Price Predictor
A web application that estimates airline ticket prices using Machine Learning (Random Forest algorithm).

🎯 Features

Price prediction based on route, date, airline, and additional parameters

Simple and intuitive web interface

Instant, real-time results

🛠️ Technologies

Python – Core programming language

Flask – Web framework

Random Forest – Machine Learning algorithm

Scikit-learn – ML toolkit

Pandas – Data handling

HTML/CSS – Frontend structure and styling

📊 About the Model

Algorithm: Random Forest Regressor

Model Size: 472 MB

Features used: route, departure date, airline, service class

🚀 Installation and Setup

1. Clone the repository

git clone https://github.com/ismailovaemilia615-design/SmartFly.git
cd SmartFly


2. Install dependencies

pip install flask pandas scikit-learn numpy


3. Download the pretrained models
The trained models are stored separately due to their large size (472 MB total).

📥 Download all model files from Google Drive

Create a models/ directory and place the downloaded files inside:

SmartFly/
└── models/
    ├── random_forest_model.pkl
    ├── label_encoders.pkl
    └── features.pkl


4. Start the application

python app.py


Open in browser: http://localhost:5000

📁 Project Structure
SmartFly/
├── app.py                      # Main Flask application
├── models/                     # ML models (download separately)
│   ├── random_forest_model.pkl # Trained Random Forest model
│   ├── label_encoders.pkl      # Encoders for categorical data
│   └── features.pkl            # Feature definitions
├── templates/                  # HTML templates
│   ├── index.html              # Main page
│   └── predict.html            # Prediction result page
└── static/
    └── style.css               # Styling

📈 Model Performance

Algorithm: Random Forest Regressor

Training Data: Large dataset of flight information

Model Size: 472 MB of learned parameters

💡 How It Works

User enters flight details (route, date, airline, etc.)

The model processes the input via the Random Forest algorithm

The system outputs the predicted price

Results are displayed on a clean, user-friendly page

🖼️ Screenshots
![Изображение WhatsApp 2025-11-25 в 15 38 09_b46a5bfe](https://github.com/user-attachments/assets/3868dfcd-9363-45e2-8d69-c8fb561fc17d)
![Изображение WhatsApp 2025-11-25 в 15 38 09_528cbcbe](https://github.com/user-attachments/assets/dc9b0480-e3ca-4043-a699-f5b56cd8795f)
![Изображение WhatsApp 2025-11-25 в 15 38 08_d32866e1](https://github.com/user-attachments/assets/013a9cd6-f85f-49fd-9243-5573bcbd57ec)
![Изображение WhatsApp 2025-11-25 в 15 38 08_324636a5](https://github.com/user-attachments/assets/5f40c80c-cabc-4195-a18f-a2f19d9dd5ba)

👤 Author
Emiliya Ismailova
📝 Note
Models are not included in the repository due to GitHub file size limitations. Please download them from the Google Drive link above.
🔒 License
This project was created for educational purposes.
Model Size: 472 MB of trained parameters
💡 How It Works
User inputs flight details (route, date, airline, etc.)
Model processes the input using trained Random Forest algorithm
System returns predicted price range
Results displayed in user-friendly interface
🖼️ Screenshots
