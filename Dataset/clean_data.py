"""
Name: Kristen, Justin, and Jayden

This file contains functions that will take in our data_w_spotify csv file and
clean it up. We will be computing data, removing and adding columns.
"""

import pandas as pd

csv = ("/Users/krxxsten/Artist-vs-Genre-1/Dataset/data_w_spotify.csv")
art_pd = pd.read_csv(csv)


def catergorized_genre(art_pd: pd.DataFrame) -> None:
    '''
    Takes in our dataframe and iterates through the list of genres of each
    artist name and makes a new column with the first genre index of
    their list.
    '''

    if "genres" in art_pd.columns:
        art_pd["genres"] = art_pd["genres"].str.strip("[]").str.replace("", "")
        art_pd["updated_genre"] = art_pd["genres"].str.split(",").str[0]
        art_pd.dropna(subset=["updated_genre"], inplace=True)

    return art_pd


def drop_columns(art_pd: pd.DataFrame) -> None:
    '''
    Takes in our dataframe and drop the following columns;
    "id", "isdone", and "spotifyid". In order to narrow our dataframe
    to keeping data that supports our research questions, we will be deleting
    those columns.
    '''
    df2 = catergorized_genre(art_pd)
    art_pd = df2.drop(columns=[
                                  "id",
                                  "isdone",
                                  "spotifyid",
                                  "genres"], axis=1)

    return art_pd


def transfer_to_csv(art_pd: pd.DataFrame) -> None:
    '''
    Takes in our dataframe and combines the two data wrangling functions and
    transfers it into a new csv file with the updated data.
    '''
    genre = catergorized_genre(art_pd)
    dropped = drop_columns(genre)

    return dropped.to_csv('artist_success2.csv', index=False)


def main():
    transfer_to_csv(art_pd)


if __name__ == '__main__':
    main()
