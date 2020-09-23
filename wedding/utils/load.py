import os
import pandas as pd

from config import Config, logger


def load_weather() -> pd.DataFrame:
    logger.info('Loading weather data')
    df = pd.read_csv(os.path.join(Config.DATA_DIR, 'weather', 'noblesville_weather.csv'))
    df['dt_iso'] = pd.to_datetime(df['dt_iso'].str.replace(' \+0000 UTC', ''))
    df['year'] = df['dt_iso'].dt.year
    df['month'] = df['dt_iso'].dt.month
    df['day'] = df['dt_iso'].dt.day

    return df
