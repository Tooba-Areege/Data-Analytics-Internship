# 📊 Task 02: Data Cleaning Basics

## 👩‍💻 Internship Information

**Internship:** CoreTech data analysis Internship  
**Task:** Task 02 – Data Cleaning Basics  
**Name:** Tooba Areege
**Education:** 2nd Year statistics Student at Shaheed Benazir Bhutto University  
**City:** Mehrabpur, Sindh, Pakistan  

---

## 🎯 Objective

The objective of this task is to practice the fundamental data cleaning process using Python and Pandas. A raw public Titanic dataset was explored and cleaned by identifying and handling missing values, removing duplicate records, and correcting inappropriate data types.

---

## 📊 Dataset

The **Titanic Dataset** contains passenger information such as passenger class, name, gender, age, fare, cabin, and survival status.

The dataset was analyzed using Python and Pandas. Missing values in the `Age` column were filled using the median, missing values in `Embarked` were replaced with the mode, and missing `Cabin` values were labeled as `Unknown`. Duplicate records were identified and removed, and column data types were checked and corrected where necessary.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Visual Studio Code

---

## 🔄 Data Cleaning Workflow

```text
Raw Dataset
     ↓
Explore Data
     ↓
Check Missing Values
     ↓
Handle Missing Values
     ↓
Remove Duplicate Rows
     ↓
Fix Data Types
     ↓
Final Quality Check
     ↓
Export Cleaned Dataset

 Task_02_Data_Cleaning/
│
├── README.md
├── task_02_data_cleaning.py
├── Titanic-Dataset.csv
└── cleaned_titanic.csv

 Conclusion
The Titanic dataset was successfully cleaned by handling missing values, removing duplicate records, and correcting data types. The cleaned dataset is now more consistent and ready for further data analysis, visualization, and machine learning tasks.
This task provided practical experience with the essential data preprocessing steps used in the data analytics workflow.
