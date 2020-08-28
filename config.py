import os
import logging


# Setup logs
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Get root dir
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


class Config(object):
    ROOT_DIR = ROOT_DIR
    DATA_DIR = os.path.join(ROOT_DIR, 'data')
    RESULTS_DIR = os.path.join(ROOT_DIR, 'results')
    mapbox_token = 'pk.eyJ1Ijoic3B3aGl0ZTEzMzciLCJhIjoiY2ppc3g5Yms0MWxsczNrdDk2cWx5Y3h5eSJ9.cyqzPXRz_Y_382m-tZqIIA'
    CLOUD_DATA = 's3://scott-p-white/website/data'
