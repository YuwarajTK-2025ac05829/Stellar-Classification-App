# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import pandas as pd


# ==========================================================
# Prediction
# ==========================================================

def render_prediction(
    selected_model,
    models,
    scaler,
    label_encoder,
    X_test
):
    """
    Perform prediction using the selected model.

    Returns
    -------
    predictions : ndarray
    prediction_df : DataFrame
    """

    if X_test is None:
        return None, None

    st.markdown("---")
    st.header("🚀 Prediction")

    st.write(f"**Selected Model:** {selected_model}")

    if st.button(
        f"Predict using {selected_model}",
        type="primary",
        width="stretch"
    ):

        model = models[selected_model]

        # ----------------------------------------------
        # Scale data only when required
        # ----------------------------------------------

        if selected_model in [
            "Logistic Regression",
            "K-Nearest Neighbors"
        ]:

            X = scaler.transform(X_test)

        else:

            X = X_test

        # ----------------------------------------------
        # Prediction
        # ----------------------------------------------

        predictions = model.predict(X)

        # ----------------------------------------------
        # Decode prediction labels
        # ----------------------------------------------

        if predictions.dtype != object:
            predicted_labels = label_encoder.inverse_transform(predictions)
        else:
            predicted_labels = predictions

        # ----------------------------------------------
        # Prediction DataFrame
        # ----------------------------------------------

        prediction_df = X_test.copy()

        prediction_df["Predicted Class"] = predicted_labels

        st.success("Prediction completed successfully!")

        st.subheader("Prediction Results")

        st.dataframe(
            prediction_df.head(),
            width="stretch"
        )

        return predictions, prediction_df

    return None, None