import os
import argparse

from config import Config, logger


def upload():
    parser = argparse.ArgumentParser(prog='Upload data')
    parser.add_argument('--dryrun', action='store_true')
    args = parser.parse_args()

    sync_base = 'aws s3 sync '
    dryrun_arg = ' --dryrun'
    data_sync = '{} {}'.format(Config.DATA_DIR, Config.CLOUD_DATA)

    logger.info('Uploading Data')
    wd_sync = sync_base + data_sync
    wd_sync += dryrun_arg if args.dryrun else ''
    logger.info(wd_sync)
    os.system(wd_sync)
