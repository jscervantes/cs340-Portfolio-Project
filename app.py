from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
from flask import Flask, render_template
import os

app = Flask(__name__)

# database connection
# Template:

mysql = MySQL(app)

# Routes
@app.route('/')
def root():
    title = "Ciani Synths"
    return render_template("base.j2", title=title)

@app.route('/synthesizers', methods=('GET', 'POST'))
def synthesizers():
    synthesizers = [
        {
            "synthesizerID": "1",
            "manufacturerID": "1",
            "synthesizerName": "Juno60",
            "synthesizerCost": "2099.99",
            "synthesizerPrice": "2999.99",
            "signalType": "Analog",
            "keyboard": "TRUE"
        },

        {
            "synthesizerID": "2",
            "manufacturerID": "2",
            "synthesizerName": "Jupiter8",
            "synthesizerCost": "13335.99",
            "synthesizerPrice": "22930.99",
            "signalType": "Analog",
            "keyboard": "TRUE"
        },

        {
            "synthesizerID": "3",
            "manufacturerID": "3",
            "synthesizerName": "Prophet5",
            "synthesizerCost": "3999.99",
            "synthesizerPrice": "7899.99",
            "signalType": "Analog",
            "keyboard": "TRUE"
        },

        {
            "synthesizerID": "4",
            "manufacturerID": "4",
            "synthesizerName": "WavestateMK2",
            "synthesizerCost": "499.99",
            "synthesizerPrice": "699.99",
            "signalType": "Digital",
            "keyboard": "FALSE"
        },
        
        {
            "synthesizerID": "5",
            "manufacturerID": "5",
            "synthesizerName": "Grandmother",
            "synthesizerCost": "799.99",
            "synthesizerPrice": "999.99",
            "signalType": "Analog",
            "keyboard": "TRUE"
        }
              
    ]

    return render_template("synthesizers.j2")

@app.route('/manufacturers', methods=('GET', 'POST'))
def manufacturers():
    manufacturers = [
        {
            "manufacturerID": "1",
            "manufacturerName": "Roland",
            "manufacturerStreet": "123 Sesame St",
            "manufacturerStreet2": "NULL",
            "manufacturerCity": "Brooklyn",
            "manufacturerState": "New York",
            "manufacturerZip": "11214",
            "manufacturerEmail": "hi@roland.com",
            "manufacturerPhone": "7185553848"
        },

         {
            "manufacturerID": "2",
            "manufacturerName": "Sequential",
            "manufacturerStreet": "343 Nostrand Ave",
            "manufacturerStreet2": "NULL",
            "manufacturerCity": "Denver",
            "manufacturerState": "Colorado",
            "manufacturerZip": "34214",
            "manufacturerEmail": "hello@sequential.com",
            "manufacturerPhone": "8885553434"
        },        

        {
            "manufacturerID": "3",
            "manufacturerName": "Korg",
            "manufacturerStreet": "195 Vernon Rd",
            "manufacturerStreet2": "NULL",
            "manufacturerCity": "Portland",
            "manufacturerState": "Oregon",
            "manufacturerZip": "18383",
            "manufacturerEmail": "welcome@korg.com",
            "manufacturerPhone": "9395559282"
        },        
        {
            "manufacturerID": "4",
            "manufacturerName": "Moog",
            "manufacturerStreet": "17 Mississipi St",
            "manufacturerStreet2": "NULL",
            "manufacturerCity": "Bend",
            "manufacturerState": "Oregon",
            "manufacturerZip": "38458",
            "manufacturerEmail": "lol@moog.com",
            "manufacturerPhone": "9345552221"
        },        
        {
            "manufacturerID": "5",
            "manufacturerName": "Yamaha",
            "manufacturerStreet": "9039 Wow St",
            "manufacturerStreet2": "NULL",
            "manufacturerCity": "Providence",
            "manufacturerState": "Rhode Island",
            "manufacturerZip": "38933",
            "manufacturerEmail": "hey@yamaha.com",
            "manufacturerPhone": "5555555555"
        }              
    ]

    return render_template("manufacturers.j2", manufacturers = manufacturers)

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
            customerID = request.form["customerID"]
            orderDate = request.form["orderDate"]
            orderPrice = request.form["orderPrice"]
            
            query = "INSERT INTO Orders (customerID, orderDate, orderPrice) VALUES (%s, %s, %s)"

            cur = mysql.connection.cursor()
            cur.execute(query, (customerID, orderDate, orderPrice))

            mysql.connection.commit()
    
            return redirect("/orders")

    
    if request.method == "GET":
        query = "SELECT orderID, customerID, orderDate, orderPrice FROM Orders"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

    return render_template("orders.j2", data=data)

@app.route('/ordersynthesizer', methods=('GET', 'POST'))
def ordersynthesizer():
    orderSynthesizers = [
          {
            "id": "1",
            "orderId": "1",
            "synthesizerId": "1",
            "synthesizerQuantity": "2",
            "synthesizerUnitPrice": "2999.99",
            "synthesizerLinePrice": "5999.98"
        },
          {
            "id": "2",
            "orderId": "1",
            "synthesizerId": "2",
            "synthesizerQuantity": "1",
            "synthesizerUnitPrice": "22930.99",
            "synthesizerLinePrice": "22930.99"
        },
          {
            "id": "3",
            "orderId": "2",
            "synthesizerId": "5",
            "synthesizerQuantity": "3",
            "synthesizerUnitPrice": "999.99",
            "synthesizerLinePrice": "2999.97"
        },
          {
            "id": "4",
            "orderId": "3",
            "synthesizerId": "1",
            "synthesizerQuantity": "1",
            "synthesizerUnitPrice": "2999.99",
            "synthesizerLinePrice": "2999.99"
        },
          {
            "id": "5",
            "orderId": "4",
            "synthesizerId": "4",
            "synthesizerQuantity": "1",
            "synthesizerUnitPrice": "699.99",
            "synthesizerLinePrice": "699.99"
        },
          {
            "id": "6",
            "orderId": "4",
            "synthesizerId": "3",
            "synthesizerQuantity": "1",
            "synthesizerUnitPrice": "7899.99",
            "synthesizerLinePrice": "7899.99"
        },
          {
            "id": "7",
            "orderId": "5",
            "synthesizerId": "1",
            "synthesizerQuantity": "1",
            "synthesizerUnitPrice": "2999.99",
            "synthesizerLinePrice": "2999.99"
        },
        ]
    return render_template("ordersynthesizer.j2", orderSynthesizers=orderSynthesizers)

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
