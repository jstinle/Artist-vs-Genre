"""
Name: Kristen, Justin, and Jayden 

This file contains functions that will take in our data_w_spotify csv file and
clean it up. We will be computing data, removing and adding columns. 
"""

import pandas as pd 
import geopandas as gpd 

artist_success_pd = pd.read_csv("/home/data_w_spotify.csv")