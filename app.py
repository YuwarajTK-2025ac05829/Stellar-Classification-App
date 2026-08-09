from utils.model_loader import load_models
from utils.evaluation import evaluate_model

from components.model_selection import model_selection
from components.dashboard import render_dashboard
from components.prediction_mode import render_prediction_mode
from components.dataset_preview import render_dataset_preview
from components.prediction import render_prediction
from components.metrics import render_metrics
from components.confusion_matrix import render_confusion_matrix
from components.classification_report import render_classification_report
from components.feature_importance import render_feature_importance
from components.download import render_download
from components.model_comparison import render_model_comparison
from components.model_inspector import render_model_inspector

import streamlit as st


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Stellar Classification",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 Stellar Classification using Machine Learning")

st.markdown("---")

st.write(
    """
This application predicts whether a celestial object is a

- 🌌 GALAXY
- ⭐ STAR
- ✨ QSO

using supervised Machine Learning models.
"""
)

# ==========================================================
# Load Models
# ==========================================================

models, scaler, label_encoder = load_models()

# ==========================================================
# Model Selection
# ==========================================================

selected_models = model_selection(models)

# ==========================================================
# Clear cached predictions when selected models change
# ==========================================================

if (
    "last_selected_models" not in st.session_state
    or st.session_state["last_selected_models"] != selected_models
):

    st.session_state["last_selected_models"] = selected_models.copy()

    st.session_state.pop("prediction_results", None)

# ==========================================================
# Dashboard
# ==========================================================

render_dashboard(selected_models)

# ==========================================================
# Prediction Mode
# ==========================================================

df, prediction_mode = render_prediction_mode()

# ==========================================================
# Continue only if dataset exists
# ==========================================================

if df is None:
    st.stop()

# ==========================================================
# Dataset Preview
# ==========================================================

X_test, y_test = render_dataset_preview(df)

# ==========================================================
# Prediction
# ==========================================================

prediction_results = render_prediction(
    selected_models,
    models,
    scaler,
    label_encoder,
    X_test
)

if prediction_results is None:
    st.stop()

# ==========================================================
# MANUAL INPUT MODE
# ==========================================================

if prediction_mode == "Manual Input":

    st.markdown("---")
    st.header("🎯 Prediction Results")

    if len(selected_models) == 1:

        model_name = selected_models[0]

        result = prediction_results[model_name]

        st.dataframe(
            result["prediction_df"],
            width="stretch"
        )

        render_download(
            result["prediction_df"]
        )

    else:

        inspect_model = st.selectbox(
            "Choose a model",
            selected_models,
            key="manual_prediction_model"
        )

        result = prediction_results[inspect_model]

        st.dataframe(
            result["prediction_df"],
            width="stretch"
        )

        render_download(
            result["prediction_df"]
        )

    st.stop()

# ==========================================================
# DATASET EVALUATION MODE
# ==========================================================

if len(selected_models) == 1:

    model_name = selected_models[0]

    if model_name not in prediction_results:

        st.info("Click **Run Prediction** to generate predictions.")
        st.stop()

    result = prediction_results[model_name]

    metrics = evaluate_model(
        result["model"],
        result["X"],
        y_test,
        result["predictions"]
    )

    render_metrics(metrics)

    render_confusion_matrix(
        metrics,
        label_encoder
    )

    render_classification_report(
        metrics
    )

    render_feature_importance(
        result["model"],
        X_test.columns,
        model_name
    )

    render_download(
        result["prediction_df"]
    )

else:

    missing_models = [
        model
        for model in selected_models
        if model not in prediction_results
    ]

    if missing_models:

        st.info("Click **Run Prediction** to generate predictions.")
        st.stop()

    render_model_comparison(
        prediction_results,
        selected_models,
        y_test
    )

    render_model_inspector(
        prediction_results,
        selected_models,
        y_test,
        label_encoder,
        X_test.columns
    )