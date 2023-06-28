from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import pandas_datareader.data as web

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div(children = [
      html.H1("Stock Vizualization Dashboard"),
      html.H4("Please enter the stock name"),
      dcc.Input(id="input", value ='', type='text'),
      html.Div(id="output-graph")
])


@app.callback(
    Output(component_id ="output-graph", 
    component_property = "children"),
    [Input(component_id = "input", 
    component_property = "value")])

def update_value(input_data):
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime.now()
    df = web.DataReader(input_data, 'yahoo', start, end)
    return dcc.Graph(id = "demo", figure ={'data': 
    [{'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},],
    'layout': {'title': input_data}})


if __name__ == "__main__":
    app.run_server(debug=True)