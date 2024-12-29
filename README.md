# 📊 Student Performance Prediction

PROJECT LINK : https://student-performance-prediction-1jf3.onrender.com

## 🚀 Overview
This project aims to predict students' academic performance based on various socio-economic, demographic, and educational factors. The model uses machine learning techniques to help educators and policymakers understand the key factors influencing student success.


## 🎯 Project Objective
The main objective of this project is to build a predictive model that can identify students at risk of poor academic performance. By leveraging data on students' background, parental education, and study habits, the model helps in making data-driven decisions to improve educational outcomes.


## 📁 Table of Contents
Features
Tech Stack
Dataset
Modeling Approach
Installation
Usage
Results
Future Work
Contributing
License
Contact


## ✨ Features
Exploratory Data Analysis (EDA) to understand key factors affecting performance.
Data Preprocessing: Handling missing values, encoding categorical variables, and feature scaling.
Model Training: Multiple algorithms tested including Decision Tree, Random Forest, and Logistic Regression.
Model Evaluation: Metrics such as Accuracy, Precision, Recall, and F1-Score are used to assess model performance.
Hyperparameter Tuning for optimizing model performance.
Visualization of results for better interpretability.


## 🛠️ Tech Stack
Programming Language: Python
Libraries:
Data Analysis: Pandas, NumPy
Visualization: Matplotlib, Seaborn
Machine Learning: scikit-learn
Tools: Jupyter Notebook


## 📊 Dataset
Source: The dataset is available on UCI Machine Learning Repository or any other relevant source.
Description: The dataset contains information about students' academic performance and various socio-economic factors like parental education, family support, and study time.
Key Features:
age: Age of the student
sex: Gender of the student
studytime: Weekly study time
failures: Number of past class failures
G1, G2, G3: Grades in the first, second, and final period


## 📈 Modeling Approach
Data Cleaning & Preprocessing


Handling missing values
Encoding categorical features
Feature scaling and normalization
Exploratory Data Analysis (EDA)


Visualizing data distributions and correlations
Identifying significant features affecting performance
Model Training


Models used: Decision Tree, Random Forest, Logistic Regression
Hyperparameter tuning using GridSearchCV
Cross-validation for reliable performance estimation
Model Evaluation


Metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC
Confusion Matrix to evaluate classification results


## 🛠️ Installation
Prerequisites
Python 3.x
Jupyter Notebook
Clone the Repository
bash
Copy code
git clone https://github.com/Soham-003/StudentPerformancePrediction.git
cd StudentPerformancePrediction
Install Dependencies
bash
Copy code
pip install -r requirements.txt


## 🚀 Usage
Open the Jupyter Notebook

bash
Copy code
jupyter notebook Student_Performance_Prediction.ipynb
Run All Cells

Execute the cells step by step to understand data loading, preprocessing, model training, and evaluation.
Predict on New Data

Modify the notebook to load your own dataset or use the existing model to make predictions.


## 📊 Results
The best model achieved an accuracy of 85% on the test dataset.

Confusion Matrix:

Predicted Positive	Predicted Negative
Actual Positive	True Positive (TP)	False Negative (FN)
Actual Negative	False Positive (FP)	True Negative (TN)
Precision: 0.82

Recall: 0.87

F1-Score: 0.84


## 🔮 Future Work

Implement deep learning models for potentially higher accuracy.
Integrate feature selection techniques to reduce dimensionality.
Develop a user-friendly web interface using Flask or Streamlit for real-time predictions.
Extend the analysis to predict other aspects of student behavior, such as dropout rates.


## 🤝 Contributing
Contributions are welcome! If you'd like to improve this project:

Fork the repository.
Create your feature branch: git checkout -b feature/YourFeature
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature/YourFeature
Open a pull request.


## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
Author: Soham Khanna
Email: sohamsavankhanna@gmail.com
LinkedIn: Soham Khanna
