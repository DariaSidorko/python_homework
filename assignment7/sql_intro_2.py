

# Task 5: Read Data into a DataFrame

import pandas as pd
import sqlite3

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        query = """
        SELECT 
            line_items.line_item_id, 
            line_items.quantity, 
            products.product_id, 
            products.product_name, 
            products.price
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id
        """
        df = pd.read_sql_query(query, conn)

    df['total'] = df['quantity'] * df['price']
    print("\nFirst 5 rows with totals:")
    print(df.head())

    summary = df.groupby('product_id').agg({
        'line_item_id': 'count',
        'total': 'sum',
        'product_name': 'first'
    }).reset_index()

    summary = summary.sort_values(by='product_name')
    summary.to_csv("order_summary.csv", index=False)

    print("\nOrder summary:")
    print(summary.head())

except Exception as e:
    print("Error:", e)