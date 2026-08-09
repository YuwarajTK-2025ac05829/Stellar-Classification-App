# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import pandas as pd

from utils.evaluation import evaluate_model


# ==========================================================
# Model Comparison
# ==========================================================

def render_model_comparison(
    prediction_results,
    selected_models,
    y_test
):
    """
    Compare the performance of multiple machine learning models.

    Returns
    -------
    comparison_df : DataFrame
    best_model : str
    """

    if prediction_results is None or y_test is None:
        return None, None

    st.markdown("---")
    st.header("📊 Model Comparison")

    comparison = []

    for model_name in selected_models:

        result = prediction_results[model_name]
        
        metrics = evaluate_model(
            result["model"],
            result["X"],
            y_test,
            result["predictions"]
        )

        comparison.append({
            "Model": model_name,
            "Accuracy": metrics["accuracy"],
            "Precision": metrics["precision"],
            "Recall": metrics["recall"],
            "F1 Score": metrics["f1"],
            "AUC": metrics["auc"],
            "MCC": metrics["mcc"]
        })

    comparison_df = pd.DataFrame(comparison)

    # Sort by Accuracy
    comparison_df = comparison_df.sort_values(
        by="Accuracy",
        ascending=False
    )

    # Format numbers
    numeric_cols = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "AUC",
        "MCC"
    ]

    comparison_display = comparison_df.copy()

    for col in numeric_cols:
        comparison_display[col] = comparison_display[col].map(
            lambda x: f"{x:.4f}" if pd.notna(x) else "N/A"
        )

    st.dataframe(
        comparison_display,
        width="stretch",
        hide_index=True
    )

    best_model = comparison_df.iloc[0]["Model"]

    st.success(
        f"🏆 Best Performing Model: **{best_model}** "
        f"(Accuracy: {comparison_df.iloc[0]['Accuracy']:.4f})"
    )

    return comparison_df, best_model