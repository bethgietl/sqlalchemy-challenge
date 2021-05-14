# -*- coding: utf-8 -*-
"""
Created on Wed May 12 10:08:52 2021

@author: bethg
"""

import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect
from flask import Flask, jsonify

# create engine to hawaii.sqlite
base_path = "Resources/hawaii.sqlite"
engine = create_engine(f'sqlite:///{base_path}')
conn = engine.connect()
#engine

# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save references. Map classes and create a session
M = Base.classes.measurement
S = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route('/')
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")

def precipitation():
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    result = session.query(M.date, M.prcp).filter(M.date >= last_year).all()
    # Create Dictionary of result and return it
    session.close()
    precip_to_return = {date: prcp for date, prcp in result}
    return jsonify(precip_to_return)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(S.station, S.name).all()
    session.close()
    # Convert list of tuples into normal list
    all_stations = list(results)
    return jsonify(all_stations)
        

@app.route("/api/v1.0/tobs")

def tobs():
    year_ago2 = dt.date(2017, 8 ,18) - dt.timedelta(days=365)
    result = session.query(M.date, M.tobs).filter_by(station='USC00519281').filter(M.date >= year_ago2).all()
    session.close()
    # Create Dictionary of result and return it
    tobs_to_return = {date: tobs for date, tobs in result}
    return jsonify(tobs_to_return)

@app.route("/api/v1.0/temp/<start>")
def start_stats(start=None):
    results = session.query(func.min(M.tobs), func.avg(M.tobs), func.max(M.tobs)).filter(M.date >= start).all()
    
    session.close()
    
    start_stats_to_return = {'Date Beginning': start, 'Temp Min': results[0][0], 'Temp Avg': results[0][1],'Temp Max': results[0][2]} 
    
    return jsonify(start_stats_to_return)


@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # create session link
    
    results = session.query(func.min(M.tobs), func.avg(M.tobs), func.max(M.tobs)).filter(M.date >= start).filter(M.date <=end).all()
    
    session.close()
    
    stats_to_return = {'Date Beginning': start, 'Date End': end, 'Temp Min': results[0][0], 'Temp Avg': results[0][1],'Temp Max': results[0][2]} 
    
    return jsonify(stats_to_return)
    
  

if __name__ == '__main__':
    app.run()
