import streamlit as st


def render_sidebar(models):
    """
    Render sidebar and return the selected model.
    """

    st.sidebar.title("🌌 Stellar Classification")

    st.sidebar.markdown("---")

    selected_model = st.sidebar.selectbox(
        "🤖 Select Machine Learning Model",
        list(models.keys())
    )

    st.sidebar.markdown("---")

    st.sidebar.success(
        f"Selected Model\n\n**{selected_model}**"
    )

    return selected_model