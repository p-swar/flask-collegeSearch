# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import request
from flask_pymongo import PyMongo
import os

# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')



# -- Routes section --
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html')


@app.route('/rankings')
def rankings():
    return render_template('rankings.html')


@app.route('/financialaid')
def financialaid():
    return render_template('FinancialAid.html')

@app.route('/advancedSearch')
def advancedSearch():
    return render_template('advancedSearch.html')


