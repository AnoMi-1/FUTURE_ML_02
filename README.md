# Customer Churn Prediction System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](futurechurnpredict.streamlit.app)

# Project Overview
This project was developed for Task 2 of the Machine Learning Internship at Future Interns. The system identifies customers likely to stop using a service, allowing businesses to take proactive retention measures. 

# Tech Stack
The versions below are optimized for 2026 deployment environments, specifically addressing library deprecations and Streamlit Cloud compatibility.

1. **UI:** [Streamlit](https://streamlit.io/) (v1.52.2)
2. **Model:** [FastAI](docs.fast.ai) Tabular Learner (v2.8.6)
3. **Interpretation:** [SHAP](shap.readthedocs.io) (v0.49.1)
4. **Data Handling:** [Pandas](pandas.pydata.org) (v2.3.3) & [NumPy](numpy.org) (v2.0.2)
5. **Environment Fixes:** Added `ipython` for `fastprogress` support on Linux servers.
6. **Training Environment:** Kaggle

# Repository Structure
1. `streamlit/app.py`: The main Streamlit web application.
2. `streamlit/churn_model.pkl`: The exported FastAI model (uses relative paths for cloud hosting).
3. `requirements.txt`: List of dependencies for cloud deployment.
4. `notebooks/`: Contains the original Kaggle training notebook (`.ipynb`).
5. `data/`: Sample dataset used for training and testing.

# Model & Performance
The model was trained on the Telco Customer Churn dataset.
1. **Type:** Deep Learning (Tabular Learner).
2. **Interpretability:** Uses SHAP to explain feature importance and prediction drivers.
3. **Key Features:** Contract type, Tenure, Monthly Charges, and Internet Service.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AnoMi-1/FUTURE_ML_02.git
   cd FUTURE_ML_02

2. **Install dependencies:**
      pip install -r requirements.txt

3. **Run the application:**
      streamlit run streamlit/app.py








