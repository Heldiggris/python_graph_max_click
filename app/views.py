from flask import render_template, flash, redirect
from app import app
# from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():

    return render_template("beta.html")
@app.route('/cytoscape-edge.js')
def login():
    return render_template("cytoscape-edge.js")
@app.route('/style.css')
def style():
    return render_template("style.css")
@app.route('/code.js')
def code():
    return render_template("code.js")