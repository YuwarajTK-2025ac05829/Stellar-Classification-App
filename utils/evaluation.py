# ==========================================================
# Import Libraries
# ==========================================================

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    matthews_corrcoef,
    confusion_matrix,
    classification_report
)


# ==========================================================
# Calculate Evaluation Metrics
# ==========================================================

def evaluate_model(model, X_test, y_test, predictions):

    """
    Calculate all evaluation metrics.

    Returns
    -------
    metrics : dict
    """

    metrics = {}

    metrics["accuracy"] = accuracy_score(
        y_test,
        predictions
    )

    metrics["precision"] = precision_score(
        y_test,
        predictions,
        average="weighted"
    )

    metrics["recall"] = recall_score(
        y_test,
        predictions,
        average="weighted"
    )

    metrics["f1"] = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    metrics["mcc"] = matthews_corrcoef(
        y_test,
        predictions
    )

    # ------------------------------------------------------
    # AUC
    # ------------------------------------------------------

    try:

        probabilities = model.predict_proba(X_test)

        metrics["auc"] = roc_auc_score(
            y_test,
            probabilities,
            multi_class="ovr"
        )

    except Exception:

        metrics["auc"] = None

    # ------------------------------------------------------

    metrics["confusion_matrix"] = confusion_matrix(
        y_test,
        predictions
    )

    metrics["classification_report"] = classification_report(
        y_test,
        predictions
    )

    return metrics