import os
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

    # Distribution of temperatures by month-day-hour

    # Distribution of temperatures by month-week-hour

    # Time-series of temp by hour on month-day broken down by year

    # Time-series of temp by day on month broken down by year

    # Rain by hour

    # Rain by day

