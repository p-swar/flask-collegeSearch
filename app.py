# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import request
import model
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

select_majors_list=[]
select_size_list=[]
select_location_list=[]

@app.route('/advancedSearch', methods = ["GET", "POST"])
def advancedSearch():
    if request.method == "GET":
        return render_template('advancedSearch.html')
    else:
        form = request.form
        select_choices = form["majors"]
        select_size = form["sizes"]
        select_location = form["locations"]

        
       
# def choose():
#     if 
        forms={
            "m":select_choices,
            "s":select_size,
            "l":select_location
            #"colleges": model.compare(select_choices,select_size,select_location)
        }
        colleges=model.compare(forms)

        # select_majors_list.append("m")
        # select_size_list.append("s")
        # select_location_list.append("l")
        # print("forms: "+str(forms))
        # print(select_choices)
        # print(select_size)
        # print(select_location)
        # print(select_majors_list)
        #model.compare(forms)
        return render_template('Compare.html', forms=forms, colleges=colleges)
    


# @app.route('/compare')
# def compare():
#     if forms["m"] == majors['Business and Management', "Business and Management1"]:
#         print()

#     return render_template('advancedSearch.html')
