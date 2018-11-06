
from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_home():
    with open('county-demographics2.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template("home.html",candy = getStateOptions(counties))
def getStateOptions(counties):
    myList=[] 
    for county in counties:
        if not county("State") in myList:
            myList
    otptions = ""
    for state in listOfStates:
        options=options + Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options
    
if __name__=="__main__":
    app.run(debug=True, port=54321)