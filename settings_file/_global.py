import os

SETTINGS_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR,"data")
FUNCTIONS_DIR = os.path.join(ROOT_DIR,"functions")
TOKEN = DEBUG = os.getenv("TOKEN",False)