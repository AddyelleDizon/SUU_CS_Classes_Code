USE northwind;

#DESCRIBE Shippers;
#DESCRIBE Orders;
#DESCRIBE Customers;
#DESCRIBE Products;
#DESCRIBE Suppliers;

SELECT Shippers.shipper_name, COUNT(Orders.OrderID) AS NumberOfOrders
FROM Shippers
JOIN Orders ON Shippers.shipperID = Orders.shipperID
GROUP BY Shippers.shipper_name;

SELECT country, COUNT(customerID) AS NumberOfCustomers
FROM Customers
GROUP BY country
HAVING COUNT(customerID) > 5
ORDER BY NumberOfCustomers DESC;

SELECT AVG(price) AS AveragePrice FROM Products;

SELECT product_name, price
FROM Products
WHERE price > (SELECT AVG(price) FROM Products)
ORDER BY price DESC;

SELECT DISTINCT Suppliers.supplier_name
FROM Suppliers
WHERE EXISTS (
    SELECT 1 FROM Products
    WHERE Products.supplierID = Suppliers.supplierID
    AND Products.price < 20
);