
from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_home():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    if "state" in request.args:
        state = request.args ["state"]
        return render_template("home.html",candy = getStateOptions(counties), funFactoid = funFactoid(state))
    else:
        return render_template("home.html",candy = getStateOptions(counties))
def getStateOptions(counties):
    myList=[] 
    for county in counties:
        if not county["State"] in myList:
            myList.append (county["State"])
    options = ""
    for state in myList:
        options=options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options
def funFactoid(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    first = counties[0]["Education"]["Bachelor's Degree or Higher"]
    for county in counties:
        if county ["Education"]["Bachelor's Degree or Higher"]> first and state == county["State"]:    
            first=county["Education"]["Bachelor's Degree or Higher"] 
    return first
    
if __name__=="__main__":
    app.run(debug=True)