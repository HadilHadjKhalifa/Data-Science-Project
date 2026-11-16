# Customer Data Analysis & Data Cleaning

## Project Overview
This project focuses on data preparation, cleaning, validation, and feature engineering using Python and Excel.

The objective is to improve data quality, identify outliers, create meaningful features, and prepare the dataset for further data analysis.

## Project Objectives
- Explore and understand the dataset.
- Identify missing values and data inconsistencies.
- Detect and handle outliers.
- Perform feature engineering to create new variables.
- Convert categorical data into numerical format.
- Analyze correlations between numerical features.
- Validate data quality and consistency.

## Tools & Technologies
- **Python:** Main programming language.
- **Pandas:** Data manipulation and analysis.
- **NumPy:** Numerical operations.
- **Excel:** Dataset storage and exploration.
- **Pandera:** Data validation.

## Dataset Description
The project includes two dataset versions:

- `Dataset_notCleaned.xlsx`: Original dataset before data cleaning.
- `Dataset_cleaned.xlsx`: Processed dataset after cleaning and feature engineering.

## Methodology

### 1. Data Exploration
- Examining dataset structure.
- Checking missing values.
- Generating descriptive statistics.

### 2. Data Cleaning
- Handling missing values in the `CouponCode` column.
- Detecting outliers using the Interquartile Range (IQR) method.
- Applying outlier capping using lower and upper bounds.

### 3. Feature Engineering
- Creating a binary feature `HasCoupon`.
- Calculating customer order counts.
- Creating additional features from existing variables.

### 4. Data Transformation
- Applying One-Hot Encoding to categorical variables.
- Converting categorical values into numerical representations.

### 5. Correlation Analysis
- Calculating the correlation matrix.
- Identifying highly correlated features using a threshold of 0.80.

### 6. Data Validation
- Defining data types and validation rules using Pandera.
- Checking data consistency against the defined schema.

### 7. Exporting Results
- Saving the processed dataset into a new Excel file.

## Skills Developed
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Outlier Detection (IQR)
- One-Hot Encoding
- Correlation Analysis
- Data Validation

## Project Structure

```text
Data-Science-Project/
│
├── projet1.py
├── Dataset_notCleaned.xlsx
├── Dataset_cleaned.xlsx
└── README.md
```

## How to Run the Project

1. Clone this repository.
2. Install the required libraries:

```bash
pip install pandas numpy openpyxl pandera
```

3. Open `projet1.py` in your Python environment.
4. Update the dataset file path if necessary.
5. Run the Python script.

## Author
**Hadil Hadj Khalifa**

[GitHub Profile](https://github.com/HadilHadjKhalifa)
