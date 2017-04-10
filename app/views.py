from flask import render_template, flash, redirect
from flask import request
from app import app
from networkx import nx
import networkx.algorithms.clique as cl
import json



def Graph_max_clique(graph):
    clique_max_all = []
    clique = [i for i in cl.find_cliques(graph)]
    max_len_clique = len(clique[0])
    for i in clique:
        if(max_len_clique <= len(i)):
            max_len_clique = len(i)
    for i in clique:
        if(max_len_clique ==len(i)):
            clique_max_all.append(i)
    return clique_max_all




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

@app.route('/_find', methods=['GET', 'POST'])
def find():
    matrix = []
    data = request.json
    graph = nx.Graph()
    try:
        for i in data['elements']['nodes']:
            graph.add_node(i['data']['id'])
    except:
        pass
    try:
        for i in data['elements']['edges']:
            graph.add_edge(i['data']['source'], i['data']['target'])
    except:
        pass
    if request.method == "POST":
        return json.dumps(Graph_max_clique(graph))
    else:
        return -1