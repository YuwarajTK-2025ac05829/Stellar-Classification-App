# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import pandas as pd

# ==========================================================
# Dataset Preview
# ==========================================================

def render_dataset_preview(df):
    """
    Display dataset preview and dataset information.

    Returns
    -------
    X_test : DataFrame
    y_test : Series or None
    """

    if df is None:
        return None, None

    st.markdown("---")

    # ======================================================
    # Dataset Preview
    # ======================================================

    st.header("📄 Dataset Preview")

    with st.expander("View Dataset", expanded=True):

        st.dataframe(
            df.head(),
            width="stretch"
        )

    # ======================================================
    # Dataset Information
    # ======================================================

    st.subheader("Dataset Information")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    if "class" in df.columns:

        X_test = df.drop(columns=["class"])
        y_test = df["class"]

        col3.metric("Features", X_test.shape[1])
        col4.metric("Target", "Available")

    else:

        X_test = df
        y_test = None

        col3.metric("Features", X_test.shape[1])
        col4.metric("Target", "Not Available")

    # ======================================================
    # Dataset Validation
    # ======================================================

    required_columns = [
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

    uploaded_columns = list(X_test.columns)

    missing_columns = [
        col for col in required_columns
        if col not in uploaded_columns
    ]

    extra_columns = [
        col for col in uploaded_columns
        if col not in required_columns
    ]

    missing_values = X_test.isnull().sum().sum()

    # Wrong dataset
    if missing_columns or extra_columns:

        st.error("❌ Invalid dataset format detected.")

        if missing_columns:
            st.write(
                "**Missing Columns:** " +
                ", ".join(missing_columns)
            )

        if extra_columns:
            st.write(
                "**Unexpected Columns:** " +
                ", ".join(extra_columns)
            )

        st.write("### Expected Dataset Structure")

        sample_df = pd.DataFrame(columns=required_columns)

        st.dataframe(
            sample_df,
            width="stretch",
            hide_index=True
        )

        # Stop here
        return None, None

    # Missing values
    elif missing_values > 0:

        st.warning(
            f"⚠️ Dataset contains {missing_values} missing value(s)."
        )

    # Everything is valid
    else:

        st.success(
            "✅ Dataset format is valid. No missing values detected."
        )

    return X_test, y_test