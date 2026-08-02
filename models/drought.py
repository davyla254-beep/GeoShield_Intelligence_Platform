
import pandas as pd

def load_drought_data(path):
    return pd.read_csv(path)

def top_risk_counties(df, n=10):
    return df.sort_values(
        "Drought_Risk",
        ascending=False
    ).head(n)

def highest_risk(df):
    return df.loc[df["Drought_Risk"].idxmax()]
