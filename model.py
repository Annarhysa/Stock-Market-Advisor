import dash
from dash import dcc, html
import datetime as data
import yfinance as yf
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd 
import plotly.graph_objs as go 
import plotly.express as px 

from sklearn.model_selection import train_test_split, GridSearchCV
import numpy as np
from sklearn.svm import LinearSVR
from datetime import date, timedelta

def prediciton(stock, n_days):
    #loading the user specified stock from yfinance
    df = yf.download(stock, period='60d')
    df.reset_index(inplace = True)
    df['Day'] = df.index

    #storing the days in a list
    days = []
    for i in range(len(df.Day)):
        days.append([i])
    
    #splitting the dataste in features and targets
    x = days
    y = df[['Close']]
    


