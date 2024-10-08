# Citation for the following code:
# Date: 08/12/2024
# Based on:
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template, json, redirect, request
from flask_mysqldb import MySQL
import os
import traceback

app = Flask(__name__)

# database connection
# Template:
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_cervanj2"
app.config["MYSQL_PASSWORD"] = "4397"
app.config["MYSQL_DB"] = "cs340_cervanj2"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"


mysql = MySQL(app)

# Routes
@app.route('/')
def root():
    title = "Ciani Synths"
    return render_template("base.j2", title=title)

@app.route('/synthesizers', methods=['GET', 'POST'])
def synthesizers():
    # POST
    #insert a synthesizer into Synthesizers entity
    if request.method == "POST":
        # Execute if user presses Add Synthesizer button
        if request.form.get("Add_Synthesizer"):
            # grab user form inputs
            manufacturer = request.form["manufacturerID"]
            name = request.form["name"]
            cost = request.form["cost"]
            price = request.form["price"]
            signal = request.form["signal"]
            keyboard = request.form["keyboard"]

            # account for null cost AND price
            if cost == "" and price == "":
                query = "INSERT INTO Synthesizers (manufacturerID, synthesizerName, signalType, keyboard) \
                         VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (manufacturer, name, signal, keyboard))
                mysql.connection.commit()

            # account for null cost
            elif cost == "":
                query = "INSERT INTO Synthesizers (manufacturerID, synthesizerName, synthesizerPrice, signalType, keyboard) \
                         VALUES (%s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (manufacturer, name, price, signal, keyboard))
                mysql.connection.commit()

            # account for null price
            elif price == "":
                query = "INSERT INTO Synthesizers (manufacturerID, synthesizerName, synthesizerCost, signalType, keyboard) \
                         VALUES (%s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (manufacturer, name, cost, signal, keyboard))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "INSERT INTO Synthesizers (manufacturerID, synthesizerName, synthesizerCost, synthesizerPrice, signalType, keyboard) \
                         VALUES (%s, %s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (manufacturer, name, cost, price, signal, keyboard))
                mysql.connection.commit()

            return redirect("/synthesizers")
            

    # Grab Synthesizers data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the synthesizers in Synthesizer table
        query = "SELECT synthesizerID AS ID, manufacturerID AS ManufacturerID, synthesizerName AS Name, synthesizerCost AS Cost, synthesizerPrice AS Price, signalType, keyboard as Keyboard FROM Synthesizers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        
        # Get info from db for manufacturer drop down
        query2 = "SELECT manufacturerID, manufacturerName FROM Manufacturers ORDER BY manufacturerName"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        manufacturerData = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("synthesizers.j2", data=data, manufacturerData = manufacturerData)

    return render_template("synthesizers.j2")

@app.route('/manufacturers', methods=('GET', 'POST'))
def manufacturers():
    # POST 
    #insert a manufacturer into Manufacturers entity
    if request.method == "POST":
        # Execute if user presses Add_Manufacturer button
        if request.form.get("Add_Manufacturer"):
            try:
                # grab user form inputs
                name = request.form["name"]
                street = request.form["street"]
                street2 = request.form["street2"]
                city = request.form["city"]
                state = request.form["state"]
                zip = request.form["zip"]
                email = request.form["email"]
                phone = request.form["phone"]
                   
                try:
                    #account for null street2 input
                    if street2 == "":
                        query = "INSERT INTO Manufacturers (manufacturerName, manufacturerStreet, manufacturerCity, manufacturerState, manufacturerZip, manufacturerEmail, manufacturerPhone) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        cur = mysql.connection.cursor()
                        cur.execute(query, (name, street, city, state, zip, email, phone))
                    #no null inputs
                    else:                                
                        query = "INSERT INTO Manufacturers (manufacturerName, manufacturerStreet, manufacturerStreet2, manufacturerCity, manufacturerState, manufacturerZip, manufacturerEmail, manufacturerPhone) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        cur = mysql.connection.cursor()
                        cur.execute(query, (name, street, street2, city, state, zip, email, phone))
                    mysql.connection.commit()
                    
                except Exception as e:
                    tb = traceback.format_exc()
                    log(tb)  # Log the detailed traceback
                    return str(e), 500   
                  
                return redirect("/manufacturers")
            
            except Exception as e:
                tb = traceback.format_exc()
                log(tb)  # Log the detailed traceback
                return str(e), 500  # Return error message and HTTP 500 status code

    # Grab Manufacturers data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the manufacturers in Manufacturers table
        query = "SELECT manufacturerID AS ID, manufacturerName AS Name, manufacturerStreet AS Street, manufacturerStreet2 AS Street2, manufacturerCity AS City, manufacturerState AS State, manufacturerZip AS Zip, manufacturerEmail AS Email, manufacturerPhone AS Phone FROM Manufacturers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    # render manufacturers page passing our query data and manufacturers template
    return render_template("manufacturers.j2", data = data)

@app.route('/customers', methods=('GET', 'POST'))
def customers():
    # POST 
    #insert a customer into Customers entity
    if request.method == "POST":
        # Execute if user presses Add_Customer button
        if request.form.get("Add_Customer"):
            try:
                #grab user form inputs
                fname = request.form["first-name"]
                lname = request.form["last-name"]
                street = request.form["street"]
                street2 = request.form["street2"]
                city = request.form["city"]
                state = request.form["state"]
                zip = request.form["zip"]
                email = request.form["email"]
                phone = request.form["phone"]
                
                try:
                    #account for null street2 input
                    if street2 == "":
                        query = "INSERT INTO Customers (customerFirstName, customerLastName, customerStreet, customerCity, customerState, customerZip, customerEmail, customerPhone) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        cur = mysql.connection.cursor()
                        cur.execute(query, (fname, lname, street, city, state, zip, email, phone))
                        
                    #no null inputs
                    else:
                        query = "INSERT INTO Customers (customerFirstName, customerLastName, customerStreet, customerStreet2, customerCity, customerState, customerZip, customerEmail, customerPhone) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        cur = mysql.connection.cursor()
                        cur.execute(query, (fname, lname, street, city, street2, state, zip, email, phone))
                    mysql.connection.commit()
                except Exception as e:
                    tb = traceback.format_exc()
                    log(tb)  # Log the detailed traceback
                    return str(e), 500

                return redirect("/customers")

            except Exception as e:
                tb = traceback.format_exc()
                log(tb)  # Log the detailed traceback
                return str(e), 500  # Return error message and HTTP 500 status code

    # Grab Customers data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the customers in Customers table
        query = "SELECT customerID AS ID, customerFirstName AS FirstName, customerLastName AS LastName, customerStreet AS Street, customerStreet2 AS Street2, customerCity AS City, customerState AS State, customerZip AS Zip, customerEmail AS Email, customerPhone AS Phone FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        
    return render_template("customers.j2", data = data)

@app.route('/orders', methods=('GET', 'POST'))
def orders():
    # POST 
    #insert an order into Orders entity
    if request.method == "POST":
        # Execute if user presses Add_Order button
        if request.form.get("Add_Order"):
            #grab user form inputs
            customerID = request.form["customerID"]
            orderDate = request.form["orderDate"]
            
            #grab dynamic data from form inputs 
            countOrderItems = len([key for key in request.form.keys() if key.startswith('synthesizerID')])
            synthesizerLinePrice = 0
            try: 
                #calculate total price based on all order line items added by itereating through dynamic data
                for i in range(1, countOrderItems + 1):
                    synthesizerID = request.form[f"synthesizerID{i}"]
                    quantity = request.form[f"quantity{i}"]
                    querySynthesizerPrice = "SELECT synthesizerPrice,1 FROM Synthesizers WHERE synthesizerID = %s"
                    curPrice = mysql.connection.cursor()
                    curPrice.execute(querySynthesizerPrice, (int(synthesizerID),))
                    synthesizerUnitPrice = curPrice.fetchall()[0]["synthesizerPrice"]
                    if synthesizerUnitPrice is None:
                        synthesizerUnitPrice = 0
                    synthesizerLinePrice = float(synthesizerLinePrice) + (float(synthesizerUnitPrice) * float(quantity))
           
                #mySQL query to insert new Orders row         
                queryOrders = "INSERT INTO Orders (customerID, orderDate, orderPrice) VALUES (%s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(queryOrders, (customerID, orderDate, synthesizerLinePrice))
                mysql.connection.commit()

            except Exception as e:
                tb = traceback.format_exc()
                log(tb) # Log the detailed traceback
                return str(e), 500  # Return error message and HTTP 500 status code

            #find the recently added order and grab its auto-incremented/generated id                
            queryAddedOrder = "SELECT LAST_INSERT_ID()"
            curOrderID = mysql.connection.cursor()
            curOrderID.execute(queryAddedOrder)
            orderID = curOrderID.fetchall()
            orderIDValue = orderID[0]
            orderIDValue = orderIDValue.get("LAST_INSERT_ID()")
            
            #iterate through dynamic data, adding an Ordersynthesizer for each order line item
            for i in range(1, countOrderItems + 1):
                synthesizerID = request.form[f"synthesizerID{i}"]
                quantity = request.form[f"quantity{i}"]
                querySynthesizerPrice = "SELECT synthesizerPrice,1 FROM Synthesizers WHERE synthesizerID = %s"
                curPrice = mysql.connection.cursor()
                curPrice.execute(querySynthesizerPrice, (int(synthesizerID),))
                synthesizerUnitPrice = curPrice.fetchall()[0]["synthesizerPrice"]
                if synthesizerUnitPrice is None:
                    synthesizerUnitPrice = 0
                synthesizerLinePrice = (float(synthesizerUnitPrice) * float(quantity))

                #mySQL query to insert each order line item into OrderSynthesizer table
                queryOrderSynthesizer = "INSERT INTO OrderSynthesizer (orderID, synthesizerID, orderItemQuantity, orderItemUnitPrice, orderItemLinePrice) VALUES (%s, %s, %s, %s, %s)"
                curOrderSynthesizer = mysql.connection.cursor()
                curOrderSynthesizer.execute(queryOrderSynthesizer, (orderIDValue, synthesizerID, quantity, synthesizerUnitPrice, synthesizerLinePrice))
                mysql.connection.commit()

            return redirect("/orders")

    # Grab Orders data so we send it to our template to display  
    if request.method == "GET":
        # mySQL query to grab all the orders in Orders table
        query = "SELECT orderID AS ID, customerID AS CustomerID, orderDate AS Date, orderPrice AS Price FROM Orders"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        
        # mySQL query to grab all rows from Synthesizers table for SELECT drop-down user-input 
        queryGetSynthesizer = "SELECT synthesizerID, synthesizerName FROM Synthesizers ORDER BY synthesizerName"
        curGetSynthesizers = mysql.connection.cursor()
        curGetSynthesizers.execute(queryGetSynthesizer)
        synthesizersNames = curGetSynthesizers.fetchall()   

        # mySQL query to grab all rows from Customers table for SELECT drop-down user-input 
        queryGetCustomers = "SELECT customerFirstName, customerLastName, customerID FROM Customers ORDER BY customerFirstName, customerLastName"
        curGetCustomers = mysql.connection.cursor()
        curGetCustomers.execute(queryGetCustomers)
        customerNames = curGetCustomers.fetchall()   

    return render_template("orders.j2", data=data, synthesizersNames=synthesizersNames, customerNames=customerNames)

def log(tb: str):
    f = open("log.txt", "a")
    f.write(tb)
    f.close()

@app.route('/ordersynthesizer', methods=('GET', 'POST'))
def ordersynthesizer():
    # POST 
    #insert/update an order into OrderSynthesizer entity
    if request.method == "POST":
        print("Form data:", request.form)
        # Execute if user presses Update_OrderSynthesizer button
        if request.form.get("Update_OrderSynthesizer"):
            try:
                #grab user form inputs
                synthOrderID = request.form["synthOrderID"]
                orderSynthesizerID, orderID = synthOrderID.split(',')
                synthesizerID = request.form["synthesizerID"]
                quantity = request.form["quantity"]
                unit_price = request.form["unit-price"]
                if unit_price is None:
                    unit_price = 0
                line_price = float(unit_price) * int(quantity)

                #SQL query to find previous orderSynthesizer price
                getPreviousOrderSynthesizerPrice = "SELECT orderItemLinePrice, 1 FROM OrderSynthesizer WHERE orderSynthesizerID = %s"
                curGetPrice = mysql.connection.cursor()
                curGetPrice.execute(getPreviousOrderSynthesizerPrice, (int(orderSynthesizerID),))
                previousOrderSynthesizerPrice = float(curGetPrice.fetchall()[0]["orderItemLinePrice"])

                #SQL query to update orderSynthesizer
                updateOrderSynthesizer = "UPDATE OrderSynthesizer SET synthesizerID = %s, orderItemQuantity = %s, orderItemUnitPrice = %s, orderItemLinePrice = %s WHERE orderSynthesizerID = %s"
                curUpdate = mysql.connection.cursor()
                curUpdate.execute(updateOrderSynthesizer, (synthesizerID, quantity, unit_price, line_price, orderSynthesizerID))
                mysql.connection.commit()

                #SQL query to find previous associated order price
                getPreviousOrderPrice = "SELECT orderPrice, 1 FROM Orders WHERE orderID = %s"
                curGetOrderPrice = mysql.connection.cursor()
                curGetOrderPrice.execute(getPreviousOrderPrice, (int(orderID),))
                previousOrderPrice = float(curGetOrderPrice.fetchall()[0]["orderPrice"])

                #Calculate new order price
                newOrderPrice = (previousOrderPrice - previousOrderSynthesizerPrice) + line_price

                #SQL query to update associated order price
                updateOrderPrice = "UPDATE Orders SET orderPrice = %s WHERE orderID = %s"
                curUpdatePrice = mysql.connection.cursor()
                curUpdatePrice.execute(updateOrderPrice, (newOrderPrice, orderID))
                mysql.connection.commit()

            except Exception as e:
                tb = traceback.format_exc()
                log(tb)  # Log the detailed traceback
                return str(e), 500  # Return error message and HTTP 500 status code

        # Execute if user presses Add_OrderSynthesizer button
        if request.form.get("Add_OrderSynthesizer"):
            try:
                #grab user form inputs
                orderID = request.form["orderID"]
                synthesizerID = request.form["synthesizerID"]
                quantity = request.form["quantity"]
                
                #mySQL query to find associated synthesizer's price
                querySynthesizerPrice = "SELECT synthesizerPrice,1 FROM Synthesizers WHERE synthesizerID = %s"
                curPrice = mysql.connection.cursor()
                curPrice.execute(querySynthesizerPrice, (int(synthesizerID),))
                synthesizerUnitPrice = curPrice.fetchall()[0]["synthesizerPrice"]
                if synthesizerUnitPrice is None:
                    synthesizerUnitPrice = 0
                synthesizerLinePrice = (float(synthesizerUnitPrice) * float(quantity))

                #mySQL query to insert order OrderSynthesizer row
                query = "INSERT INTO OrderSynthesizer (orderID, synthesizerID, orderItemQuantity, orderItemUnitPrice, orderItemLinePrice) \
                          VALUES (%s, %s, %s, %s, %s)"
                curAddOrderSynthesizer = mysql.connection.cursor()
                curAddOrderSynthesizer.execute(query, (orderID, synthesizerID, quantity, synthesizerUnitPrice, synthesizerLinePrice))
                mysql.connection.commit()

                #mySQL query to update order based on new OrderSynthesizer row by adding the row total to current Orders price
                query2 = "UPDATE Orders \
                        SET orderPrice = orderPrice + %s \
                        WHERE orderID = %s;"                        
                curUpdateOrders = mysql.connection.cursor()
                curUpdateOrders.execute(query2, (synthesizerLinePrice, orderID))
                mysql.connection.commit()
                                
            except Exception as e:
                tb = traceback.format_exc()
                log(tb)  # Log the detailed traceback
                return str(e), 500  # Return error message and HTTP 500 status code

        return redirect("/ordersynthesizer")
        
    # Grab OrderSynthesizer data so we send it to our template to display  
    if request.method == "GET":
        # mySQL query to grab all the OrderSynthesizer in OrderSynthesizer table
        query = "SELECT orderSynthesizerID AS ID, orderID AS OrderID, synthesizerID AS SynthesizerID, orderItemQuantity AS ItemQuantity, orderItemUnitPrice AS UnitPrice, orderItemLinePrice AS LinePrice \
                  FROM OrderSynthesizer;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        
        # mySQL query to grab all rows from orderSynthesizer table for SELECT drop-down user-input 
        queryGetorderSynthesizerID = "SELECT orderSynthesizerID, orderID FROM OrderSynthesizer ORDER BY orderSynthesizerID"
        curGetorderSynthesizerID = mysql.connection.cursor()
        curGetorderSynthesizerID.execute(queryGetorderSynthesizerID)
        synthOrderIds = curGetorderSynthesizerID.fetchall()
        
        # mySQL query to grab all rows from orders table for SELECT drop-down user-input 
        queryGetorderID = "SELECT orderID FROM Orders"
        curGetorderID = mysql.connection.cursor()
        curGetorderID.execute(queryGetorderID)
        orderIds = curGetorderID.fetchall()
        
        # mySQL query to grab all rows from synthesizers table for SELECT drop-down user-input 
        queryGetSynthesizer = "SELECT synthesizerID, synthesizerName FROM Synthesizers ORDER BY synthesizerName"
        curGetSynthesizers = mysql.connection.cursor()
        curGetSynthesizers.execute(queryGetSynthesizer)
        synthesizersNames = curGetSynthesizers.fetchall()   

    return render_template("ordersynthesizer.j2", data=data, synthOrderIds=synthOrderIds, orderIds=orderIds, synthesizersNames=synthesizersNames)

@app.route('/delete_orderSynthesizer/<int:orderSynthesizerID>/<float:orderItemLinePrice>/<int:orderID>')
def delete_orderSynthesizer(orderSynthesizerID, orderItemLinePrice, orderID):
    #delete OrderSynthesizer row
    
    #mySQL query to delete OrderSynthesizer row
    query = "DELETE FROM OrderSynthesizer WHERE orderSynthesizerID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (orderSynthesizerID,))
    mysql.connection.commit()

    #mySQL query to update associated Order by subtracting deleted OrderSynthesizer row
    query2 = "UPDATE Orders \
              SET orderPrice = orderPrice - %s \
              WHERE orderID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query2, (orderItemLinePrice, orderID))
    mysql.connection.commit()
    
    return redirect("/ordersynthesizer")

@app.route('/purchases', methods=('GET', 'POST'))
def purchases():
    # POST 
    #insert purchase into Purchases table
    if request.method == "POST":
        # Execute if user presses Add_Purchase button
        if request.form.get("Add_Purchase"):
            try:
                #grab user form inputs
                orderID = request.form["orderID"]
                manufacturerID = request.form["manufacturerID"]
                purchaseDate = request.form["purchaseDate"]

                #grab dynamic data from form inputs
                countPurchaseItems = len([key for key in request.form.keys() if key.startswith('synthesizerID')])
                synthesizerLinePrice = 0
                try: 
                    #calculate total price based on all purchase line items added by itereating through dynamic data
                    for i in range(1, countPurchaseItems + 1):
                        synthesizerID = request.form[f"synthesizerID{i}"]
                        quantity = request.form[f"quantity{i}"]
                        querySynthesizerPrice = "SELECT synthesizerPrice,1 FROM Synthesizers WHERE synthesizerID = %s"
                        curPrice = mysql.connection.cursor()
                        curPrice.execute(querySynthesizerPrice, (int(synthesizerID),))
                        synthesizerUnitPrice = curPrice.fetchall()[0]["synthesizerPrice"]
                        if synthesizerUnitPrice == None:
                            synthesizerUnitPrice = 0
                        synthesizerLinePrice = float(synthesizerLinePrice) + (float(synthesizerUnitPrice) * float(quantity))

                        # account for null orderID
                        if orderID == "":
                            queryPurchases = "INSERT INTO Purchases (manufacturerID, purchaseDate, purchaseCost) VALUES (%s, %s, %s)"
                            cur = mysql.connection.cursor()
                            cur.execute(queryPurchases, (manufacturerID, purchaseDate, synthesizerLinePrice))
                            mysql.connection.commit()

                        # no null inputs
                        else:
                            queryPurchases = "INSERT INTO Purchases (orderID, manufacturerID, purchaseDate, purchaseCost) VALUES (%s, %s, %s, %s)"
                            cur = mysql.connection.cursor()
                            cur.execute(queryPurchases, (orderID, manufacturerID, purchaseDate, synthesizerLinePrice))
                            mysql.connection.commit()

                except Exception as e:
                    tb = traceback.format_exc()
                    log(tb) # Log the detailed traceback
                    return str(e), 500  # Return error message and HTTP 500 status code

                #find the recently added purchase and grab its auto-incremented/generated id                
                queryAddedPurchase = "SELECT LAST_INSERT_ID()"
                curPurchaseID = mysql.connection.cursor()
                curPurchaseID.execute(queryAddedPurchase)
                purchaseID = curPurchaseID.fetchall()
                purchaseIDValue = purchaseID[0]
                purchaseIDValue = purchaseIDValue.get("LAST_INSERT_ID()")

                #iterate through dynamic data, adding an Purchasesynthesizer for each purchase line item
                for i in range(1, countPurchaseItems + 1):
                    synthesizerID = request.form[f"synthesizerID{i}"]
                    quantity = request.form[f"quantity{i}"]
                    querySynthesizerPrice = "SELECT synthesizerPrice,1 FROM Synthesizers WHERE synthesizerID = %s"
                    curPrice = mysql.connection.cursor()
                    curPrice.execute(querySynthesizerPrice, (int(synthesizerID),))
                    synthesizerUnitPrice = curPrice.fetchall()[0]["synthesizerPrice"]
                    if synthesizerUnitPrice is None:
                        synthesizerUnitPrice = 0
                    synthesizerLinePrice = (float(synthesizerUnitPrice) * float(quantity))

                    queryPurchaseSynthesizer = "INSERT INTO PurchaseSynthesizer (PurchaseID, synthesizerID, PurchaseItemQuantity, PurchaseItemUnitCost, PurchaseItemLineCost) VALUES (%s, %s, %s, %s, %s)"
                    curPurchaseSynthesizer = mysql.connection.cursor()
                    curPurchaseSynthesizer.execute(queryPurchaseSynthesizer, (purchaseIDValue, synthesizerID, quantity, synthesizerUnitPrice, synthesizerLinePrice))
                    mysql.connection.commit()

            except Exception as e:
                tb = traceback.format_exc()
                log(tb)  # Log the detailed traceback
                return str(e), 500  # Return error message and HTTP 500 status code

            return redirect("/purchases")

    # Grab Purchases data so we send it to our template to display  
    if request.method == "GET":
        # mySQL query to grab all the purchases in Purchases table
        query = "SELECT purchaseID AS ID, orderID AS OrderID, manufacturerID AS ManufacturerID, purchaseDate AS Date, purchaseCost AS Cost FROM Purchases"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab all rows from orders table for SELECT drop-down user-input 
        queryGetorderID = "SELECT orderID FROM Orders"
        curGetorderID = mysql.connection.cursor()
        curGetorderID.execute(queryGetorderID)
        orderIds = curGetorderID.fetchall()  

        # mySQL query to grab all rows from manufacturers table for SELECT drop-down user-input 
        queryGetManufacturers = "SELECT manufacturerID, manufacturerName FROM Manufacturers"
        curGetManufacturers = mysql.connection.cursor()
        curGetManufacturers.execute(queryGetManufacturers)
        manufacturerIds = curGetManufacturers.fetchall()    

        #mySQL query to grab all rows from synthesziers table for SELET drop-down user-input
        queryGetSynthesizer = "SELECT synthesizerID, synthesizerName FROM Synthesizers ORDER BY synthesizerName"
        curGetSynthesizers = mysql.connection.cursor()
        curGetSynthesizers.execute(queryGetSynthesizer)
        synthesizersNames = curGetSynthesizers.fetchall()  

    return render_template("purchases.j2", data=data, orderIds=orderIds, manufacturerIds=manufacturerIds, synthesizersNames=synthesizersNames)

@app.route('/purchasesynthesizer', methods=('GET', 'POST'))
def purchasesynthesizer():
    # POST 
    #insert purchase into PurchaseSynthesizer table
    if request.method == "POST":
        print("Form data:", request.form)
        try: 
            # Execute if user presses Add_PurchaseSynthesizer button
            if request.form.get("Add_PurchaseSynthesizer"):
                tb = traceback.format_exc()

                #grab user form inputs
                purchaseID = request.form["purchaseID"]
                synthesizerID = request.form["synthesizerID"]
                quantity = request.form["quantity"]
                print(quantity)
                
                # Get synthesizer price from Synthesizer table
                querySynth = "SELECT synthesizerCost FROM Synthesizers WHERE synthesizerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(querySynth, (synthesizerID,))
                #calculate total line_price based on synthesizer cost     
                unit_price = cur.fetchall()[0]["synthesizerCost"]
                if unit_price is None:
                    unit_price = 0
                line_price = float(unit_price) * int(quantity)

                #mySQL query to insert new role into PurchaseSynthesizer
                query = "INSERT INTO PurchaseSynthesizer (purchaseID, synthesizerID, purchaseItemQuantity, purchaseItemUnitCost, purchaseItemLineCost) \
                        VALUES (%s, %s, %s, %s, %s)"
                curAddPurchaseSynthesizer = mysql.connection.cursor()
                curAddPurchaseSynthesizer.execute(query, (purchaseID, synthesizerID, quantity, unit_price, line_price))
                mysql.connection.commit()
                print("Commit successful")
             
                #mySQL query to updated associated purchase by adding PurchaseSynthesizer row cost to current purchase  
                query2 = "UPDATE Purchases \
                SET purchaseCost = purchaseCost + %s \
                WHERE purchaseID = %s;"             
                curUpdateOrders = mysql.connection.cursor()
                curUpdateOrders.execute(query2, (line_price, purchaseID))
                mysql.connection.commit()

        except Exception as e:
            tb = traceback.format_exc()
            log(tb)  # Log the detailed traceback
            return str(e), 500  # Return error message and HTTP 500 status code

        return redirect("/purchasesynthesizer")
    
    # Grab PurchaseSynthesizer data so we send it to our template to display  
    if request.method == "GET":
        # mySQL query to grab all the PurchaseSynthesizers in PurchaseSynthesizer table
        query = "SELECT purchaseSynthesizerID AS ID, purchaseID AS PurchaseID, synthesizerID as SynthesizerID, purchaseItemQuantity AS ItemQuantity, purchaseItemUnitCost AS UnitCost, purchaseItemLineCost AS LineCost FROM PurchaseSynthesizer"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        
        # mySQL query to grab all rows from Purchases table for SELECT drop-down user-input 
        queryGetpurchaseID = "SELECT purchaseID FROM Purchases"
        curGetpurchaseID = mysql.connection.cursor()
        curGetpurchaseID.execute(queryGetpurchaseID)
        purchaseIds = curGetpurchaseID.fetchall()
 
        # mySQL query to grab all rows from synthesizers table for SELECT drop-down user-input        
        queryGetSynthesizer = "SELECT synthesizerID, synthesizerName FROM Synthesizers ORDER BY synthesizerName"
        curGetSynthesizers = mysql.connection.cursor()
        curGetSynthesizers.execute(queryGetSynthesizer)
        synthesizersNames = curGetSynthesizers.fetchall()   

    return render_template("purchasesynthesizer.j2", data=data, purchaseIds=purchaseIds, synthesizersNames=synthesizersNames)

# Listener
if __name__ == "__main__":

    #Elizabeth port: 49408
    #Main port: 49484
    app.run(port=49484, debug=True)