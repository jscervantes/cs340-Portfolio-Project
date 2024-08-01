from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
from flask import Flask, render_template
import os

app = Flask(__name__)

# Routes
@app.route('/')
def root():
    title = "Ciani Synths"
    return render_template("base.j2", title=title)

@app.route('/synthesizers', methods=('GET', 'POST'))
def synthesizers():
    return render_template("synthesizers.j2")

@app.route('/manufacturers', methods=('GET', 'POST'))
def manufacturers():
    return render_template("manufacturers.j2")

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
    return render_template("orders.j2")

@app.route('/ordersynthesizer', methods=('GET', 'POST'))
def ordersynthesizer():
    return render_template("ordersynthesizer.j2")

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
