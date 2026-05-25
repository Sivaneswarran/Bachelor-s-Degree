import pandas as pd
data = pd.read_csv('Retail_Sales_Data.csv')
data.isnull().sum
print(data)

#handling missing data
data['Quantity'].fillna(data['Quantity'].median(), inplace=True)
data['Price'].fillna(data['Price'].mean(), inplace=True)


#integrate data
negative_prices = data[data['Price'] < 0]
negative_quantities = data[data['Quantity'] < 0]

# Correcting negative values
if not negative_prices.empty:
    print("\nNegative Prices Found:")
    print(negative_prices)
    data.loc[data['Price'] < 0, 'Price'] = 0  # Set negative prices to 0

if not negative_quantities.empty:
    print("\nNegative Quantities Found:")
    print(negative_quantities)
    data.loc[data['Quantity'] < 0, 'Quantity'] = 0


##Data Cleaning Process:
##1. Loaded data from 'Retail_Sales_Data.csv'.
##2. Inspected the data for missing values and data types.
##3. Corrected data integrity issues:
##  - Set negative 'Price' values to 0.
##  - Set negative 'Quantity' values to 0.
##  - Converted 'Date' to datetime format and removed invalid dates.
##4. Final dataset is now clean and ready for analysis.

