# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st


# ==========================================================
# Download Predictions
# ==========================================================

def render_download(prediction_df):

    if prediction_df is None:
        return

    st.markdown("---")

    st.header("💾 Download Predictions")

    csv = prediction_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Prediction Results",
        data=csv,
        file_name="prediction_results.csv",
        mime="text/csv",
        width="stretch"
    )