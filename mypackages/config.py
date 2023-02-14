import os
import sys
from pathlib import Path
import pandas as pd
import platform

os_platform = platform.system()

version = "1.1.0"
application_name = "GD Recruit Assistant"
window_title = f"{application_name} ({version})"

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
role_ratings_df = pd.DataFrame()
role_ratings_df_hash = ""

# Bold Attributes Config
bold_attributes_csv = os.path.join(cwd, "config", "bold_attributes.csv")

# Grab recruits from one divison higher
higher_division_recruits = False

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    gdr_csv = f"{Path(sys._MEIPASS) / 'data' / 'gdr.csv'}"
    checkmarkicon = f"{Path(sys._MEIPASS) / 'images' / 'checkmark_1.png'}"
    x_icon = f"{Path(sys._MEIPASS) / 'images' / 'x_icon.png'}"
    
else:
    gdr_csv = f"./data/gdr.csv"
    checkmarkicon = f"./images/checkmark_1.png"
    x_icon = f"./images/x_icon.png"

wis_gd_df = pd.read_csv(gdr_csv, header=0, index_col=0)

rids_unsigned = []
rids_unsigned_length = 0
rids_all_length = 0
watchlist_length = 0
clear_model = False
season_filename = ""

main_url = "www.whatifsports.com"
#main_url = "wis-dev.shub.dog"