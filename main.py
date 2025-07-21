# Import packages
import pandas as pd
import pingouin as pg
from scipy.stats import pearsonr
import functions as fc
import variables as var

# Import functions


# Load the cleaned dataset from the uploaded Excel file
file_path = "data/Cleaned_Employee_Data.xlsx"
df = pd.read_excel(file_path, sheet_name="Cleaned Data")

# Show the first few rows of the dataset to confirm successful load
print(df.head())

# Reliability Analysis

# Correlational Analysis

attr_demo_corr = fc.get_correlation_table(df, target="Attrition", predictors=var.attr_demographics)
attr_style_corr = fc.get_correlation_table(df, target="Attrition", predictors=var.attr_work_style)
attr_comp_corr = fc.get_correlation_table(df, target="Attrition", predictors=var.attr_compensation)
attr_sat_corr = fc.get_correlation_table(df, target="Attrition", predictors=var.attr_satisfaction)

with pd.ExcelWriter("correlation_results.xlsx", 
  mode="w", 
  engine="openpyxl") as writer:
    attr_demo_corr.to_excel(writer, sheet_name="Attr_Demo")
    attr_style_corr.to_excel(writer, sheet_name="Attr_Work_Style")
    attr_comp_corr.to_excel(writer, sheet_name="Attr_Comp")
    attr_sat_corr.to_excel(writer, sheet_name="Attr_Sat")

# Regression Analysis