import streamlit as st


def render_dashboard(selected_model):
    """
    Display project title and dashboard metrics.
    """

    st.title("🌌 Stellar Classification using Machine Learning")

    st.markdown("---")

    st.write(
        """
        This application predicts whether a celestial object is a

        - 🌌 GALAXY
        - ⭐ STAR
        - ✨ QSO

        using supervised Machine Learning models.
        """
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Dataset", "SDSS17")
    c2.metric("Features", "14")
    c3.metric("Classes", "3")
    c4.metric("Model", selected_model)

    st.markdown("---")