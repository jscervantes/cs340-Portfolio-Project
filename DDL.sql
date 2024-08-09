-- Disable foreign keys
SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;


-- Create or replace Customers (entity) table
CREATE OR REPLACE TABLE Customers (
    customerID int NOT NULL AUTO_INCREMENT unique,
    customerFirstName varchar(100) NOT NULL,
    customerLastName varchar(100) NOT NULL,
    customerStreet varchar(100) NOT NULL,
    customerStreet2 varchar(100),
    customerCity varchar(100) NOT NULL,
    customerState varchar(100) NOT NULL,
    customerZip varchar(10) NOT NULL,
    customerEmail varchar(100) NOT NULL unique,
    customerPhone varchar(10) NOT NULL unique,
    PRIMARY KEY (customerID)
);

-- Insert 5 rows into Customers table
INSERT INTO Customers (customerID, customerFirstName, customerLastName, customerStreet, customerCity, customerState, customerZip, customerEmail, customerPhone)
VALUES (1, 'Naomi', 'Shaw', '596 Edgefield Drive', 'Clarksburg', 'WV', '26301', 'likvidatorcelok@ezsmail.com', '7188904009'),
(2, 'Brendan', 'Frye', '3308 Godfrey Street', 'Portland', 'OR', '97229', 'frimponmachineus@jojoo.online', '6040917948'),
(3, 'Calvin', 'Melton', '103 Mutton Town Road', 'Vancouver', 'WA', '98663', 'someong6n9v@bankinnepal.com', '8651589083'),
(4, 'Lacey', 'Robbins', '3823 Heron Way', 'Portland', 'OR', '97205', '64j0cy5q5@duniakeliling.com', '3051178216'),
(5, 'Dana', 'Greer', '1225 New Street', 'Eugene', 'OR', '97401', 'parapamm@bmuss.com', '7775332610');

-- Create or replace Manufacturers (entity) table
CREATE OR REPLACE TABLE Manufacturers (
    manufacturerID int NOT NULL AUTO_INCREMENT unique,
    manufacturerName varchar(100) NOT NULL unique,
    manufacturerStreet varchar(100) NOT NULL,
    manufacturerStreet2 varchar(100),
    manufacturerCity varchar(100) NOT NULL,
    manufacturerState varchar(100) NOT NULL,
    manufacturerZip varchar(10) NOT NULL,
    manufacturerEmail varchar(100) NOT NULL unique,
    manufacturerPhone varchar(10) NOT NULL unique,
    PRIMARY KEY (manufacturerID)
);

-- Insert 5 rows into Manufacturers table
INSERT INTO Manufacturers (manufacturerID, manufacturerName, manufacturerStreet, manufacturerCity, manufacturerState, manufacturerZip, manufacturerEmail, manufacturerPhone)
VALUES (1, 'Roland', '123 Sesame St', 'Brooklyn', 'New York', '11214', 'hi@roland.com', '7185553848'),
(2, 'Sequential', '343 Nostrand Ave', 'Denver', 'Colorado', '34214', 'hello@sequential.com', '8885553434'),
(3, 'Korg', '195 Vernon Rd', 'Portland', 'Oregon', '18383', 'welcome@korg.com', '9395559282'), 
(4, 'Moog', '17 Mississipi St', 'Bend', 'Oregon', '38458', 'lol@moog.com', '9345552221'),
(5, 'Yamaha', '9039 Wow St', 'Providence', 'Rhode Island', '38933', 'hey@yamaha.com', '5555555555');

-- Create or replace Synthesizers (entity) table
CREATE OR REPLACE TABLE Synthesizers (
    synthesizerID int NOT NULL AUTO_INCREMENT unique,
    manufacturerID int NOT NULL,
    synthesizerName varchar(100) NOT NULL unique,
    synthesizerCost numeric (10,2),
    synthesizerPrice numeric (10,2),
    signalType varchar(100),
    keyboard boolean,
    PRIMARY KEY (synthesizerID),
    FOREIGN KEY (manufacturerID) REFERENCES Manufacturers(manufacturerID) ON DELETE CASCADE
);

-- Insert 5 rows into Synthesizers table
INSERT INTO Synthesizers (synthesizerID, manufacturerID, synthesizerName, synthesizerCost, synthesizerPrice, signalType, keyboard)
VALUES (1, 1, 'Juno60', 2099.99, 2999.99, 'Analog', TRUE),
(2, 2, 'Jupiter8', 13335.99, 22930.99, 'Analog', TRUE),
(3, 3, 'Prophet5', 3999.99, 7899.99, 'Analog', TRUE),
(4, 4, 'WavestateMK2', 499.99, 699.99, 'Digital', FALSE),
(5, 5, 'Grandmother', 799.99, 999.99, 'Analog', TRUE);

-- Create or replace Orders (entity) table
CREATE OR REPLACE TABLE Orders (
    orderID int NOT NULL AUTO_INCREMENT unique,
    customerID int NOT NULL,
    orderDate date NOT NULL,
    orderPrice numeric (10,2),
    PRIMARY KEY (orderID),
    FOREIGN KEY (customerID) REFERENCES Customers(customerID) ON DELETE CASCADE
);

-- Insert 5 rows into Orders table
INSERT INTO Orders (orderID, customerID, orderDate, orderPrice)
VALUES (1, 5, '2024-03-17', 28930.97),
(2, 4, '2024-07-14', 2999.97),
(3, 4, '2023-11-14', 2999.99),
(4, 2, '2023-12-01', 8599.98),
(5, 1, '2024-01-02', 2999.99);

-- Create or replace OrderSynthesizer (intersection) table
CREATE OR REPLACE TABLE OrderSynthesizer (
    orderSynthesizerID int NOT NULL AUTO_INCREMENT unique,
    orderID int NOT NULL,
    synthesizerID int NOT NULL,
    orderItemQuantity int NOT NULL,
    orderItemUnitPrice numeric (10,2),
    orderItemLinePrice numeric (10,2),
    PRIMARY KEY (orderSynthesizerID),
    FOREIGN KEY (orderID) REFERENCES Orders(orderID) ON DELETE CASCADE,
    FOREIGN KEY (synthesizerID) REFERENCES Synthesizers(synthesizerID) ON DELETE CASCADE
);

-- Insert 7 rows into OrderSynthesizer intersection table
INSERT INTO OrderSynthesizer (orderSynthesizerID, orderID, synthesizerID, orderItemQuantity, orderItemUnitPrice, orderItemLinePrice)
VALUES (1, 1, 1, 2, 2999.99, 5999.98),
(2, 1, 2, 1, 22930.99, 22930.99), 
(3, 2, 5, 3, 999.99, 2999.97), 
(4, 3, 1, 1, 2999.99, 2999.99), 
(5, 4, 4, 1, 699.99, 699.99), 
(6, 4, 3, 1, 7899.99, 7899.99), 
(7, 5, 1, 1, 2999.99, 2999.99);

-- Create or replace Purchases (entity) table
CREATE OR REPLACE TABLE Purchases (
    purchaseID int NOT NULL AUTO_INCREMENT unique,
    orderID int,
    manufacturerID int NOT NULL,
    purchaseDate date NOT NULL,
    purchaseCost numeric (10,2),
    PRIMARY KEY (purchaseID),
    FOREIGN KEY (orderID) REFERENCES Orders(orderID) ON DELETE CASCADE,
    FOREIGN KEY (manufacturerID) REFERENCES Manufacturers(manufacturerID) ON DELETE CASCADE
);

-- Insert 5 rows into Purchases table
INSERT INTO Purchases (purchaseID, orderID, manufacturerID, purchaseDate, purchaseCost)
VALUES (1, 1, 1, '2024-03-18', 17535.97),
(2, 2, 4, '2024-07-14', 2399.97),
(3, 3, 1, '2024-11-15', 2099.99),
(4, 4, 3, '2024-12-02', 499.99),
(5, 4, 2, '2024-12-02', 3999.99),
(6, 5, 1, '2024-12-02', 2099.99);

-- Create or replace PurchaseSynthesizer (intersection) table
CREATE OR REPLACE TABLE PurchaseSynthesizer (
    purchaseSynthesizerID int NOT NULL AUTO_INCREMENT unique,
    purchaseID int NOT NULL,
    synthesizerID int NOT NULL,
    purchaseItemQuantity int NOT NULL,
    purchaseItemUnitCost numeric (10,2),
    purchaseItemLineCost numeric (10,2),
    PRIMARY KEY (purchaseSynthesizerID),
    FOREIGN KEY (synthesizerID) REFERENCES Synthesizers(synthesizerID) ON DELETE CASCADE,
    FOREIGN KEY (purchaseID) REFERENCES Purchases(purchaseID) ON DELETE CASCADE
);

-- Insert 7 rows into PurchaseSynthesizer intersection table
INSERT INTO PurchaseSynthesizer (purchaseSynthesizerID, purchaseID, synthesizerID, purchaseItemQuantity, purchaseItemUnitCost, purchaseItemLineCost)
VALUES (1, 1, 1, 2, 2099.99, 4199.98),
(2, 1, 2, 1, 13335.99, 13335.99),
(3, 2, 5, 3, 799.99, 2399.97), 
(4, 3, 1, 1, 2099.99, 6299949),
(5, 4, 4, 1, 499.99, 349988.00),
(6, 4, 3, 1, 3999.99, 31599881.00),
(7, 5, 1, 1, 2099.99, 6299949.00);

-- Enable foreign keys
SET FOREIGN_KEY_CHECKS=1;
COMMIT;
