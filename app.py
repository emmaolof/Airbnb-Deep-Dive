import requests
import json
import prettytable
import xlwt
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/index.html")
def indexPage():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/Sumi_Maps.html")
def sumiPage():
    """Return the homepage."""
    return render_template("Sumi_Maps.html")

@app.route("/Jeremy_Maps.html")
def jeremyPage():
    """Return the homepage."""
    return render_template("Jeremy_Maps.html")

@app.route("/Emmanuel_Maps.html")
def emmanuelPage():
    """Return the homepage."""
    return render_template("Emmanuel_Maps.html")      

@app.route("/countynames")
def names():
    """Return a list of sample names."""
    data  = {"County": "1"},{"County": "2"},{"County": "3"}
    sampleNames = jsonify(data)
    # Return a list of the county  names (sample names)
    return sampleNames

if __name__ == '__main__':
    app.run()
