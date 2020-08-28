import os
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

from wedding.utils.params import params
from wedding.utils.plots import plot_availability, plot_locations

from config import Config


def add_wedding_dash(server, routes_pathname_prefix: str = '/'):
    dashapp = dash.Dash(
        __name__,
        routes_pathname_prefix=routes_pathname_prefix,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        server=server
    )

    dashapp.layout = html.Div(children=[
        html.H1('Wedding Overview'),
        # html.Div(id='availability-data', style=params['no-show'],
        #          children=pd.read_csv(os.path.join(Config.DATA_DIR, 'wedding', 'availability.csv')).to_json()
        #          ),
        dcc.Graph(id='availability-figure', figure=plot_availability()),
        html.Br(),
        dcc.Graph(id='locations-figure', figure=plot_locations())
    ])


    return dashapp.server
