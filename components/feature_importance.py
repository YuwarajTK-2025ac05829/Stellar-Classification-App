# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import pandas as pd


# ==========================================================
# Feature Importance
# ==========================================================

def render_feature_importance(model, feature_names, selected_model):

    if selected_model not in [
        "Decision Tree",
        "Random Forest"
    ]:
        return

    st.markdown("---")
    st.header("⭐ Feature Importance")

    importance = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    st.bar_chart(
        importance.set_index("Feature")
    )

    st.dataframe(
        importance,
        width="stretch"
    )