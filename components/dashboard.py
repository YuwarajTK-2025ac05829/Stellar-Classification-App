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

    c1.metric("Dataset", "Stellar Classification")

    c1.markdown(
        """
        <a href="https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17"
        target="_blank">
        🔗 Open Dataset
        </a>
        """,
        unsafe_allow_html=True
    )


    
    c2.metric("Features", "14")
    c3.metric("Classes", "3")
    c4.metric("Model", selected_model)

    st.markdown("---")