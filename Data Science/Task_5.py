import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Retail_Sales_Data.csv')
data['Total_Sale_Value'] = data['Price'] * data['Quantity_Sold']
data['Date'] = pd.to_datetime(data['Date'], errors='coerce') #date time format

data['YearMonth'] = data['Date'].dt.to_period('M')
monthly_sales = data.groupby('YearMonth')['Total_Sale_Value'].sum() #aggreate month and total sales

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o', color='b')

plt.title('Total Sales by Month', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Sales Value', fontsize=14)
plt.xticks(rotation=45)  
plt.grid()

plt.tight_layout()
plt.show()

#bar chart
category_sales = data.groupby('Product_Category')['Total_Sale_Value'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Sales Comparison Across Product Categories', fontsize=16)
plt.xlabel('Product Category', fontsize=14)
plt.ylabel('Total Sales Value', fontsize=14)
plt.xticks(rotation=45)  
plt.grid(axis='y')  
plt.tight_layout()  
plt.show()

#scatter plot
top_products = data.groupby('Product_Category').agg({'Quantity_Sold': 'sum', 'Price': 'mean'}).nlargest(5, 'Quantity_Sold')

plt.figure(figsize=(12, 6))
plt.scatter(top_products['Price'], top_products['Quantity_Sold'], color='orange')
plt.title('Price vs Quantity Sold for Top 5 Selling Products', fontsize=16)
plt.xlabel('Price', fontsize=14)
plt.ylabel('Quantity Sold', fontsize=14)
plt.grid()
plt.tight_layout()
plt.show()