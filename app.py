#References: 
# https://canvas.oregonstate.edu/courses/1967354/pages/exploration-developing-in-flask?module_item_id=24460849

from flask import Flask, render_template, json, redirect, request
from flask_mysqldb import MySQL
import os
import traceback

app = Flask(__name__)

# database connection
# Template:

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
        query = "SELECT synthesizerID, manufacturerID, synthesizerName, synthesizerCost, synthesizerPrice, signalType, keyboard FROM Synthesizers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        
        # Get info from db for manufacturer drop down
        query2 = "SELECT manufacturerID, manufacturerName FROM Manufacturers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        manufacturerData = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("synthesizers.j2", data=data, manufacturerData = manufacturerData)

    return render_template("synthesizers.j2")

@app.route('/manufacturers', methods=('GET', 'POST'))
def manufacturers():
    
    if request.method == "GET":
        query = "SELECT manufacturerID, manufacturerName, manufacturerStreet, manufacturerStreet2, manufacturerCity, manufacturerState, manufacturerZip, manufacturerEmail, manufacturerPhone FROM Manufacturers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    return render_template("manufacturers.j2", data = data)

@app.route('/customers', methods=('GET', 'POST'))
def customers():
    customers = [
          {
            "id": "1",
            "firstname": "Naomi",
            "lastname": "Shaw",
            "street": "596 Edgefield Drive",
            "street2": "NULL",
            "city": "Clarksburg",
            "state": "WV",
            "zip": "26301",
            "email": "likvidatorcelok@ezsmail.com",
            "phone": "7188904009"
        },
          {
            "id": "2",
            "firstname": "Brendan",
            "lastname": "Frye",
            "street": "3308 Godfrey Street",
            "street2": "NULL",
            "city": "Portland",
            "state": "OR",
            "zip": "97229",
            "email": "fromponmachineus@jojoo.online",
            "phone": "7188904009"
        },
          {
            "id": "3",
            "firstname": "Calvin",
            "lastname": "Melton",
            "street": "103 Mutton Town Road",
            "street2": "NULL",
            "city": "Vancouver",
            "state": "WA",
            "zip": "98663",
            "email": "someong6n9v@bankinnepal.com",
            "phone": "3051178216"
        },
          {
            "id": "4",
            "firstname": "Lacey",
            "lastname": "Robbins",
            "street": "3823 Heron Way",
            "street2": "NULL",
            "city": "Portland",
            "state": "OR",
            "zip": "97205",
            "email": "64j0cy5q5@dunilakeling.com",
            "phone": "3051178216"
        },
          {
            "id": "5",
            "firstname": "Dana",
            "lastname": "Greer",
            "street": "1225 New Street",
            "street2": "NULL",
            "city": "Eugene",
            "state": "OR",
            "zip": "97401",
            "email": "parapamm@bmuss.com",
            "phone": "7775332610"
        },
        ]
    return render_template("customers.j2", customers = customers)

@app.route('/orders', methods=('GET', 'POST'))
def orders():
    
    if request.method == "POST":
        if request.form.get("Add_Order"):
            synthesizerID = request.form["synthesizerID"]
            quantity = request.form["quantity"]
            customerID = request.form["customerID"]
            orderDate = request.form["orderDate"]

            # try:
            querySynthesizerPrice = "SELECT synthesizerPrice,1 FROM Synthesizers WHERE synthesizerID = %s"
            curPrice = mysql.connection.cursor()
            curPrice.execute(querySynthesizerPrice, (int(synthesizerID),))
            synthesizerUnitPrice = curPrice.fetchall()[0]["synthesizerPrice"]
            #     log("synthesizerPrice:" + str(synthesizerUnitPrice))
            # except Exception:
            #     tb = traceback.format_exc()
            #     log(tb)

            synthesizerLinePrice = int(synthesizerUnitPrice) * int(quantity)
               
            queryOrders = "INSERT INTO Orders (customerID, orderDate, orderPrice) VALUES (%s, %s, %s)"

            cur = mysql.connection.cursor()
            cur.execute(queryOrders, (customerID, orderDate, synthesizerLinePrice))

            mysql.connection.commit()
            
            queryAddedOrder = "SELECT LAST_INSERT_ID()"
            curOrderID = mysql.connection.cursor()
            curOrderID.execute(queryAddedOrder)
            orderID = curOrderID.fetchall()
            orderIDValue = orderID[0]
            orderIDValue = orderIDValue.get("LAST_INSERT_ID()")
            
            queryOrderSynthesizer = "INSERT INTO OrderSynthesizer (orderID, synthesizerID, orderItemQuantity, orderItemUnitPrice, orderItemLinePrice) VALUES (%s, %s, %s, %s, %s)"
            curOrderSynthesizer = mysql.connection.cursor()
            curOrderSynthesizer.execute(queryOrderSynthesizer, (orderIDValue, synthesizerID, quantity, synthesizerUnitPrice, synthesizerLinePrice))
            mysql.connection.commit()

            return redirect("/orders")

    
    if request.method == "GET":
        query = "SELECT orderID, customerID, orderDate, orderPrice FROM Orders"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    return render_template("orders.j2", data=data)

def log(tb: str):
    f = open("log.txt", "a")
    f.write(tb)
    f.close()

@app.route('/ordersynthesizer', methods=('GET', 'POST'))
def ordersynthesizer():
    if request.method == "POST":
        if request.form.get("Update_OrderSynthesizer"):
            try:
                synthOrderID = request.form["synthOrderID"]
                orderSynthesizerID, orderID = synthOrderID.split(',')
                synthesizerID = request.form["synthesizerID"]
                quantity = request.form["quantity"]
                unit_price = request.form["unit-price"]
                line_price = float(unit_price) * int(quantity)

                getPreviousOrderSynthesizerPrice = "SELECT orderItemLinePrice, 1 FROM OrderSynthesizer WHERE orderSynthesizerID = %s"
                curGetPrice = mysql.connection.cursor()
                curGetPrice.execute(getPreviousOrderSynthesizerPrice, (int(orderSynthesizerID),))
                previousOrderSynthesizerPrice = float(curGetPrice.fetchall()[0]["orderItemLinePrice"])

                updateOrderSynthesizer = "UPDATE OrderSynthesizer SET synthesizerID = %s, orderItemQuantity = %s, orderItemUnitPrice = %s, orderItemLinePrice = %s WHERE orderSynthesizerID = %s"
                curUpdate = mysql.connection.cursor()
                curUpdate.execute(updateOrderSynthesizer, (synthesizerID, quantity, unit_price, line_price, orderSynthesizerID))
                mysql.connection.commit()

                getPreviousOrderPrice = "SELECT orderPrice, 1 FROM Orders WHERE orderID = %s"
                curGetOrderPrice = mysql.connection.cursor()
                curGetOrderPrice.execute(getPreviousOrderPrice, (int(orderID),))
                previousOrderPrice = float(curGetOrderPrice.fetchall()[0]["orderPrice"])

                newOrderPrice = (previousOrderPrice - previousOrderSynthesizerPrice) + line_price

                updateOrderPrice = "UPDATE Orders SET orderPrice = %s WHERE orderID = %s"
                curUpdatePrice = mysql.connection.cursor()
                curUpdatePrice.execute(updateOrderPrice, (newOrderPrice, orderID))
                mysql.connection.commit()

            except Exception as e:
                tb = traceback.format_exc()
                log(tb)  # Log the detailed traceback
                return str(e), 500  # Return error message and HTTP 500 status code

            return redirect("/ordersynthesizer")

    if request.method == "GET":
        query = "SELECT orderSynthesizerID, orderID, synthesizerID, orderItemQuantity, orderItemUnitPrice, orderItemLinePrice \
                  FROM OrderSynthesizer;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        
        queryGetorderSynthesizerID = "SELECT orderSynthesizerID, orderID FROM OrderSynthesizer"
        curGetorderSynthesizerID = mysql.connection.cursor()
        curGetorderSynthesizerID.execute(queryGetorderSynthesizerID)
        synthOrderIds = curGetorderSynthesizerID.fetchall()
        
        queryGetorderID = "SELECT orderID FROM Orders"
        curGetorderID = mysql.connection.cursor()
        curGetorderID.execute(queryGetorderID)
        orderIds = curGetorderID.fetchall()
        
        queryGetSynthesizer = "SELECT synthesizerID, synthesizerName FROM Synthesizers"
        curGetSynthesizers = mysql.connection.cursor()
        curGetSynthesizers.execute(queryGetSynthesizer)
        synthesizersNames = curGetSynthesizers.fetchall()


        

    return render_template("ordersynthesizer.j2", data=data, synthOrderIds=synthOrderIds, orderIds=orderIds, synthesizersNames=synthesizersNames)

@app.route('/delete_orderSynthesizer/<int:orderSynthesizerID>/<float:orderItemLinePrice>/<int:orderID>')
def delete_orderSynthesizer(orderSynthesizerID, orderItemLinePrice, orderID):
    query = "DELETE FROM OrderSynthesizer WHERE orderSynthesizerID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (orderSynthesizerID,))
    mysql.connection.commit()

    query2 = "UPDATE Orders \
              SET orderPrice = orderPrice - %s \
              WHERE orderID = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query2, (orderItemLinePrice, orderID))
    mysql.connection.commit()
    
    return redirect("/ordersynthesizer")

# @app.route("/edit_orderSynthesizer/<int:orderSynthesizerID>", methods=["GET", "POST"])
# def edit_orderSynthesizer(orderSynthesizerID):
# #   if request.method == "GET":
# #     # grab info for orderSynthesizer with passed ID
# #     query = "Select * FROM OrderSynthesizer WHERE orderSynthesizerID = %s"
# #     cur = mysql.connection.cursor()
# #     cur.execute(query, (orderSynthesizerID,))
# #     data = cur.fetchall()

# #     # fetch data for orderID and synthesizerID dropdowns
# #     query2 = "SELECT orderID, synthesizerID FROM OrderSynthesizer WHERE orderSynthesizerID = %s"
# #     cur = mysql.connection.cursor()
# #     cur.execute(query2, (orderSynthesizerID,))
# #     ordersynthesizer_data = cur.fetchall()

#     return render_template("edit_orderSynthesizer.j2", data=data, ordersynthesizer_data=ordersynthesizer_data)

@app.route('/purchases', methods=('GET', 'POST'))
def purchases():
    return render_template("purchases.j2")

@app.route('/purchasesynthesizer', methods=('GET', 'POST'))
def purchasesynthesizer():
    return render_template("purchasesynthesizer.j2")


# Listener
if __name__ == "__main__":

    #Elizabeth port: 49408
    #Main port: 49484
    app.run(port=49484, debug=True)
