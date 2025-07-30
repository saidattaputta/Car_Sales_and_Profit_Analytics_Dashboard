# scripts/process_data.py

import pandas as pd
excel_path = 'CarSalesByModelStart copy.xlsx'
def load_and_clean_data(excel_path):
    """
    Load Excel data and perform basic cleaning.
    """
    data = pd.read_excel(excel_path, sheet_name='CarSales')
    
    # Drop rows with missing values to ensure clean data
    data.dropna(inplace=True)
    
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    
    return data

def feature_engineering(data):
    """
    Add useful derived columns for analysis.
    """
    # Add a YearMonth column for easier time-based aggregation
    data['YearMonth'] = data['Date'].dt.to_period('M')
    
    return data

def aggregate_data(data):
    """
    Produce aggregate summaries from cleaned data.
    """
    # Total quantity sold by car model
    sales_by_model = data.groupby('Model')['Quantity Sold'].sum().sort_values(ascending=False)
    
    # Total profit by dealer
    profit_by_dealer = data.groupby('Dealer ID')['Profit'].sum().sort_values(ascending=False)
    
    return sales_by_model, profit_by_dealer

def main():
    excel_file = '../CarSalesByModelStart-copy.xlsx'  # Adjust as necessary
    data = load_and_clean_data(excel_file)
    data = feature_engineering(data)
    
    sales_by_model, profit_by_dealer = aggregate_data(data)
    
    # Print key summaries
    print(f"Total Profit: ${data['Profit'].sum():,.2f}")
    print(f"Total Quantity Sold: {data['Quantity Sold'].sum():,} units")
    print("\nSales by Model:")
    print(sales_by_model.head())
    print("\nProfit by Dealer:")
    print(profit_by_dealer.head())

if __name__ == '__main__':
    main()
