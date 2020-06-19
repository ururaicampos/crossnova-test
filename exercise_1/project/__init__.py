import dash
import dash_core_components as dcc
import dash_html_components as html

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import AutoDatabase


flask = Flask(__name__)
flask.config.from_object('project.config.Config')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, server=flask, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Crossnova interview test'),
    html.Label([
        'Select the X axis variable.',
        dcc.Dropdown(
            id='variable1',
            options=[
                {'label': 'Acceleration', 'value': 'acceleration'},
                {'label': 'Cilinders', 'value': 'cilinders'},
                {'label': 'Displacement', 'value': 'displacement'},
                {'label': 'Horsepower', 'value': 'horsepower'},
                {'label': 'Model Year', 'value': 'model_year'},
                {'label': 'Weight', 'value': 'weight'},
                {'label': 'Miles per gallon', 'value': 'mpg'},
            ],
            placeholder="X axis",
        )
    ]),
    html.Label([
        'Select the Y axis variable.',
        dcc.Dropdown(
            id='variable2',
            options=[
                {'label': 'Acceleration', 'value': 'acceleration'},
                {'label': 'Cilinders', 'value': 'cilinders'},
                {'label': 'Displacement', 'value': 'displacement'},
                {'label': 'Horsepower', 'value': 'horsepower'},
                {'label': 'Model Year', 'value': 'model_year'},
                {'label': 'Weight', 'value': 'weight'},
                {'label': 'Miles per gallon', 'value': 'mpg'},
            ],
            placeholder="Y axis",
        )
    ]),
    html.Div(dcc.Graph(id='graph')),
])

@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('variable1', 'value'),
    dash.dependencies.Input('variable2', 'value')])
def update_output(variable1, variable2):
    '''
    Receive the variables in the dropdown, search for it in the database and update
    the graph.

    :param variable1: Variable representing the x axis value.
    :type variable1: **str**

    :param variable2: Variable representing the y axis value.
    :type variable2: **str**

    :return : The graph with the results.
    :rtype: **dict**
    '''
    df = {}
    if variable1 is None or variable2 is None:
        df[variable1] = []
        df[variable2] = []
    else:
        df = AutoDatabase([variable1,variable2]).get_database_info()
    
    return {
        'data': [
            dict(
                x=df[variable1],
                y=df[variable2],
                text=df[variable2],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ) for i in df
        ],
        'layout':
            dict(
                xaxis={'title': 'x: {}'.format(variable1) if variable1 != None else ''},
                yaxis={'title': 'y: {}'.format(variable2) if variable2 != None else ''},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )        
    }
