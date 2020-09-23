import os
import pandas as pd

from config import Config, logger


def load_weather() -> pd.DataFrame:
    logger.info('Loading weather data')
    df = pd.read_csv(os.path.join(Config.DATA_DIR, 'weather', 'noblesville_weather.csv'))
    df['dt_iso'] = pd.to_datetime(df['dt_iso'].str.replace(' \+0000 UTC', ''))
    # Correct for time-zone (it is now in EST)
    df['dt_iso'] = df['dt_iso'] - pd.Timedelta(4, 'H')
    # Get important parts of date
    df['year'] = df['dt_iso'].dt.year
    df['month'] = df['dt_iso'].dt.month
    df['week'] = df['dt_iso'].dt.isocalendar().week
    df['day'] = df['dt_iso'].dt.day
    df['hour'] = df['dt_iso'].dt.hour

    return df
