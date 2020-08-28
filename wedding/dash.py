import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from wedding.utils.plots import plot_availability, plot_locations


def add_wedding_dash(server, routes_pathname_prefix: str = '/'):
    dashapp = dash.Dash(
        __name__,
        routes_pathname_prefix=routes_pathname_prefix,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        server=server
    )

    dashapp.layout = html.Div(children=[
        html.H1('Wedding Overview'),
        dcc.Graph(id='availability-figure', figure=plot_availability()),
        html.Br(),
        dcc.Graph(id='locations-figure', figure=plot_locations())
    ])

    return dashapp.server
