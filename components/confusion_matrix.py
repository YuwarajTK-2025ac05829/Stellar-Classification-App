# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


# ==========================================================
# Confusion Matrix
# ==========================================================

def render_confusion_matrix(metrics, label_encoder):

    st.markdown("---")
    st.header("📊 Confusion Matrix")

    fig, ax = plt.subplots(figsize=(6, 6))

    disp = ConfusionMatrixDisplay(
        confusion_matrix=metrics["confusion_matrix"],
        display_labels=label_encoder.classes_
    )

    disp.plot(ax=ax, colorbar=False)

    st.pyplot(fig)