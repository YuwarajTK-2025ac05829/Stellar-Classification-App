import streamlit as st


def render_dashboard(selected_models):
    """
    Display project title and dashboard metrics.
    """

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
    if len(selected_models) == 1:
        model_name = selected_models[0]
    else:
        model_name = f"{len(selected_models)} Models"

    c4.metric("Selected", model_name)

    st.markdown("---")