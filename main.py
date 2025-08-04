# made w/ ai (actual intelligence)

# online tools used:
#
# Flask documentation

import os
from flask import Flask, render_template, send_from_directory
import requests
import json

app = Flask(__name__)

@app.route("/")
def thing():
    return render_template("index.html")

#https://flask.palletsprojects.com/en/stable/patterns/favicon/

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/style.css')
def stylesheet():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'style.css', mimetype='text/css')

@app.route('/logo.png')
def logo():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'logo.png', mimetype='image/png')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route("/buy") #yay last endpoint!?
def buy():
    return render_template("payment.html")

@app.route("/catfact")
def catfact():
    catfactdict = requests.get("https://catfact.ninja/fact?max_length=75").json()
    return catfactdict["fact"]