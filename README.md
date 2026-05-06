Sales Forecasting System using SARIMA, Prophet, XGBoost & LSTM

📌 Project Overview

This project is an end-to-end time series forecasting system developed to predict the next 8 weeks of sales for each state using historical sales data.

The solution compares multiple forecasting techniques and automatically selects the best-performing model based on evaluation metrics.

The project includes:

Data preprocessing
Feature engineering
Time series forecasting
Model comparison
REST API deployment using FastAPI

🚀 Features
✅ Forecast next 8 weeks of sales
✅ State-wise forecasting
✅ Automatic best model selection
✅ Handles missing dates
✅ Feature engineering for time-series ML
✅ REST API deployment using FastAPI
✅ Multiple forecasting models implemented
✅ Evaluation using RMSE, MAE, and MAPE

📊 Models Implemented

The following forecasting models were trained and compared:

SARIMA (Seasonal ARIMA)
Facebook Prophet
XGBoost Regressor
LSTM Neural Network

The best model is automatically selected for each state using RMSE.

🛠️ Tech Stack
Programming Language
Python
Libraries & Frameworks
Pandas
NumPy
Scikit-learn
XGBoost
Prophet
Statsmodels
TensorFlow / Keras
Matplotlib
Seaborn
FastAPI
Uvicorn
Joblib

📂 Dataset Information

Dataset Columns:

State
Date
Total
Category

Dataset Size:

8084 rows

⚙️ Feature Engineering

The following features were created:

Lag Features
lag_1
lag_7
lag_30

Rolling Statistics
Rolling Mean (7 days)
Rolling Standard Deviation (7 days)
Date Features
Day of Week
Month
Week Number
Holiday Feature
US Holiday Flag

📈 Evaluation Metrics

The models were evaluated using:

MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)
MAPE (Mean Absolute Percentage Error)

🔄 Time-Series Validation

A proper time-series split strategy was used to avoid data leakage.

Training Data → Historical observations
Validation Data → Last 56 days (8 weeks)

📡 FastAPI Deployment

The forecasting system is deployed using FastAPI.

Run API
uvicorn app:app --reload

🌐 API Endpoints
Home Endpoint
/

Returns API status.

Get Available States
/states

Returns all available states.

Forecast Endpoint
/predict/{state}

Example:

/predict/California

Response:

{
  "state": "California",
  "best_model": "XGBoost",
  "rmse": 1234.56
}

📊 Project Workflow
Load Dataset
Data Cleaning & Preprocessing
Feature Engineering
Train-Test Split
Train Forecasting Models
Evaluate Models
Select Best Model
Save Forecast Results
Deploy Predictions via API

📁 Project Structure
├── app.py
├── forecasting_notebook.ipynb
├── forecast_results.pkl
├── Forecasting Case- Study(1).xlsx
├── requirements.txt
└── README.md

▶️ Installation & Setup

Clone Repository

git clone <your-github-repo-link>

Create Virtual Environment

python -m venv venv

Activate Environment

Windows

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

▶️ Run Notebook

Open Jupyter Notebook:

jupyter notebook

Run all notebook cells sequentially.

▶️ Run API
uvicorn app:app --reload

📷 Sample Output

Example Output:

Processing State: California
Best Model for California: XGBoost
