from utils.model_loader import load_models
from utils.evaluation import evaluate_model

from components.sidebar import render_sidebar
from components.dashboard import render_dashboard
from components.prediction_mode import render_prediction_mode
from components.dataset_preview import render_dataset_preview
from components.prediction import render_prediction
from components.metrics import render_metrics
from components.confusion_matrix import render_confusion_matrix
from components.classification_report import render_classification_report
from components.feature_importance import render_feature_importance
from components.download import render_download

import streamlit as st

st.set_page_config(
    page_title="Stellar Classification",
    page_icon="🌌",
    layout="wide"
)

models, scaler, label_encoder = load_models()

selected_model = render_sidebar(models)

render_dashboard(selected_model)

df = render_prediction_mode()

if df is not None:

    X_test, y_test = render_dataset_preview(df)

    predictions, prediction_df = render_prediction(selected_model, models, scaler, label_encoder, X_test)

    if predictions is not None:

        if y_test is not None:

            model = models[selected_model]

            if selected_model in [
                "Logistic Regression",
                "K-Nearest Neighbors"
            ]:
                X_eval = scaler.transform(X_test)
            else:
                X_eval = X_test

            metrics = evaluate_model(model, X_eval, y_test, predictions)

            render_metrics(metrics)

            render_confusion_matrix(metrics, label_encoder)

            render_classification_report(metrics)

            render_feature_importance(model, X_test.columns, selected_model)

        render_download(prediction_df)