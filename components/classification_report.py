# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st


# ==========================================================
# Classification Report
# ==========================================================

def render_classification_report(metrics):

    st.markdown("---")

    with st.expander("📋 Classification Report", expanded=True):

        st.text(metrics["classification_report"])