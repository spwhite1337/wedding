import os
import argparse

from config import Config


def sync():
    parser = argparse.ArgumentParser()
    parser.add_argument('--upload')
    data_sync = 'aws'