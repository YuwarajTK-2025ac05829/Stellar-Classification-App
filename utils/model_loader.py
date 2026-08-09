# ==========================================================
# Import Libraries
# ==========================================================

import joblib
import streamlit as st


# ==========================================================
# Load Trained Models
# ==========================================================

@st.cache_resource
def load_models():
    """
    Load all trained machine learning models along with
    the scaler and label encoder.
    """

    models = {
        "Logistic Regression": joblib.load("models/logistic_regression.pkl"),
        "Decision Tree": joblib.load("models/decision_tree.pkl"),
        "K-Nearest Neighbors": joblib.load("models/knn.pkl"),
        "Gaussian Naive Bayes": joblib.load("models/gaussian_nb.pkl"),
        "Random Forest": joblib.load("models/random_forest.pkl")
    }

    scaler = joblib.load("models/scaler.pkl")

    label_encoder = joblib.load("models/label_encoder.pkl")

    return models, scaler, label_encoder