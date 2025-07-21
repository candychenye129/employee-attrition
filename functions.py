# Import packages
import pandas as pd
from scipy.stats import pearsonr

# Create data frames for each correlation comparison 
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