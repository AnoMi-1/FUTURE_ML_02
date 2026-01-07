# Customer Churn Prediction System

# [Live App Link][![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://futurechurnpredict.streamlit.app/)


# Project Overview
This project was developed for Task 2 of the Machine Learning Internship at Future Interns. The system identifies customers likely to stop using a service, allowing businesses to take proactive retention measures. 

# Tech Stack
1. UI: Streamlit (v1.52.2)
2. Model: FastAI Tabular Learner (v2.8.4)
3. Interpretation: SHAP (v0.49.1)
4. Data Handling: Pandas (v2.2.6) & NumPy (v2.0.2)
5. Training Environment: Kaggle

# Repository Structure
1. `app.py`: The main Streamlit web application.
2. `churn_model.pkl`: The exported FastAI model.
3. `requirements.txt`: List of dependencies for cloud deployment.
4.  `notebooks/`: Contains the original Kaggle training notebook (`.ipynb`).
5. `data/`: Sample dataset used for training and testing.

#  Model & Performance
The model was trained on the Telco Customer Churn dataset.
1. Type: Deep Learning (Tabular Learner).
2. Interpretability: Uses SHAP to explain feature importance and prediction drivers.
3. Key Features: Contract type, Tenure, Monthly Charges, and Internet Service.

## ⚙️ How to Run Locally
1. Clone the repository:
   ```bash
   git clone github.com
   cd YOUR_REPO_NAME
