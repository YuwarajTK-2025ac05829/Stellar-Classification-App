# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import pandas as pd


# ==========================================================
# Feature Importance
# ==========================================================

def render_feature_importance(model, feature_names, selected_model):

    # ------------------------------------------------------
    # Applicable Models
    # ------------------------------------------------------

    if selected_model not in [
        "Decision Tree",
        "Random Forest"
    ]:
        return

    st.markdown("---")
    st.header("⭐ Feature Importance")

    # ------------------------------------------------------
    # Create Importance DataFrame
    # ------------------------------------------------------

    importance = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })

    importance = (
        importance
        .sort_values(
            by="Importance",
            ascending=False
        )
        .head(10)
        .round(4)
    )

    # ------------------------------------------------------
    # Bar Chart
    # ------------------------------------------------------

    st.subheader("Top 10 Feature Importance")

    st.bar_chart(
        importance.set_index("Feature"),
        height=350
    )

    # ------------------------------------------------------
    # Table
    # ------------------------------------------------------

    st.subheader("Feature Importance Values")

    html = importance.to_html(
        classes="feature-table",
        index=False,
        border=0
    )

    st.markdown("""
    <style>

    .feature-table{
        width:100%;
        border-collapse:collapse;
        font-size:18px;
        margin-top:10px;
    }

    .feature-table th{
        background:#1f2937;
        color:white;
        font-size:20px;
        font-weight:bold;
        padding:12px;
        text-align:center;
        border:1px solid #444;
    }

    .feature-table td{
        font-size:18px;
        padding:10px;
        text-align:center;
        border:1px solid #444;
    }

    .feature-table tr:nth-child(even){
        background:#111827;
    }

    .feature-table tr:nth-child(odd){
        background:#0f172a;
    }

    .feature-table tr:hover{
        background:#1e293b;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(html, unsafe_allow_html=True)