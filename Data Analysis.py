# Import packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


# Load the cleaned dataset from the uploaded Excel file
file_path = "Cleaned_Employee_Data.xlsx"
df = pd.read_excel(file_path, sheet_name="Cleaned Data")

# Show the first few rows of the dataset to confirm successful load
print(df.head())


### ---------------Functions-------------------
## Create data frames for each correlation comparison 
def get_correlation_table(df, target, predictors, significance_level=0.05):
    results = []

    for col in predictors:
        if col == target:
            continue
        try:
            r, p = pearsonr(df[target], df[col])
            results.append({
                "Variable": col,
                "Correlation (r)": round(r, 2),
                "P-value": round(p, 5),
                "Significant (p < 0.05)": "Yes" if p < significance_level else "No"
            })
        except Exception as e:
            results.append({
                "Variable": col,
                "Correlation (r)": "ERROR",
                "P-value": str(e),
                "Significant (p < 0.05)": "No"
            })

    return pd.DataFrame(results)

### ------------Create Tables---------------
# Correlation tables
attr_demographics = [
    "Attrition", 
    "Age", 
    "Total Working Years", 
    "Education"
]

attr_work_style = [
    "Over Time", 
    "Work Life Balance"
]

attr_compensation = [
    "Monthly Income", 
    "Percent Salary Hike", 
    "Stock Option Level", 
    "Years Since Last Promotion"
]

attr_satisfaction = [
    "Environment Satisfaction", 
    "Job Satisfaction", 
    "Relationship Satisfaction", 
    "Total Satisfaction Score"
]

# Run the function
attr_demo_corr = get_correlation_table(df, target="Attrition", predictors=attr_demographics)
attr_style_corr = get_correlation_table(df, target="Attrition", predictors=attr_work_style)
attr_comp_corr = get_correlation_table(df, target="Attrition", predictors=attr_compensation)
attr_sat_corr = get_correlation_table(df, target="Attrition", predictors=attr_satisfaction)

with pd.ExcelWriter("correlation_results.xlsx", 
  mode="w", 
  engine="openpyxl") as writer:
    attr_demo_corr.to_excel(writer, sheet_name="Attr_Demo")
    attr_style_corr.to_excel(writer, sheet_name="Attr_Work_Style")
    attr_comp_corr.to_excel(writer, sheet_name="Attr_Comp")
    attr_sat_corr.to_excel(writer, sheet_name="Attr_Sat")
