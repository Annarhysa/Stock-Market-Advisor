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

#def prediciton(stock, n_days):
