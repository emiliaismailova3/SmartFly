✈️ SmartFly - Flight Price Predictor
A web application for predicting airline ticket prices using Machine Learning (Random Forest algorithm).

🎯 Features
Price prediction based on route, date, airline, and other parameters
User-friendly web interface
Real-time predictions
🛠️ Technologies
Python - Core programming language
Flask - Web framework
Random Forest - Machine Learning algorithm
Scikit-learn - ML library
Pandas - Data processing
HTML/CSS - Frontend
📊 About the Model
Algorithm: Random Forest Regressor
Model Size: 472 MB
Features: route, departure date, airline, service class
🚀 Installation and Setup
1. Clone the repository
git clone https://github.com/ismailovaemilia615-design/SmartFly.git
cd SmartFly
2. Install dependencies
pip install flask pandas scikit-learn numpy
3. Download trained models
Models are stored separately due to large file size (472 MB total).

📥 Download all models from Google Drive

Create a models/ folder and place the downloaded files there:

SmartFly/
└── models/              ← create this folder
    ├── random_forest_model.pkl
    ├── label_encoders.pkl
    └── features.pkl
4. Run the application
python app.py
Open your browser: http://localhost:5000

📁 Project Structure

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
📈 Model Performance
Algorithm: Random Forest Regressor
Training Data: Large dataset of flight records


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
