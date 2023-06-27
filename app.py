import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([item1, item2])

html.Div(
          [
            html.P("Welcome to the Stock Dash App!", className="start"),
            html.Div([
              # stock code input
            ]),
            html.Div([
              # Date range picker input
            ]),
            html.Div([
              # Stock price button
              # Indicators button
              # Number of days of forecast input
              # Forecast button
            ]),
          ],
        className="nav")

html.Div(
          [
            html.Div(
                  [  # Logo
                    # Company Name
                  ],
                className="header"),
            html.Div( #Description
              id="description", className="decription_ticker"),
            html.Div([
                # Stock price plot
            ], id="graphs-content"),
            html.Div([
                # Indicator plot
            ], id="main-content"),
            html.Div([
                # Forecast plot
            ], id="forecast-content")
          ],
        className="content")       

        html.Div(
            [
              html.Div(
                    [  # Logo
                      # Company Name
                    ],
                  className="header"),
              html.Div( #Description
                id="description", className="decription_ticker"),
              html.Div([
                  # Stock price plot
              ], id="graphs-content"),
              html.Div([
                  # Indicator plot
              ], id="main-content"),
              html.Div([
                  # Forecast plot
              ], id="forecast-content")
            ],
          className="content")

if __name__ == '__main__':
    app.run_server(debug=True)