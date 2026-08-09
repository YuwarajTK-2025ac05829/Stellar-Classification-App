# 🌌 Stellar Classification using Machine Learning

---

# A. Problem Statement

The objective of this project is to develop a **Multi-Class Classification** model that can accurately classify celestial objects into one of the following categories:

- 🌌 Galaxy
- ⭐ Star
- ✨ Quasi-Stellar Object (QSO)

The project utilizes the **SDSS Stellar Classification Dataset** and compares the performance of five supervised machine learning algorithms:

- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Gaussian Naive Bayes
- Random Forest (Ensemble)

The best-performing model is integrated into a **Streamlit web application**, allowing users to upload a dataset, manually enter feature values, perform predictions, evaluate model performance, and download prediction results.

---

# B. Dataset Description

**Dataset Name:** SDSS Stellar Classification Dataset

**Dataset Source:**

https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17

## Dataset Summary

| Property | Value |
|----------|-------|
| Problem Type | Multi-Class Classification |
| Number of Samples | 100,000 |
| Number of Features | 14 |
| Target Classes | 3 |
| Target Variable | class |

## Input Features

| No | Feature |
|----|---------|
|1|alpha|
|2|delta|
|3|u|
|4|g|
|5|r|
|6|i|
|7|z|
|8|run_ID|
|9|cam_col|
|10|field_ID|
|11|redshift|
|12|plate|
|13|MJD|
|14|fiber_ID|

## Target Classes

- GALAXY
- STAR
- QSO

---

# C. GitHub Repository Link

GitHub Repository:

https://github.com/YuwarajTK-2025ac05829/Stellar-Classification-App

> Replace the above URL with your actual GitHub repository link before submission.

---

# D. Model Comparison

| ML Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|----------|----------|------|-----------|--------|----------|------|
| Logistic Regression | 0.9576 | 0.9863 | 0.9576 | 0.9576 | 0.9571 | 0.9248 |
| Decision Tree | 0.9673 | 0.9699 | 0.9673 | 0.9673 | 0.9673 | 0.9420 |
| K-Nearest Neighbors | 0.9032 | 0.9498 | 0.9060 | 0.9032 | 0.9019 | 0.8258 |
| Gaussian Naive Bayes | 0.6911 | 0.7947 | 0.6492 | 0.6911 | 0.6181 | 0.4366 |
| Random Forest (Ensemble) | **0.9794** | **0.9948** | **0.9793** | **0.9794** | **0.9792** | **0.9633** |

---

# E. Model Performance Observations

| ML Model | Observation about Model Performance |
|----------|-------------------------------------|
| **Logistic Regression** | Logistic Regression achieved an accuracy of **95.76%** and provided a strong baseline for the classification task. It produced balanced predictions across all three classes with high precision, recall, and F1-score. |
| **Decision Tree** | Decision Tree improved the overall accuracy to **96.73%** by effectively learning non-linear decision boundaries. It demonstrated better performance than Logistic Regression but may be more susceptible to overfitting. |
| **K-Nearest Neighbors (KNN)** | KNN achieved an accuracy of **90.32%**. Although its performance was satisfactory, it was lower than Decision Tree and Random Forest because of its sensitivity to feature scaling and neighboring sample distribution. |
| **Gaussian Naive Bayes** | Gaussian Naive Bayes produced the lowest performance with an accuracy of **69.11%**. The model struggled to classify the QSO class accurately because the independence assumption among features was not well suited for this dataset. |
| **Random Forest (Ensemble)** | Random Forest achieved the highest performance among all evaluated models. It obtained an accuracy of **97.94%**, an AUC of **0.9948**, and the highest Precision, Recall, F1-score, and MCC, demonstrating excellent generalization capability. |
| **Overall Winner for the Dataset** | **Random Forest (Ensemble)** was selected as the final model because it achieved the best performance across all evaluation metrics. It provided the highest classification accuracy and the most robust predictions, making it the most suitable model for deployment in the Streamlit application. |

---

# Project Structure

```
Stellar-Classification-App/
│
├── app.py
├── README.md
├── requirements.txt
├── test_data.csv
│
├── models/
│   ├── logistic_regression.pkl
│   ├── decision_tree.pkl
│   ├── knn.pkl
│   ├── gaussian_nb.pkl
│   ├── random_forest.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── components/
│   ├── sidebar.py
│   ├── dashboard.py
│   ├── prediction_mode.py
│   ├── dataset_preview.py
│   ├── prediction.py
│   ├── metrics.py
│   ├── confusion_matrix.py
│   ├── classification_report.py
│   ├── feature_importance.py
│   └── download.py
│
└── utils/
    ├── model_loader.py
    └── evaluation.py
```

---

# How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/YuwarajTK-2025ac05829/Stellar-Classification-App.git
```

## 2. Navigate to the Project Folder

```bash
cd Stellar-Classification-using-Machine-Learning
```

## 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

## 4. Launch the Streamlit Application

```bash
streamlit run app.py
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

---

# Author

**Yuwaraj T K**

M.Tech Artificial Intelligence & Machine Learning

BITS Pilani – Work Integrated Learning Programme