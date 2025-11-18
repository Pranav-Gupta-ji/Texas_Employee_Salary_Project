# Texas Employee Salary Predictor 💰

link_of_Salary_datasets : https://d3ilbtxij3aepc.cloudfront.net/projects/CDS-Capstone-Projects/salary.zip

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**A Machine Learning solution for predicting Texas state employee salaries with 83% accuracy**

[Overview](#-overview) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Model Performance](#-model-performance) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

This project builds a predictive model to forecast monthly salaries for Texas state government employees based on various factors including agency, job classification, employment status, and demographics. The model helps the Texas state government understand compensation patterns and make data-driven decisions for payroll forecasting and budget planning.

### 🎯 Key Objectives

- **Predict** monthly salaries for Texas state employees
- **Analyze** compensation patterns across 109+ state agencies
- **Identify** salary trends based on demographics and job classifications
- **Support** budget planning and fair compensation policies

## ✨ Features

### 🤖 Machine Learning Model
- **Decision Tree Regressor** with optimized hyperparameters
- **Custom Sklearn Pipeline** with automated preprocessing
- **83% prediction accuracy** (R² = 0.832)
- **Log-transformed target** for better predictions
- **Sample weighting** to handle extreme salary values

### 📊 Comprehensive Analysis
- Exploratory Data Analysis (EDA) with visualizations
- Salary distribution across agencies and job titles
- Demographic analysis (ethnicity, gender)
- Employment status impact (Full-time vs Part-time)
- Feature importance and correlation analysis

### 🛠️ Production-Ready Components
- Custom transformers compatible with sklearn
- Serialized model ready for deployment
- Modular and reusable code structure
- Comprehensive documentation

## 📈 Model Performance

| Metric | Value | Description |
|--------|-------|-------------|
| **R² Score** | 0.832 | Explains 83% of salary variance |
| **Adjusted R²** | 0.832 | Adjusted for feature count |
| **MAE** | $3,843.19| Mean Absolute Error |
| **RMSE** | $7,555.52 | Root Mean Squared Error |

### Performance Rating
- ⭐⭐⭐⭐⭐⭐⭐⭐ **Model Accuracy** (8/10) - Strong for HR data
- ⭐⭐⭐⭐⭐⭐ **Error Stability** (6/10) - Manageable outliers
- ⭐⭐⭐⭐⭐⭐⭐⭐ **Practical Use** (8/10) - Deployment-ready

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/Pranav-Gupta-ji/texas-salary-predictor.git
cd texas-salary-predictor

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Requirements

```txt
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
category-encoders>=2.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
joblib>=1.1.0
jupyter>=1.0.0
```

## 💻 Usage

### Quick Start - Making Predictions

```python
import joblib
import pandas as pd

# 1. Load model
model = joblib.load('model_simple.pkl')

# 2. Prepare input
new_employee = pd.DataFrame({
    'AGENCY_NAME': ['HEALTH AND HUMAN SERVICES COMMISSION'],
    'CLASS_TITLE': ['REGISTERED NURSE'],
    'ETHNICITY': ['WHITE'],
    'GENDER': ['FEMALE'],
    'STATUS': ['FULL-TIME']
})

# 3. Predict salary
predicted_salary = model.predict(new_employee)
print(f"Predicted Annual Salary: ${predicted_salary[0]:,.2f}")
```

### Running the Jupyter Notebook

```bash
# Start Jupyter Notebook
jupyter notebook

# Open Texas_Salary_Prediction.ipynb
# Run all cells to see the complete analysis
```

### Model Training (from scratch)

```python
from sklearn.model_selection import train_test_split
import pandas as pd

# Load data
data = pd.read_csv('salary.csv')

# Prepare features and target
X = data[['AGENCY NAME', 'CLASS TITLE', 'ETHNICITY', 
          'GENDER', 'STATUS']]
y = data['ANNUAL']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Fit pipeline (see notebook for complete pipeline definition)
pipeline.fit(X_train, y_train)

# Evaluate
predictions = pipeline.predict(X_test)
```

## 📊 Dataset Information

### Dataset Overview
- **Total Records**: 149,481 Texas state employees
- **Features**: 5 input features + 1 target variable
- **Coverage**: All major Texas state agencies

### Features Description

| Feature | Type | Description | Unique Values |
|---------|------|-------------|---------------|
| `AGENCY NAME` | Categorical | State department/agency | 109 |
| `CLASS TITLE` | Categorical | Job classification | 1,842 |
| `ETHNICITY` | Categorical | Employee ethnicity | 5 |
| `GENDER` | Binary | Male/Female | 2 |
| `STATUS` | Categorical | Employment status | 11 → 2 |
| `ANNUAL` | Numeric | **Target**: Annual salary | Continuous |

### Top 5 Agencies (70% of data)
1. Texas Health and Human Services
2. Texas Department of Criminal Justice
3. Texas Department of Transportation
4. Department of Family and Protective Services
5. Department of Public Safety

## 🏗️ Project Structure

```
Taxes_Salary_Estimator/
│
├── __pycache__/                    # Python cache files
├── venv/                           # Virtual environment
├── main.py                         # Main application script
├── model_simple.pkl                       # Trained model (serialized)
├── Readme.md                       # Project documentation
├── requirements.txt                # Python dependencies
├── salary.csv                      # Dataset (149,481 records)
|
└── Texas_Salary_Prediction.ipynb   # Main analysis notebook
```


## 📉 Key Findings

### 💡 Insights from Analysis

1. **Agency Impact**: Criminal Justice and Health departments dominate employment (70%+)
2. **Gender Patterns**: Males earn ~15-20% more in part-time positions
3. **Ethnic Variations**: "Other" category shows highest full-time compensation
4. **Job Classification**: Strongest predictor of salary (high cardinality handled via frequency encoding)
5. **Employment Status**: Full-time positions show significantly higher compensation

### 📊 Correlation Findings
- **Monthly ↔ Annual**: 0.99 correlation (removed Annual from model)
- **Agency ↔ Salary**: Strong predictor through frequency encoding
- **Status ↔ Salary**: Full-time earns significantly more

## 🎓 Use Cases

### For Government
- 💼 Budget forecasting and payroll planning
- 📈 Compensation benchmarking across agencies
- ⚖️ Ensuring pay equity and fairness
- 🎯 Data-driven salary structure reforms

### For Employees
- 💰 Salary negotiation support
- 📊 Career path planning
- 🔍 Benchmark compensation in similar roles

### For Researchers
- 📚 Public sector compensation analysis
- 🌍 Labor market economic studies
- 📉 Pay gap research and analysis

## 🔮 Future Enhancements

- [ ] Add **years of experience** as a feature
- [ ] Implement **geographic location** analysis (city-level)
- [ ] Build **interactive web dashboard** (Streamlit/Flask)
- [ ] Deploy as **REST API** for real-time predictions
- [ ] Integrate **time-series forecasting** for salary trends
- [ ] Implement **ensemble methods** (Random Forest, XGBoost)
- [ ] Add **explainability** with SHAP values
- [ ] Create **automated reporting** system

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

### Contribution Guidelines
- Write clear commit messages
- Add unit tests for new features
- Update documentation as needed
- Follow PEP 8 style guidelines

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## 🙏 Acknowledgments

- **Texas State Government** for providing public salary data
- **Scikit-learn** community for excellent ML tools
- **Category Encoders** library for advanced encoding techniques
- Open-source community for inspiration and support

## 📞 Contact

**Pranav Gupta**

- GitHub: [@Pranav-Gupta-ji](https://github.com/Pranav-Gupta-ji)
- LinkedIn: [[Pranav Gupta](https://www.linkedin.com/in/pranavguptaji/)]
- Email: pranavgupta922@gmail.com

---

<div align="center">

### ⭐ If you find this project helpful, please give it a star!

**Made with ❤️ by Pranav Gupta**

</div>

---

## 🛡️ Disclaimer

This project uses publicly available Texas state employee salary data. The predictions are based on statistical modeling and should not be considered as official salary determinations. Actual salaries may vary based on specific circumstances, budget constraints, seniority, and individual qualifications.

For official compensation decisions, always consult with HR professionals and relevant state authorities.

---

## 📚 Documentation

For detailed analysis and methodology, please refer to:
- [Jupyter Notebook](Texas_Salary_Prediction.ipynb) - Complete analysis
- [Custom Transformers](custom_transformers.py) - Preprocessing code
- [Main Script](main.py) - Application entry point
- [Schema Definitions](schema.py) - Data structure definitions

## 🎯 Model Pipeline Architecture

```
Input Data
    ↓
[Column Name Cleaner]
    ↓
[Column Transformer - Parallel Processing]
    │
    ├── Ethnicity Pipeline
    │   ├── SimpleImputer (most_frequent)
    │   ├
    │   ├── OrdinalEncoder
    │   └── MinMaxScaler
    │
    ├── Gender Pipeline
    │   ├── SimpleImputer (most_frequent)
    │   ├── OrdinalEncoder
    │   └── MinMaxScaler
    │
    ├── Status Pipeline
    │   ├── SimpleImputer (most_frequent)
    │   |
    │   ├── OrdinalEncoder
    │   └── MinMaxScaler
    │
    └── Frequency Encoding Pipeline (AGENCY, CLASS_TITLE)
        ├── SimpleImputer (most_frequent)
        ├── CountEncoder (normalized)
        └── MinMaxScaler
    ↓
[TransformedTargetRegressor]
    ├── Target Transform: log1p
    ├── Model: DecisionTreeRegressor
    └── Inverse Transform: expm1
    ↓
Predictions (Monthly Salary)
```

---

<div align="center">

**Happy Predicting! 🚀**


</div>


