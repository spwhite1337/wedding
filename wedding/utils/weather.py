import os
import matplotlib.pyplot as plt

from wedding.utils.load import load_weather

from config import Config, logger


class WeatherAnalyzer(object):
    source_data_fp = os.path.join(Config.DATA_DIR, 'wedding', 'noblesville_weather.csv')
    plots_dir = ''

    # Distribution of temperatures by hour

    # Time-series of temp by hour broken down by year

    # Rain by hour

    # Rain by day

