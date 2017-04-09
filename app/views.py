from flask import render_template, flash, redirect
from app import app
# from .forms import LoginForm

@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    return render_template("beta.html")

@app.route('/cytoscape-edge.js',methods=['GET', 'POST'])
def cytoscape():
    return render_template("cytoscape-edge.js")

@app.route('/code.js', methods=['GET', 'POST'])
def code():
    return render_template("code.js")