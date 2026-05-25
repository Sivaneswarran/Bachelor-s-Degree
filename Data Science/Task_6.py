import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Retail_Sales_Data.csv')


df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Total_Sales'] = df['Price'] * df['Quantity_Sold']


monthly_sales = df.groupby('Month')['Total_Sales'].sum().reset_index()


X = monthly_sales[['Month']]
y = monthly_sales['Total_Sales']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))


plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Sales Prediction: Actual vs Predicted')
plt.legend()
plt.grid(True)
plt.show()

# Print performance metrics
print(f'R-squared Score: {r2:.4f}')
print(f'Root Mean Square Error: {rmse:.2f}')

# Future predictions
future_months = np.array(range(13, 19)).reshape(-1, 1)  # Next 6 months
future_predictions = model.predict(future_months)

# Display future predictions
for month, prediction in zip(future_months.flatten(), future_predictions):
    print(f'Predicted sales for month {month}: {prediction:.2f}')