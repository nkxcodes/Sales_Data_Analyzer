import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data/sales.csv')

    print()
    print('Sales DataFrame: ')
    print()
    print(df)

    number_of_rows = df.shape[0]
    number_of_columns = df.shape[1]
    column_names = df.columns
    data_types = df.dtypes

    print()
    print(f'Number of rows: {number_of_rows}')

    print()
    print(f'Number of columns: {number_of_columns}')

    print()
    print(f'Column names: {column_names}')

    print()
    print('Data types: ')
    print(data_types)

    df['Sales'] = df['Quantity'] * df['Unit_Price']

    print()
    print('========== OVERALL ANALYSIS ==========')
    total_number_of_orders = df['Order_ID'].count()
    total_quantity_of_products_sold = df['Quantity'].sum()
    average_order_value = df['Unit_Price'].mean()
    average_quantity_per_order = df['Quantity'].mean()

    print()
    print(f'Total number of orders: {total_number_of_orders}')

    print()
    print(f'Total quantity of products sold: {total_quantity_of_products_sold}')

    print()
    print(f'Total sales: {total_quantity_of_products_sold}')

    print()
    print(f'Average order value: {average_order_value}')

    print()
    print(f'Average quantity per order: {average_quantity_per_order}')


if __name__ == "__main__":
    main()