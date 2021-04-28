import os
import sys
from os import path
from pathlib import Path
from loguru import logger
import pandas as pd


cwd = os.getcwd()

config_directory = 'config'
config_directory_path = os.path.join(cwd, config_directory)
if not os.path.exists(config_directory_path):
    os.makedirs(config_directory_path)

cookies_directory = 'cookies'
cookies_directory_path = os.path.join(cwd, cookies_directory)
if not os.path.exists(cookies_directory_path):
    os.makedirs(cookies_directory_path)

seasons_directory = 'seasons'
seasons_directory_path = os.path.join(cwd, seasons_directory)
if not os.path.exists(seasons_directory_path):
    os.makedirs(seasons_directory_path)

# Config file
config_file = os.path.join(cwd, "config", "config.ini")

# Role Ratings Config
show_update_role_ratings_dialog = False
role_ratings_csv = os.path.join(cwd, "config", "role_ratings.csv")

# Bold Attributes Config
bold_attributes_csv = os.path.join(cwd, "config", "bold_attributes.csv")

# Grab recruits from one divison higher
higher_division_recruits = False

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        gdr_csv = f"{Path(sys._MEIPASS) / 'data' / 'gdr.csv'}"
else:
    gdr_csv = f"./data/gdr.csv"
logger.info(f"gdr.csv path is = {gdr_csv}")
wis_gd_df = pd.read_csv(gdr_csv, header=0, index_col=0)