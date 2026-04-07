# Group sales data by region and product: compute mean sales and total quantity, then filter groups where mean sales > 500.�
import numpy as np
import pandas as pd


data = {
    'Region': ['East', 'West', 'East', 'West', 'North', 'East'],
    'Product': ['A', 'B', 'A', 'A', 'B', 'B'],
    'Sales': [100, 200, 150, 300,550, 180],
    'Year': [2022, 2022, 2023, 2023, 2022, 2023]
}

df = pd.DataFrame(data)
print(df)

# result = df.groupby(['Region', 'Product'])['Sales'].sum().reset_index()

# print(result)
result=df['Sales'].mean()
print(result)

answer=df['Sales']>500
print(answer)