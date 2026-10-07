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

if __name__ == "__main__":
    main()