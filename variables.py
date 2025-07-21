# import packages 
import pandas as pd

# Load the cleaned dataset from the uploaded Excel file
file_path = "Cleaned_Employee_Data.xlsx"
df = pd.read_excel(file_path, sheet_name="Cleaned Data")

attr_demographics = [
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

