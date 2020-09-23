import os
import matplotlib.pyplot as plt

from wedding.utils.load import load_weather

from config import Config, logger


class WeatherAnalyzer(object):
    source_data_fp = os.path.join(Config.DATA_DIR, 'wedding', 'noblesville_weather.csv')
    plots_dir = Config.PLOTS_DIR

    # Time-series by hour on day or range-of-days plotting mean / std or median / std

    # Distribution of temperatures by month-day-hour

    # Distribution of temperatures by month-week-hour

    # Time-series of temp by hour on month-day broken down by year

    # Time-series of temp by day on month broken down by year

    # Rain by hour

    # Rain by day

