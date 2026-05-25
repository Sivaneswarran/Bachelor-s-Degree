import pandas as pd
data = pd.read_csv('Retail_Sales_Data.csv')

data['Total_Sale'] = data['Price'] * data['Quantity_Sold'] #created new column for total sales
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data['YearMonth'] = data['Date'].dt.to_period('M')

aggregated_sales = data.groupby(['YearMonth', 'Product_Category'])['Total_Sale'].sum().reset_index()
print("Aggregated Sales Data by Month and Product Category:")
print(aggregated_sales)




    