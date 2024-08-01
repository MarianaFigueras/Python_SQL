import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Northwind.db")

#Top 10 productos más rentables
query = '''
    SELECT ProductName, SUM(Price*Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductId = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''
top_products = pd.read_sql_query(query,conn)
print(top_products)

top_products.plot(x= "ProductName", y= "Revenue", kind= "bar", figsize= (10,5), legend= False)

plt.title ("10 productos mas rentables")
plt.xlabel ("Productos")
plt.ylabel ("Revenue")
plt.xticks (rotation =25)
plt.show()

#Empleados más efectivos
query2 = '''
    SELECT FirstName || " " || LastName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    LIMIT 10
'''
top_employees= pd.read_sql_query(query2, conn)
print(top_employees)

top_employees.plot(x= "Employee", y= "Total", kind= "bar", figsize=(10,5), legend= False)

plt.title ("10 empleados mas efectivos")
plt.xlabel ("Empleados")
plt.ylabel ("Total de ventas")
plt.xticks (rotation =25)
plt.show()

#Empleados menos eficientes
query3 = '''
    SELECT FirstName || " " || LastName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total ASC
    LIMIT 3
'''
not_top_employees= pd.read_sql_query(query3, conn)
print(not_top_employees)

not_top_employees.plot(x= "Employee", y= "Total", kind= "bar", figsize=(10,5), legend= False)

plt.title ("3 empleados menos eficientes")
plt.xlabel ("Empleados")
plt.ylabel ("Total de ventas")
plt.xticks (rotation =25)
plt.show()

#Empleados que más recaudaron
query4 = '''
    SELECT e.FirstName || ' ' || e.LastName as Employee,
    SUM(od.Quantity * p.Price) as TotalRevenue
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Employees e ON o.EmployeeID = e.EmployeeID
    GROUP BY e.EmployeeID, e.FirstName, e.LastName
    ORDER BY TotalRevenue DESC
    LIMIT 3
'''
rev_top_employees= pd.read_sql_query(query4, conn)
print(rev_top_employees)

rev_top_employees.plot(x= "Employee", y= "TotalRevenue", kind= "bar", figsize=(10,5), legend= False)

plt.title ("Empleados que mas recaudaron")
plt.xlabel ("Empleados")
plt.ylabel ("Total de ventas")
plt.xticks (rotation =25)
plt.show()

