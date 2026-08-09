# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st

from utils.evaluation import evaluate_model
from components.metrics import render_metrics
from components.confusion_matrix import render_confusion_matrix
from components.classification_report import render_classification_report
from components.feature_importance import render_feature_importance
from components.download import render_download


# ==========================================================
# Model Inspector
# ==========================================================

def render_model_inspector(
    prediction_results,
    selected_models,
    y_test,
    label_encoder,
    feature_names
):

    st.markdown("---")
    st.header("🔍 Inspect Model")

    if y_test is None:
        st.info("Evaluation metrics are not available for Manual Input.")
        return

    inspect_model = st.selectbox(
        "Choose a model",
        selected_models
    )

    result = prediction_results[inspect_model]

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
        feature_names,
        inspect_model
    )

    render_download(
        result["prediction_df"]
    )