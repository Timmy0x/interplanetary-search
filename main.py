
from flask import Flask, render_template, Response, request

import requests

from api import api_search

app = Flask(__name__)

header = open("templates/snippets/header.html").read()
nav = open("templates/snippets/nav.html").read()


@app.route("/")
def index():
    return render_template("index.html",
                           header=header,
                           nav=nav)

@app.route("/search")
def search():
    return render_template("search.html",
                           header=header,
                           nav=nav,
                           results=api_search(request.args.get("q")),
                           query=request.args.get("q"))

"""
Static
"""
@app.route("/styles/<name>.css")
def styles(name):
    return Response(open(f"templates/styles/{name}.css").read(), mimetype="text/css")

@app.route("/scripts/<name>.js")
def scripts(name):
    return Response(open(f"templates/scripts/{name}.js").read(), mimetype="text/javascript")

@app.route("/images/<type>/<name>")
def images(type, name):
    return Response(open(f"templates/images/{type}/{name}", "rb").read(), mimetype=f"image/{type}")


app.run(host="0.0.0.0", port=420, debug=True)