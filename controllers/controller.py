from app import app
from flask import render_template
from models.orders_list import *


@app.route('/')
def index():
    return render_template('index.jinja', orders = orders)

@app.route('/order/<index>')
def order(index):
    i = int(index)
    return render_template('order.jinja', order = orders[i])

