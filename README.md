# 🚗 CarValue AI

> An end-to-end Machine Learning application for estimating the resale price of used cars.

CarValue AI is a used-car price prediction project built using **Python, Pandas, Scikit-learn and Streamlit**.

The application takes vehicle specifications such as manufacturer, model, variant, mileage, manufacturing year, fuel type, transmission and number of owners, and predicts an estimated resale price using a trained **Random Forest Regression** model.

## 🌐 Live Demo

🚀 **Try CarValue AI:**  
https://carvalue-ai.streamlit.app/

---

## 📌 Project Overview

Buying or selling a used car can be difficult because vehicle prices depend on many factors.

CarValue AI uses historical used-car data and machine learning to estimate the expected market price of a vehicle based on its specifications.

The project covers the complete machine learning workflow:

**Dataset → Data Cleaning → Feature Engineering → Encoding → Model Training → Evaluation → Model Serialization → Streamlit Deployment**

---

## ✨ Features

- 🚗 Used-car price prediction
- 🤖 Random Forest Regression model
- 📊 Machine learning based price estimation
- 🏷️ Manufacturer, model and variant selection
- ⛽ Fuel type selection
- ⚙️ Transmission selection
- 🎨 Body type and color selection
- 📍 City-based vehicle information
- 📏 Mileage input
- 📅 Manufacturing and registration year
- 👥 Number of previous owners
- 🧠 Variant frequency encoding
- 🌐 Interactive Streamlit web application
- ☁️ Deployed using Streamlit Community Cloud

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning |
| Random Forest | Regression model |
| Joblib | Model serialization |
| Streamlit | Web application |
| Git & GitHub | Version control |
| Git LFS | Large model files |

---

## 📂 Project Structure

```text
CarValue-AI/
│
├── Data/
│   └── car_data.csv
│
├── Models/
│   ├── car_price_model.pkl
│   ├── encoder.pkl
│   └── variant_freq.pkl
│
├── Notebooks/
│   └── CarValue_Model.ipynb
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── .gitattributes  
Author

🧹 Data Preprocessing

The dataset was prepared before training the machine learning model.

Main preprocessing steps included:

Loading the used-car dataset
Checking missing values
Checking duplicate records
Removing unnecessary features
Separating target and input features
Encoding categorical variables
Applying frequency encoding to the variant feature
Splitting the data into training and testing sets
🧠 Feature Engineering
Categorical Features

The following categorical features were handled using one-hot encoding:

city
make
model
fuel_type
color
body_type
transmission
Variant Frequency Encoding

The variant column contained 1,293 unique values.

Instead of creating hundreds of one-hot encoded columns, frequency encoding was used.

The frequency values were calculated using the training data only to avoid data leakage.

🤖 Machine Learning Model

The project uses:

Random Forest Regression

The model was trained with:

n_estimators = 300
random_state = 42
n_jobs = -1

The dataset was split into:

Dataset	Records
Training	6,476
Testing	1,619
Total	8,095
📈 Model Performance

The trained model was evaluated on the held-out test dataset.

Metric	Result
MAE	₹44,527
RMSE	₹88,271
R² Score	0.9582
R² Score

The model achieved an R² score of 0.9582, meaning it explains a large proportion of the variation in the test-set prices.

The reported metrics are from the project's held-out test dataset.

💻 Streamlit Application

The trained model and preprocessing artifacts are loaded into the Streamlit application.

The application provides an interactive interface where users can enter vehicle details and receive an estimated price.

The prediction workflow is:

User Input
    ↓
Feature Preparation
    ↓
Variant Frequency Encoding
    ↓
Categorical Encoding
    ↓
Feature Combination
    ↓
Random Forest Model
    ↓
Estimated Car Price
🚀 Run Locally
1. Clone the repository
git clone https://github.com/Amaryadav1000/CarValue-AI.git
2. Navigate into the project
cd CarValue-AI
3. Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run the Streamlit application
streamlit run app.py

The application will open in your browser.

☁️ Deployment

The application is deployed using Streamlit Community Cloud.

Deployment configuration
Repository: Amaryadav1000/CarValue-AI
Branch: main
Entry Point: app.py

🔗 Live Application:
https://carvalue-ai.streamlit.app/

📓 Model Training

The complete model development process is available in:

Notebooks/CarValue_Model.ipynb

The notebook contains the data preparation, feature engineering, model training, evaluation and model artifact generation workflow.

📦 Model Artifacts

The trained model artifacts are stored in the Models directory:

Models/
├── car_price_model.pkl
├── encoder.pkl
└── variant_freq.pkl

Git LFS is used to manage the trained model files.

🎯 Future Improvements

Possible future improvements include:

📊 Adding more advanced model comparison
🔍 Improving feature engineering
📈 Adding prediction confidence information
📉 Adding interactive data visualizations
🚘 Adding more vehicle-related features
🎨 Further improving the Streamlit UI
⚡ Optimizing prediction performance
🔄 Adding automatic model retraining
📚 Learning Outcomes

Through this project, I worked with:

Data preprocessing
Exploratory data analysis
Feature engineering
Categorical encoding
Frequency encoding
Regression
Random Forest
Model evaluation
Model serialization using Joblib
Streamlit application development
Git and GitHub
Git LFS
Cloud deployment
👨‍💻 Author

Amar Yadav

BCA — Artificial Intelligence & Machine Learning

⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

Built with Python, Machine Learning & Streamlit. 🚗🤖