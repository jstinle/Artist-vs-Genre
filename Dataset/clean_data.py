"""
Name: Kristen, Justin, and Jayden 

This file contains functions that will take in our data_w_spotify csv file and
clean it up. We will be computing data, removing and adding columns. 
"""

import pandas as pd

artist_success_pd = pd.read_csv("/Users/krxxsten/Artist-vs-Genre-1/Dataset/data_w_spotify.csv")


def catergorized_genre(artist_success_pd: pd.DataFrame) -> None:
    '''
    Takes in our dataframe and iterates through the list of genres of each artist name
    and makes a new column with the first genre index of their list. 
    '''
    

    if "genres" in artist_success_pd.columns:
        artist_success_pd["updated_genre"] = artist_success_pd["genres"].str.split(",").str[0]
        artist_success_pd.dropna(subset=["updated_genre"], inplace=True)
    artist_success_pd = artist_success_pd[artist_success_pd["updated_genre"] != []]
   
    return artist_success_pd

print(catergorized_genre(artist_success_pd))


def drop_columns(artist_success_pd: pd.DataFrame) -> None:
    '''
    Takes in our dataframe and drop the following columns; "id", "isdone", and "spotifyid".
    In order to narrow our dataframe to keeping data that supports our research questions, we
    will be deleting those columns.
    '''
    artist_success_pd = artist_success_pd.drop(columns= ["id", "isdone", "spotifyid", "genres"], axis= 1)
    return artist_success_pd
