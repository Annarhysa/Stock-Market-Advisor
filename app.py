import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([item, item2])

if __name__ == '__main__':
    app.run_server(debug=True)