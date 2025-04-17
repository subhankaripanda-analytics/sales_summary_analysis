import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('sales_data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create sales table
cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                  (product TEXT, quantity INTEGER, price REAL)''')

# Insert sample data
cursor.execute("INSERT INTO sales VALUES ('Laptop', 5, 800.0)")
cursor.execute("INSERT INTO sales VALUES ('Phone', 10, 400.0)")
cursor.execute("INSERT INTO sales VALUES ('Tablet', 7, 300.0)")

# Commit changes and close connection
conn.commit()
conn.close()
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('sales_data.db')

# Run SQL query
query = "SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue FROM sales GROUP BY product"
df = pd.read_sql(query, conn)

# Close the connection
conn.close()
print("Sales Summary:")
print(df)
# Plot bar chart
df.plot(kind='bar', x='product', y='revenue')
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.show()
# Save chart
plt.savefig('sales_chart.png')
