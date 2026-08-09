# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st


# ==========================================================
# Display Metrics
# ==========================================================

def render_metrics(metrics):

    """
    Display evaluation metrics.
    """

    st.markdown("---")

    st.header("📊 Model Evaluation")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Accuracy",
        f"{metrics['accuracy']:.4f}"
    )

    c2.metric(
        "Precision",
        f"{metrics['precision']:.4f}"
    )

    c3.metric(
        "Recall",
        f"{metrics['recall']:.4f}"
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "F1 Score",
        f"{metrics['f1']:.4f}"
    )

    if metrics["auc"] is not None:

        c5.metric(
            "AUC",
            f"{metrics['auc']:.4f}"
        )

    else:

        c5.metric(
            "AUC",
            "N/A"
        )

    c6.metric(
        "MCC",
        f"{metrics['mcc']:.4f}"
    )