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

@app.route('/advancedSearch', methods = ["GET", "POST"])
def advancedSearch():
    if request.method == "GET":
        print("")
    else:
        form = request.form
        select_choices = form["majors"]
        select_size = form["sizes"]
        select_location = form["locations"]
        forms{
            "m":select_choices,
            "s":select_size,
            "l":select_location
        }

        print(select_choices)
        print(select_size)
        print(select_location)
    return render_template('advancedSearch.html', forms = forms)



@app.route('/compare')
def compare():
    if forms["m"] == majors['Business and Management', "Business and Management1"]:
        print()

    return render_template('advancedSearch.html')
