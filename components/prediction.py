# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import pandas as pd
import time


# ==========================================================
# Prediction
# ==========================================================

def render_prediction(
    selected_models,
    models,
    scaler,
    label_encoder,
    X_test
):
    """
    Perform predictions using one or more selected models.

    Returns
    -------
    prediction_results : dict
    """

    if X_test is None:
        return None

    st.markdown("---")
    st.header("🚀 Prediction")

    st.write("**Selected Model(s):**")
    st.write(", ".join(selected_models))

    # ======================================================
    # Check if cached predictions belong to current models
    # ======================================================

    cached_results = st.session_state.get("prediction_results")
    cached_models = st.session_state.get("prediction_models")

    if (
        cached_results is not None
        and cached_models == selected_models
    ):

        st.success("✅ Predictions are already available.")

        if st.button(
            "🔄 Run Prediction Again",
            type="primary",
            width="stretch"
        ):

            st.session_state.pop("prediction_results", None)
            st.session_state.pop("prediction_models", None)
            st.rerun()

        return cached_results

    # ======================================================
    # Model selection changed
    # ======================================================

    if cached_results is not None and cached_models != selected_models:

        st.info(
            "ℹ️ Model selection changed. Click **Run Prediction** to generate new predictions."
        )

    # ======================================================
    # Run Prediction Button
    # ======================================================

    if st.button(
        "🚀 Run Prediction",
        type="primary",
        width="stretch"
    ):

        prediction_results = {}

        progress_bar = st.progress(
            0,
            text="Starting prediction..."
        )

        elapsed_box = st.empty()

        total_models = len(selected_models)

        start_time = time.time()

        prediction_times = {}

        with st.spinner("Running predictions... Please wait..."):

            for index, model_name in enumerate(selected_models):

                progress_bar.progress(
                    (index + 1) / total_models,
                    text=f"Processing {model_name} ({index+1}/{total_models})"
                )

                elapsed_box.caption(
                    f"⏱ Elapsed Time: {time.time()-start_time:.2f} seconds"
                )

                model = models[model_name]

                # --------------------------------------------------
                # Scaling
                # --------------------------------------------------

                if model_name in [
                    "Logistic Regression",
                    "K-Nearest Neighbors"
                ]:

                    X = scaler.transform(X_test)

                else:

                    X = X_test

                # --------------------------------------------------
                # Prediction
                # --------------------------------------------------

                model_start = time.perf_counter()

                predictions = model.predict(X)

                prediction_times[model_name] = (
                    time.perf_counter() - model_start
                )

                # --------------------------------------------------
                # Decode labels
                # --------------------------------------------------

                if predictions.dtype != object:

                    predicted_labels = (
                        label_encoder.inverse_transform(predictions)
                    )

                else:

                    predicted_labels = predictions

                prediction_df = X_test.copy()

                prediction_df["Predicted Class"] = predicted_labels

                prediction_results[model_name] = {
                    "model": model,
                    "X": X,
                    "predictions": predictions,
                    "prediction_df": prediction_df
                }

        progress_bar.empty()
        elapsed_box.empty()

        total_time = time.time() - start_time

        # ======================================================
        # Save Results
        # ======================================================

        st.session_state["prediction_results"] = prediction_results
        st.session_state["prediction_models"] = selected_models.copy()

        st.success(
            f"✅ Prediction completed successfully in {total_time:.2f} seconds."
        )

        summary_df = pd.DataFrame({
            "Model": list(prediction_times.keys()),
            "Prediction Time (ms)": [
                round(x * 1000, 2)
                for x in prediction_times.values()
            ]
        })

        st.subheader("📋 Model Execution Summary")

        st.dataframe(
            summary_df,
            width="stretch",
            hide_index=True
        )

        if len(selected_models) == 1:

            model_name = selected_models[0]

            st.subheader("Prediction Results")

            st.dataframe(
                prediction_results[model_name]["prediction_df"].head(),
                width="stretch"
            )

        else:

            st.info(
                "📊 Multiple models selected. Comparison results are available below."
            )

        return prediction_results

    return None