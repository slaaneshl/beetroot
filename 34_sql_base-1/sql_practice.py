from sql_test import create_connection, execute_query, select_query


connection = create_connection('northwind.db')

# test = """
# SELECT * FROM Orders Where ShipCountry in ('France', 'German', 'Spain')
# """
#
# pprint(select_query(connection, test))

order_sort = """
SELECT * FROM Orders order by OrderDate DESC, ShippedDate;
"""

min_product_price = """
SELECT min(UnitPrice) 
FROM Products where Products.UnitsInStock > 30;
"""

mid_time_usa = """
SELECT avg(JULIANDAY(ShippedDate) - JULIANDAY(Orders.OrderDate)) 
FROM Orders where ShipCountry = 'USA';
"""
whole_price_products = """
SELECT round(sum(UnitPrice * UnitsInStock), 2) FROM Products;
"""
whole_orders_from_u = """
SELECT * FROM Orders WHERE ShipCountry LIKE '%U';
"""
orders_from_n = """
SELECT * FROM Orders WHERE ShipCountry LIKE 'N%' ORDER BY Freight DESC LIMIT 2;
"""

for item in select_query(connection, orders_from_n):
    print(item)

