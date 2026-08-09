import streamlit as st


def model_selection(models):

    st.markdown("---")
    st.header("🤖 Select Machine Learning Model(s)")

    selected_models = st.multiselect(
        "Choose one or more models",
        options=list(models.keys()),
        default=["Random Forest"]
    )

    if len(selected_models) == 0:
        st.warning("Please select at least one model.")
        st.stop()

    return selected_models