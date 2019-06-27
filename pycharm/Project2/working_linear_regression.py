import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse


df = pd.read_csv("resources/housing.csv")
df.info()
df.describe()
df_filtered = df[['median_income', 'total_rooms', 'latitude', 'median_house_value']]
lin_reg = LinearRegression()
lin_reg.fit(df_filtered[['median_income', 'total_rooms', 'latitude']], df_filtered[['median_house_value']])
print(lin_reg.coef_)
print(lin_reg.intercept_)
predictions = lin_reg.predict(df_filtered[['median_income', 'total_rooms', 'latitude']])
print(np.sqrt(mse(df_filtered[['median_house_value']],  predictions)))
