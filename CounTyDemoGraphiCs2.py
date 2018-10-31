from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
@app.route("/index")
def render_index()

get State Options(counties)
  List listOfstates
  for each county in counties:
    add the conty's state to listOfStates
  Sting otptions
  for each state in listOfStates:
    options=options += Markup("<option value=\"" + s + "\">" + s + "</option>")
  return options
    
