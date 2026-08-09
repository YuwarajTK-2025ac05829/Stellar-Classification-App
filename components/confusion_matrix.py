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

    # Smaller figure
    fig, ax = plt.subplots(figsize=(5, 4))

    disp = ConfusionMatrixDisplay(
        confusion_matrix=metrics["confusion_matrix"],
        display_labels=label_encoder.classes_
    )

    disp.plot(
        ax=ax,
        colorbar=False,
        cmap="Blues",
        values_format="d"
    )

    # Improve appearance
    ax.set_title("")
    ax.set_xlabel("Predicted Label", fontsize=10)
    ax.set_ylabel("True Label", fontsize=10)

    ax.tick_params(axis="both", labelsize=9)

    plt.tight_layout()

    # Center the figure
    left, center, right = st.columns([1, 2, 1])

    with center:
        st.pyplot(fig, width="content")

    plt.close(fig)