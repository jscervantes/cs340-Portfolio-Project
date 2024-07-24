from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
from flask import Flask, render_template
import os

app = Flask(__name__)

# Routes
@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/synthesizers')
def synthesizers():
    return render_template("synthesizers.j2")

@app.route('/manufacturers')
def manufacturers():
    return render_template("manufacturers.j2")

@app.route('/customers')
def customers():
    return render_template("customers.j2")

@app.route('/orders')
def orders():
    return render_template("orders.j2")

@app.route('/purchases')
def purchases():
    return render_template("purchases.j2")

# Listener
if __name__ == "__main__":

    #Elizabeth port: 49408
    #Main port: 49484
    app.run(port=49484, debug=True)
