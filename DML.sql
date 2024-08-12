-- Insert Queries:

-- add a new Manufacturer when there are no null inputs
INSERT INTO INSERT INTO Manufacturers (manufacturerName, manufacturerStreet, manufacturerStreet2, manufacturerCity, manufacturerState, manufacturerZip, manufacturerEmail, manufacturerPhone)
VALUES (name, street, street2, city, state, zip, email, phone);
-- add a new Manufacturer when street2 is null
INSERT INTO Manufacturers (manufacturerName, manufacturerStreet, manufacturerCity, manufacturerState, manufacturerZip, manufacturerEmail, manufacturerPhone)
VALUES (name, street, city, state, zip, email, phone);

-- add a new Synthesizer when there are no null inputs
INSERT INTO Synthesizers (manufacturerID, synthesizerName, synthesizerCost, synthesizerPrice, signalType, keyboard)
VALUES (manufacturer, name, cost, price, signal, keyboard); 
-- add a new Synthesizer when both cost and price are null
INSERT INTO Synthesizers (manufacturerID, synthesizerName, signalType, keyboard)
VALUES (manufacturer, name, signal, keyboard);
-- add a new Synthesizer when cost is null
INSERT INTO Synthesizers (manufacturerID, synthesizerName, synthesizerPrice, signalType, keyboard)
VALUES (manufacturer, name, price, signal, keyboard);
-- add a new Synthesizer when price is null
INSERT INTO Synthesizers (manufacturerID, synthesizerName, synthesizerCost, signalType, keyboard)
VALUES (manufacturer, name, cost, signal, keyboard);

-- add a new Customer when there are no null inputs
INSERT INTO Customers (customerFirstName, customerLastName, customerStreet, customerStreet2, customerCity, customerState, customerZip, customerEmail, customerPhone)
VALUES (fname, lname, street, city, street2, state, zip, email, phone);
-- add a new Customer when street2 is null
INSERT INTO Customers (customerFirstName, customerLastName, customerStreet, customerCity, customerState, customerZip, customerEmail, customerPhone)
VALUES (fname, lname, street, city, state, zip, email, phone);

-- add a new Order
INSERT INTO Orders (customerID, orderDate, orderPrice) 
VALUES (customerID, orderDate, synthesizerLinePrice);

-- add a new Purchase when orderID is null (no associated order)
INSERT INTO Purchases (manufacturerID, purchaseDate, purchaseCost) 
VALUES (manufacturerID, purchaseDate, synthesizerLinePrice);
-- add a new Purchase when orderID is provided
INSERT INTO Purchases (orderID, manufacturerID, purchaseDate, purchaseCost) 
VALUES (orderID, manufacturerID, purchaseDate, synthesizerLinePrice);

-- add a new OrderSynthesizer
-- first get price of selected synthesizer
SELECT synthesizerPrice,1 
FROM Synthesizers 
WHERE synthesizerID = int(synthesizerID);
-- associate a Synthesizer with an Order Item (M-to-N relationship addition)
INSERT INTO OrderSynthesizer (orderID, synthesizerID, orderItemQuantity, orderItemUnitPrice, orderItemLinePrice)
VALUES (orderID, synthesizerID, quantity, synthesizerUnitPrice, synthesizerLinePrice);
-- update associated orders with the addition of ordesynthesizer row
UPDATE Orders
SET orderPrice = orderPrice + synthesizerLinePrice
WHERE orderID = orderID;

-- add a new PurchaseSynthesizer
-- first get price of selected synthesizer
SELECT synthesizerCost 
FROM Synthesizers 
WHERE synthesizerID = synthesizerID;
-- associate a Synthesizer with a Purchase Item (M-to-N relationship addition)
INSERT INTO PurchaseSynthesizer (purchaseID, synthesizerID, purchaseItemQuantity, purchaseItemUnitCost, purchaseItemLineCost) 
VALUES (purchaseID, synthesizerID, quantity, unit_price, line_price);
-- update associated purchase with the addition of PurchaseSynthesizer row
UPDATE Purchases
SET purchaseCost = purchaseCost + line_price
WHERE purchaseID = purchaseID;


-- Select Queries:

-- get all Synthesizer IDs and Synthesizer Names that are available for purchase
SELECT synthesizerID AS ID, manufacturerID AS ManufacturerID, synthesizerName AS Name, 
synthesizerCost AS Cost, synthesizerPrice AS Price, signalType, keyboard as Keyboard 
FROM Synthesizers;

-- get Synthesizer Price for a single synthesizer
SELECT synthesizerPrice,1 
FROM Synthesizers 
WHERE synthesizerID = int(synthesizerID);

-- get orderID or puchaseID of last added order or purchase
SELECT LAST_INSERT_ID();

-- get all Manufacturer IDs and Manufacturer Names that are available to make purchases from 
SELECT manufacturerID AS ID, manufacturerName AS Name, manufacturerStreet AS Street, 
manufacturerStreet2 AS Street2, manufacturerCity AS City, manufacturerState AS State, 
manufacturerZip AS Zip, manufacturerEmail AS Email, manufacturerPhone AS Phone 
FROM Manufacturers;

-- get all Customer IDs and Customer Names
SELECT customerID AS ID, customerFirstName AS FirstName, customerLastName AS LastName, 
customerStreet AS Street, customerStreet2 AS Street2, customerCity AS City, customerState AS State, 
customerZip AS Zip, customerEmail AS Email, customerPhone AS Phone 
FROM Customers;

-- get all Orders
SELECT orderID AS ID, customerID AS CustomerID, orderDate AS Date, orderPrice AS Price 
FROM Orders;

-- get all Purchases
SELECT purchaseID AS ID, orderID AS OrderID, manufacturerID AS ManufacturerID, 
purchaseDate AS Date, purchaseCost AS Cost 
FROM Purchases;

-- get all OrderSynthesizer items
SELECT orderSynthesizerID AS ID, orderID AS OrderID, synthesizerID AS SynthesizerID, 
orderItemQuantity AS ItemQuantity, orderItemUnitPrice AS UnitPrice, orderItemLinePrice AS LinePrice
FROM OrderSynthesizer;

-- get all PurchaseSynthesizer items
SELECT purchaseSynthesizerID AS ID, purchaseID AS PurchaseID, synthesizerID as SynthesizerID, 
purchaseItemQuantity AS ItemQuantity, purchaseItemUnitCost AS UnitCost, purchaseItemLineCost AS LineCost 
FROM PurchaseSynthesizer;


-- selects for user input fields (dynamic drop-down options for fks)
-- get manufacturerID and manufacturerName from Manufacturers, ordered by manufacturerName
SELECT manufacturerID, manufacturerName 
FROM Manufacturers 
ORDER BY manufacturerName;

-- get synthesizerID and synthesizerName from Synthesizers, ordered by synthesizerName
SELECT synthesizerID, synthesizerName 
FROM Synthesizers 
ORDER BY synthesizerName;

-- get customerFirstName and customerLastName, customerID from Customers, ordered by customerFirstName and customerLastName
SELECT customerFirstName, customerLastName, customerID 
FROM Customers 
ORDER BY customerFirstName, customerLastName;

-- get orderSynthesizerID and orderID from OrderSynthesizer, ordered by orderSynthesizerID
SELECT orderSynthesizerID, orderID 
FROM OrderSynthesizer 
ORDER BY orderSynthesizerID;

-- get orderID from Orders
SELECT orderID 
FROM Orders;

-- get purchaseID from purchases
SELECT purchaseID 
FROM Purchases;


-- Updates:
-- Update OrderSynthesizer row
UPDATE OrderSynthesizer 
SET synthesizerID = synthesizerID, orderItemQuantity = quantity, orderItemUnitPrice = unit_price, orderItemLinePrice = line_price 
WHERE orderSynthesizerID = orderSynthesizerID;
-- then update associated Order by first getting previous OrderSynthesizer price
SELECT orderItemLinePrice, 1 
FROM OrderSynthesizer 
WHERE orderSynthesizerID = int(orderSynthesizerID);
-- get previous price of associated order
SELECT orderPrice, 1 
FROM Orders 
WHERE orderID = int(orderID);
-- update order with new price
UPDATE Orders 
SET orderPrice = newOrderPrice 
WHERE orderID = orderID;

-- Deletes
-- delete a single OrderSynthesizer line item
DELETE FROM OrderSynthesizer 
WHERE orderSynthesizerID = orderSynthesizerID;
-- update associated order to remove OrderSynthesizer row from total order price
UPDATE Orders
SET orderPrice = orderPrice - orderItemLinePrice
WHERE orderID = orderID;
