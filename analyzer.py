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
    df['Sales'] = df['Quantity'] * df['Unit_Price']
    total_sales = df['Sales'].sum()
    average_order_value = df['Sales'].mean().round(2)
    average_quantity_per_order = df['Quantity'].mean().round(2)

    print()
    print(f'Total number of orders: {total_number_of_orders}')

    print()
    print(f'Total quantity of products sold: {total_quantity_of_products_sold}')

    print()
    print(f'Total sales: {total_sales}')

    print()
    print(f'Average order value: {average_order_value}')

    print()
    print(f'Average quantity per order: {average_quantity_per_order}')

    print()
    print('========== PRODUCTS ANALYSIS ==========')

    total_quantity_sold_for_each_product = df.groupby('Product')['Quantity'].sum()
    df['Sales'] = df['Quantity'] * df['Unit_Price']
    total_sales_for_each_product = df.groupby('Product')['Sales'].sum()
    best_selling_product_by_quantity = total_quantity_sold_for_each_product.idxmax()
    best_selling_product_by_revenue = total_sales_for_each_product.idxmax()
    lowest_selling_product = total_quantity_sold_for_each_product.idxmin()

    print()
    print('Total quantity sold for each product: ')
    print()
    print(total_quantity_sold_for_each_product)

    print()
    print('Total sales for each product: ')
    print()
    print(total_sales_for_each_product)

    print()
    print(f'Best selling product by quantity: {best_selling_product_by_quantity}')

    print()
    print(f'Best selling product by revenue: {best_selling_product_by_revenue}')

    print()
    print(f'Lowest selling product: {lowest_selling_product}')

    print()
    print('========== CATEGORIES ANALYSIS ==========')

    number_of_orders_per_category =  df.groupby('Category')['Quantity'].sum()
    total_sales_by_category = df.groupby('Category')['Sales'].sum()
    quantity_sold_by_category = df.groupby('Category')['Quantity'].sum()
    category_with_highest_sales = total_sales_by_category.idxmax()
    category_with_lowest_sales = total_sales_by_category.idxmin()

    print()
    print('Number of orders per category: ')
    print()
    print(number_of_orders_per_category)

    print()
    print('Total sales by category: ')
    print()
    print(total_sales_by_category)

    print()
    print('Quantity sold by category: ')
    print()
    print(quantity_sold_by_category)

    print()
    print(f'Category with highest sales: {category_with_highest_sales}')

    print()
    print(f'Category with lowest sales: {category_with_lowest_sales}')

    print()
    print('========== TIME-BASED ANALYSIS ==========')

    df['Date'] = pd.to_datetime(df['Date'])
    sales_on_each_date = df.groupby('Date')['Sales'].sum()
    highest_sales_date = sales_on_each_date.idxmax()
    lowest_sales_date = sales_on_each_date.idxmin()
    average_daily_sales = sales_on_each_date.mean().round(2)

    print()
    print('Sales on each date: ')
    print()
    print(sales_on_each_date)

    print()
    print(f'Highest sales date: {highest_sales_date}')

    print()
    print(f'Lowest sales date: {lowest_sales_date}')

    print()
    print(f'Average daily sales: {average_daily_sales}')

    print()
    print('========== PAYMENT ANALYSIS ==========')

    number_of_transactions_by_payment_method = df.groupby('Payment_Method')['Order_ID'].count()
    sales_by_payment_method = df.groupby('Payment_Method')['Sales'].sum()
    most_commonly_used_payment_method = number_of_transactions_by_payment_method.idxmax()

    print()
    print('Number of transactions by payment method: ')
    print()
    print(number_of_transactions_by_payment_method)

    print()
    print('Sales by payment method: ')
    print()
    print(sales_by_payment_method)

    print()
    print(f'Most commonly used payment method: {most_commonly_used_payment_method}')

    print()
    print('========== SORTING ==========')

    top_products_by_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
    top_5_products = top_products_by_sales.head()

    print()
    print('Top products by sales: ')
    print()
    print(top_products_by_sales)

    print()
    print('Top 5 products: ')
    print()
    print(top_5_products)

    print()
    print('========== VISUALIZATIONS ==========')

    plt.subplot(2, 2, 1)
    x = total_sales_by_category.index
    y = total_sales_by_category.values

    plt.bar(x, y, color='steelblue')
    plt.title('Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Sales')

    plt.subplot(2, 2, 2)
    x2 = sales_on_each_date.index
    y2 = sales_on_each_date.values

    plt.plot(x2, y2, color='steelblue')

    plt.subplot(2, 2, 3)
    x3 = top_5_products.index
    y3 = top_5_products.values

    plt.bar(x3, y3, color='steelblue')

    plt.subplot(2, 2, 4)
    x4 = number_of_transactions_by_payment_method.index
    y4 = number_of_transactions_by_payment_method.values

    plt.bar(x4, y4, color='steelblue')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()