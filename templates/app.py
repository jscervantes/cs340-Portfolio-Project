from flask import Flask, render_template, json, redirect
# from flask_mysqldb import MySQL
from flask import request
from flask import Flask, render_template
import os

app = Flask(__name__)

# Routes
@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/synthesizers', methods=('GET', 'POST'))
def synthesizers():
    return render_template("synthesizers.j2")

@app.route('/manufacturers', methods=('GET', 'POST'))
def manufacturers():
    return render_template("manufacturers.j2")

@app.route('/customers', methods=('GET', 'POST'))
def customers():
    return render_template("customers.j2")

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
    app.run(port=49444, debug=True)
