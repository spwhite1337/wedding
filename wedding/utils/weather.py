import os
import numpy as np
import matplotlib.pyplot as plt

from wedding.utils.load import load_weather

from config import Config, logger


class WeatherAnalyzer(object):
    source_data_fp = os.path.join(Config.DATA_DIR, 'wedding', 'noblesville_weather.csv')
    plots_dir = Config.PLOTS_DIR

    # Time-series by hour on month-day or range-of-days plotting mean / std or median / std
    def time_series_by_day(self, month: int, day: int):
        df = load_weather()
        df = df[(df['month'] == month) & (df['day'] == day)]
        df = df.groupby('hour').agg(temp=('temp', 'mean'), temp_std=('temp', 'std')).reset_index()

        plt.figure(figsize=(8, 8))
        plt.plot(df['hour'], df['temp'])
        plt.fill_between(df['hour'], df['temp'] - df['temp_std'], df['temp'] + df['temp_std'], alpha=0.5)
        plt.xlabel('Hour of Day')
        plt.ylabel('Temperature')
        plt.title('Date: {}-{}'.format(month, day))
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(self.plots_dir, 'time_series_by_day_{}_{}.png'.format(month, day)))
        plt.close()

    # Time-series of temp by hour on month-day broken down by year
    def time_series_on_month_day_by_year(self, month: int, day: int):
        df = load_weather()
        df = df[(df['month'] == month) & (df['day'] == day)]
        plt.figure(figsize=(8, 8))
        for year, df_plot in df.groupby('year'):
            plt.plot(df_plot['hour'], df_plot['temp'], label=year)
        plt.xlabel('Hour of Day')
        plt.ylabel('Temperature')
        plt.legend()
        plt.title('Date: {}-{}'.format(month, day))
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(self.plots_dir, 'time_series_on_month_day_by_year_{}_{}.png'.format(month, day)))
        plt.close()

    # Distribution of temperatures by month-day-hour
    def distribution_by_month_day_hour(self, month: int, day: int, hour: int):
        df = load_weather()
        df = df[(df['month'] == month) & (df['day'] == day) & (df['hour'] == hour)]
        plt.figure(figsize=(8, 8))
        plt.hist(df['temp'], bins=np.linspace(30, 80, 11))
        plt.vlines(df['temp'].mean(), 0, 5, label='mean')
        plt.vlines(df['temp'].median(), 0, 5, label='median', color='lightgray')
        plt.grid(True)
        plt.legend()
        plt.xlabel('Temperature (F)')
        plt.ylabel('Counts')
        plt.title('Datetime: {}-{} at {}'.format(month, day, hour))
        plt.tight_layout()
        plt.savefig(os.path.join(self.plots_dir, 'distribution_by_month_day_hour_{}_{}_at_{}.png'.format(
            month, day, hour))
                    )
        plt.close()

    # Distribution of temperatures by month-week-hour

    # Time-series of temp by day on month broken down by year

    # Rain by hour
    def distribution_rain_by_month_day(self, month: int, day: int):
        df = load_weather()
        df = df[(df['month'] == month) & (df['day'] == day)]
        plt.figure(figsize=(8, 8))
        plt.hist(df['rain_1h'])
        plt.vlines(0.0787402, 0, 10, label='light-rain')
        plt.vlines(0.15748, 0, 10, label='heavy-rain')
        # plt.hist(df['rain_3h'])
        plt.grid(True)
        plt.xlabel('Rain (in) in an hour')
        plt.ylabel('Counts')
        plt.title('Datetime: {}-{}'.format(month, day))
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(self.plots_dir, 'distribution_rain_by_month_day_hour_{}_{}.png'.format(month, day)))
        plt.close()

    # Rain by day

