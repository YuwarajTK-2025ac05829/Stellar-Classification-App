# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import pandas as pd

# ==========================================================
# Prediction Mode
# ==========================================================

def render_prediction_mode():

    """
    Display the prediction mode section and return
    the selected dataset as a pandas DataFrame.
    """

    st.header("📂 Prediction Mode")

    prediction_mode = st.radio(
        "Choose how you want to provide the test data:",
        (
            "📂 Upload Test Dataset",
            "📁 Use Default Test Dataset",
            # "✍ Manual Input"
        ),
        horizontal=True,
        key="prediction_mode"
    )

    df = None

    # ======================================================
    # Upload CSV
    # ======================================================

    if prediction_mode == "📂 Upload Test Dataset":

        uploaded_file = st.file_uploader(
            "Upload test_data.csv",
            type=["csv"],
            key="uploaded_dataset"
        )

        if uploaded_file is not None:

            df = pd.read_csv(uploaded_file)

            st.session_state["input_df"] = df

            st.success("Dataset uploaded successfully!")

    # ======================================================
    # Default Dataset
    # ======================================================

    elif prediction_mode == "📁 Use Default Test Dataset":

        if "input_df" not in st.session_state:
            st.session_state["input_df"] = pd.read_csv("test_data.csv")

        df = st.session_state["input_df"]

        st.success("Default test dataset loaded successfully!")

    # ======================================================
    # Manual Input
    # ======================================================

    else:

        st.info("Enter feature values below.")

        feature_names = [
            "alpha",
            "delta",
            "u",
            "g",
            "r",
            "i",
            "z",
            "run_ID",
            "cam_col",
            "field_ID",
            "redshift",
            "plate",
            "MJD",
            "fiber_ID"
        ]

        manual_data = {}

        col1, col2 = st.columns(2)

        for i, feature in enumerate(feature_names):

            if i % 2 == 0:

                manual_data[feature] = col1.number_input(
                    feature,
                    value=0.0,
                    format="%.6f",
                    key=f"manual_{feature}"
                )

            else:

                manual_data[feature] = col2.number_input(
                    feature,
                    value=0.0,
                    format="%.6f",
                    key=f"manual_{feature}"
                )

        if st.button("Create Sample", type="primary"):

            st.session_state["input_df"] = pd.DataFrame([manual_data])

            st.success("Sample created successfully!")

        if "input_df" in st.session_state:
            df = st.session_state["input_df"]

    return df, prediction_mode