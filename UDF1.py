import sqlite3
import pandas as pd

square = lambda n : (n-1)*2

with sqlite3.connect("Northwind.db") as conn:
    conn.create_function("square",1,square)
    cursor = conn.cursor()
    cursor.execute('SELECT *, square(Price) FROM Products')
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)

print(results_df)