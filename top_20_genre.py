'''
Name: Justin Le

This file contains functions that will be utilized to answer the following
question: "With wide ranges of genres and subgenres nowadays, what specific
genre(s) dominate the 20% percentile of artists' popularity on Spotify based
on our dataset?".
This will be based off of our updated dataset, "artist_success2.csv".
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('/Users/justinle/Documents/Artist-vs-Genre/artist_success2.csv')
df.dropna(subset="updated_genre", inplace=True)


def filtering_genre(df: pd.DataFrame) -> None:
    '''
    Takes in the dataframe and iterates through all the genres from the
    updated_genre column and creates a new column that lists each artists
    general genre.
    For example: if an artist genre contains "hip hop", it would be catogorized
    in the new column as "hip hop".
    '''
    for index, row in df.iterrows():
        if 'hip hop' in row['updated_genre']:
            df.at[index, 'overall_genre'] = 'hip hop'
        if 'pop' in row['updated_genre']:
            df.at[index, 'overall_genre'] = 'pop'
        if 'r&b' in row['updated_genre']:
            df.at[index, 'overall_genre'] = 'r&b'
        if 'rap' in row['updated_genre']:
            df.at[index, 'overall_genre'] = 'rap'
        if 'k-pop' in row['updated_genre']:
            df.at[index, 'overall_genre'] = 'k-pop'
        if 'edm' in row['updated_genre']:
            df.at[index, 'overall_genre'] = 'edm'

    df.dropna(subset="overall_genre", inplace=True)
    return df


def popularity_percentile(df: pd.DataFrame) -> float:
    """
    Takes in the DataFrame containing the column "popularity"
    then calculating the 20th percentile of popularity among artists
    in the given DataFrame. Returning a float represnting this percentile.
    """
    popularity_20th_percentile = np.percentile(df['popularity'], 20)
    return popularity_20th_percentile


def get_genres_in_percentile(df: pd.DataFrame,
                             popularity_percentile: float) -> list:
    """
    Takes the DataFrame containing popularity and genre columns and
    popularity_percentile, the percentile value to filter the artists.
    Then filtering the artists whose popularity falls within the given
    percentile and returns the unique genres of those artists as a list.
    """
    filtered_df = df[df['popularity'] <= popularity_percentile]
    genres = filtered_df['updated_genre'].unique()
    return genres


def dominant_genres(df: pd.DataFrame) -> list:
    """
    Takes the DataFrame containing the genre column and finds
    the most dominant genre in the DataFrame by counting the occurrences
    of each genre and returning the genre with the highest count
    from the top 20 percent of artists based on popularity.
    """
    popularity_20th_percentile = df['popularity'].quantile(0.2)
    top_artists_df = df[df['popularity'] >= popularity_20th_percentile]
    genre_counts = top_artists_df['updated_genre'].value_counts()
    max_count = genre_counts.max()
    dominant_genres = genre_counts[genre_counts == max_count].index.tolist()
    return dominant_genres


percentile = popularity_percentile(df)
genres_percentile = get_genres_in_percentile(df, percentile)
dominant_genres = dominant_genres(df)


print("Most dominant genre:")
print(dominant_genres)
