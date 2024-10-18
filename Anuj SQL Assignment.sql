/* Display all columns of SalesLT.Product table*/

SELECT * FROM SalesLT.Customer;

/*Create a list of all customer contact names that includes the title, first name, middle name (if any), last name, and suffix (if any) of all customers*/
SELECT Title, FirstName, MiddleName, LastName, Suffix FROM SalesLT.Customer;

/*Each customer has an assigned salesperson. You must write a query to create a call sheet that lists*/
/*The salesperson*/
/*A column named CustomerName that displays how the customer contact should be greeted (for example, Mr Smith)*/
/*The customer’s phone number*/

SELECT SalesPerson,Title + ', ' + FirstName AS CustomerName,Phone FROM SalesLT.Customer

/*Retrieve a list of cities*/
/*Write a Transact-SQL query that queries the SalesLT.Address table and retrieves the values for City and StateProvince, removing duplicates and sorted in ascending order of city.*/

SELECT DISTINCT City, StateProvince  FROM SalesLT.Address ORDER BY City ASC,StateProvince ASC;

/* Retrieve the heaviest products*/
/*Transportation costs are increasing and you need to identify the heaviest products. Retrieve the names of the top ten percent of products by weight*/

SELECT * FROM SalesLT.Product;
SELECT TOP 10 Weight,Name FROM SalesLT.Product ORDER BY Weight DESC;

/*The Production Manager at Adventure Works would like you to create some reports listing details of the products that you sell*/
/*1.Retrieve product details for product model 1*/
/*Initially, you need to find the names, colors, and sizes of the products with a product model ID 1*/

SELECT Name, Color, Size FROM SalesLT.Product WHERE ProductModelID = 1;

/*Filter products by color and size*/
/*Retrieve the product number and name of the products that have a color of black, red, or white and a size of S or M*/

SELECT ProductNumber, Name FROM SalesLT.Product WHERE Color IN ('Black', 'Red', 'White')  AND Size IN ('S', 'M');

/*Filter products by product number*/
/*Retrieve the product number, name, and list price of products whose product number begins BK*/

SELECT ProductNumber, Name, ListPrice FROM SalesLT.Product WHERE ProductNumber LIKE 'BK%';

/*Retrieve specific products by product number*/
/*o	Modify your previous query to retrieve the product number, name, and list price of products
whose product number begins BK- followed by any character other than R, and ends with a - followed by any two numerals*/

SELECT ProductNumber, Name, ListPrice FROM SalesLT.Product WHERE ProductNumber LIKE 'BK-[^R]%-__';

/*Notes for above query :- BK- specifies that the product number must start with "BK-".
        [^R] ensures that the next character is not "R".
        % represents any sequence of characters after that.
        - indicates that the product number must contain a dash before the final two numerals.
        __ (two underscores) specifies exactly two characters (digits in this case) at the end of the product number*/

/*Retrieve customer orders*/
/*As an initial step towards generating the invoice report, write a query that returns the company name from the SalesLT.Customer table, 
and the sales order ID and total due from the SalesLT.SalesOrderHeader table*/

SELECT CompanyName FROM SalesLT.Customer;
SELECT SalesOrderID, TotalDue FROM SalesLT.SalesOrderHeader

/*Combing both with JOIN*/
/*Note:-This query retrieves the CompanyName from the SalesLT.Customer table
and the SalesOrderID and TotalDue from the SalesLT.SalesOrderHeader table, 
linking them through the CustomerID to provide a report of customers and their sales orders
so: This is an alias for the table SalesLT.SalesOrderHeader. Aliases are created using the AS keyword
or simply by providing a name right after the table name in the FROM clause.
Dot Notation: When you see so.SalesOrderID or so.TotalDue, 
it means you are referencing the SalesOrderID and TotalDue columns from the table that has been aliased as so.*/

SELECT a.CompanyName,so.SalesOrderID,so.TotalDue FROM SalesLT.Customer AS a
JOIN SalesLT.SalesOrderHeader AS so ON a.CustomerID = so.CustomerID;

/*Retrieve customer orders with addresses*/
/*o	Extend your customer orders query to include the Main Office address for each customer, 
including the full street address, city, state or province, postal code, and country or region*/

SELECT * FROM SalesLT.Address;
SELECT *FROM SalesLT.CustomerAddress;
/*Combing both with JOIN*/
SELECT a.AddressType,a.CustomerID,so.AddressLine1,so.City,so.StateProvince,so.Postalcode,so.CountryRegion FROM SalesLT.CustomerAddress AS a
JOIN SalesLT.Address AS so ON a.AddressID = so.AddressID
WHERE a.AddressType = 'Main Office';

/*Retrieve customer data*/
/*Retrieve a list of all customers and their orders*/
/*The sales manager wants a list of all customer companies and their contacts (first name and last name), 
showing the sales order ID and total due for each order they have placed. 
Customers who have not placed any orders should be included at the bottom of the list with NULL values for the order ID and total due*/

SELECT CompanyName,FirstName,LastName FROM SalesLT.Customer
SELECT SalesOrderID,TotalDue FROM SalesLT.SalesOrderHeader
/*Combining both*/
SELECT a.CompanyName,a.FirstName,a.LastName,so.SalesOrderID,so.TotalDue FROM SalesLT.Customer AS a
JOIN SalesLT.SalesOrderHeader AS so ON a.CustomerID  = so.CustomerID


/*Retrieve a list of customers with no address*/
/*o	A sales employee has noticed that Adventure Works does not have address information for all customers. You must write a query that returns a list of 
customer IDs, company names, contact names (first name and last name), and phone numbers for customers with no address stored in the database.*/

SELECT CustomerID,CompanyName,FirstName,LastName,Phone FROM SalesLT.Customer
SELECT AddressType,AddressID FROM SalesLT.CustomerAddress
/*Combining both*/
SELECT a.CustomerID,a.CompanyName,a.FirstName,a.LastName,a.Phone,so.AddressID,so.AddressType FROM SalesLT.Customer AS a
JOIN SalesLT.CustomerAddress AS so ON a.CustomerID = so.CustomerID WHERE so.AddressID IS NULL;

/*Retrieve order shipping information*/
/*The operations manager wants reports about order shipping based on data in the SalesLT.SalesOrderHeader table*/
/*Retrieve the order ID and freight cost of each order*/
/*Write a query to return the order ID for each order, together with the the Freight value rounded to two decimal places in a column named FreightCost*/

SELECT[SalesOrderID] ,ROUND(Freight, 2) AS FreightCost FROM SalesLT.SalesOrderHeader;

/*Extend your query to include a column named ShippingMethod that contains the ShipMethod field, formatted in lower case*/

SELECT [SalesOrderID],ROUND(Freight, 2) AS FreightCost,LOWER(ShipMethod) AS ShippingMethod FROM SalesLT.SalesOrderHeader;

/*	Extend your query to include columns named ShipYear, ShipMonth, and ShipDay that contain the year, month, and day of the ShipDate. 
The ShipMonth value should be displayed as the month name (for example, June)*/

SELECT [SalesOrderID], ROUND(Freight, 2) AS FreightCost,LOWER(ShipMethod) AS ShippingMethod,YEAR(ShipDate) AS ShipYear,DATENAME(MONTH, ShipDate) AS ShipMonth,DAY(ShipDate) AS ShipDay FROM SalesLT.SalesOrderHeader;

 /*Retrieve total sales by product*/
 /*Write a query to retrieve a list of the product names from the SalesLT.Product table 
 and the total revenue for each product calculated as the sum of LineTotal from the SalesLT.SalesOrderDetail table,
 with the results sorted in descending order of total revenue*/   
/*Note:- p-Product and sod-sod is an alias for SalesLT.SalesOrderDetail*/

SELECT  p.Name AS ProductName,SUM(sod.LineTotal) AS TotalRevenue    
FROM SalesLT.Product AS p    
JOIN SalesLT.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID GROUP BY p.Name ORDER BY TotalRevenue DESC;
    
/*o	Modify the previous query to include sales totals for products that have a list price of more than 1000*/
SELECT p.Name AS ProductName,SUM(sod.LineTotal) AS TotalRevenue FROM SalesLT.Product AS p
JOIN SalesLT.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID WHERE p.ListPrice > 1000 GROUP BY p.Name ORDER BY TotalRevenue DESC;

/*Modify the previous query to only include only product groups with a total sales value greater than 20,000*/
SELECT p.Name AS ProductName,SUM(sod.LineTotal) AS TotalRevenue FROM SalesLT.Product AS p    
JOIN SalesLT.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID WHERE p.ListPrice > 1000 GROUP BY p.Name HAVING SUM(sod.LineTotal) > 20000 ORDER BY 
    TotalRevenue DESC;
   

