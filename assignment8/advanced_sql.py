
import sqlite3

def run_query(description, query, params=None):
    print(f"\n{description}")
    cursor.execute(query, params or ())
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()



# Task 1: Total price of first 5 orders
task1_query = """
SELECT 
    o.order_id,
    SUM(p.price * li.quantity) AS total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5
"""
# run_query("Task 1: Total price of first 5 orders", task1_query)




# Task 2: Average price of orders per customer using a subquery
task2_query = """
SELECT 
    c.customer_name, 
    AVG(sub.total_price) AS average_total_price
FROM customers c
LEFT JOIN (
    SELECT 
        o.customer_id AS customer_id_b,
        SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
) sub ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id
"""
# run_query("Task 2: Average order price per customer", task2_query)



# Task 3: Insert transaction for Perez and Sons

# Step 1: Get customer_id, employee_id, 5 cheapest product_ids
cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
customer_id = cursor.fetchone()[0]

cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
employee_id = cursor.fetchone()[0]

cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
product_ids = [row[0] for row in cursor.fetchall()]

# Step 2: Create order and line_items in a transaction
conn.execute("BEGIN")
cursor.execute("""
    INSERT INTO orders (customer_id, employee_id)
    VALUES (?, ?)
    RETURNING order_id
""", (customer_id, employee_id))
order_id = cursor.fetchone()[0]

for pid in product_ids:
    cursor.execute("""
        INSERT INTO line_items (order_id, product_id, quantity)
        VALUES (?, ?, 10)
    """, (order_id, pid))

conn.commit()

# Step 3: Print out the new line_items for this order
task3_query = """
SELECT 
    li.line_item_id,
    li.quantity,
    p.product_name AS product_name
FROM line_items li
JOIN products p ON li.product_id = p.product_id
WHERE li.order_id = ?
"""
# run_query("Task 3: New order's line items", task3_query, (order_id,))


# Task 4: Employees with more than 5 orders
task4_query = """
SELECT 
    e.employee_id,
    e.first_name,
    e.last_name,
    COUNT(o.order_id) AS order_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) > 5
"""
run_query("Task 4: Employees with > 5 orders", task4_query)

# Close connection
conn.close()
