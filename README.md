# 🧠 Job Role Prediction System

This project is a **Machine Learning-based Job Role Predictor** that takes in job-related information such as **expected salary, experience, requirements, and job description** to predict the most likely **job role/title** using Natural Language Processing (NLP) and classification models.

A user-friendly **Streamlit web interface** allows users to interact with the system easily.

---

## 🚀 Features

- Cleaned and preprocessed dataset with salary normalization
- TF-IDF vectorization of text fields (`requirement`, `description`)
- Label encoding of target variable (job titles)
- Trained `VotingClassifier` using:
  - Logistic Regression
  - Random Forest
- Streamlit-based GUI for real-time prediction

---

## 📂 Project Structure

```
📁 Job_Prediction_System/
│
├── app.py                     # Streamlit GUI file
├── Dataset_jotpars.csv        # Raw job data
├── Job_prediction_system.pkl  # Trained ML model
├── column_transformer.pkl     # Fitted ColumnTransformer
├── label_encoder.pkl          # Trained LabelEncoder
├── requirements.txt           # Project dependencies
└── README.md                  # This file
```

---

## 💻 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Job_Prediction_System.git
cd Job_Prediction_System
```

### 2. Install dependencies

Create a virtual environment (recommended):

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📊 Sample Input Fields

- **Salary** (numeric): e.g. `500000`
- **Experience** (numeric): e.g. `2`
- **Requirement**: e.g. `Python, SQL, Machine Learning`
- **Description**: e.g. `We are looking for an experienced data analyst...`

---

## 🛠️ Tech Stack

- Python
- Pandas, Scikit-learn
- NLP (TF-IDF)
- Streamlit
- Pickle (model serialization)

---

## 🔮 Prediction Output

Based on input details, the system predicts the most likely **job title/role**, such as:

```
Predicted Job Role: Data Analyst
```

---

## 🤝 Contributions

Feel free to open issues, submit pull requests or give suggestions to improve this project!

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙋‍♂️ Author

**Aman Mani Tripathi**  
🔗 [LinkedIn](https://www.linkedin.com/in/aman-mani-tripathi-744320299/)  
📁 GitHub: [amantripathi-dev](https://github.com/Amanpandit87)
