# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st


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
    # Missing Values
    # ======================================================

    missing_values = df.isnull().sum().sum()

    if missing_values == 0:

        st.success("✅ No missing values detected.")

    else:

        st.warning(f"⚠️ Missing Values : {missing_values}")

    return X_test, y_test