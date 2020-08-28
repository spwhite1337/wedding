import os
import pandas as pd
import plotly.express as px


from config import Config


def plot_availability():
    df = pd.read_csv(os.path.join(Config.DATA_DIR, 'wedding', 'availability.csv'))
    df['AsOfDate'] = pd.to_datetime(df['AsOfDate'])
    df['AvailableDate'] = pd.to_datetime(df['AvailableDate'])
    df = df[df['AsOfDate'] == df.groupby('Venue')['AsOfDate'].transform('max')]
    return px.scatter(df, x='AvailableDate', y='Venue', color='Venue')


def plot_locations():
    df = pd.read_csv(os.path.join(Config.DATA_DIR, 'wedding', 'locations.csv'))
    return px.scatter_geo(df, lat='Latitude', lon='Longitude', color='Venue', hover_data=['MinAirport'])
