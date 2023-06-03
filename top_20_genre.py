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


def dominant_genres_count(df: pd.DataFrame) -> list:
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
    dominant_genres_count = genre_counts[genre_counts ==
                                         max_count].index.tolist()
    return dominant_genres_count


def dominant_genres_score(df: pd.DataFrame) -> list:
    """
    Takes the DataFrame containing the genre column and finds
    the most dominant genre in the DataFrame by calculating the
    average popularity score for each genre and returning the
    genre with the highest average from the top 20 percent
    of artists based on popularity.
    """
    popularity_20th_percentile = df['popularity'].quantile(0.2)
    top_artists = df[df['popularity'] >= popularity_20th_percentile]
    avg_popularity = top_artists.groupby('updated_genre')['popularity'].mean()
    max_avg_popularity = avg_popularity.max()
    dominant_genres_score = avg_popularity[avg_popularity ==
                                           max_avg_popularity].index.tolist()
    return dominant_genres_score


dominant_genres_c = dominant_genres_count(df)
dominant_genres_s = dominant_genres_score(df)


def main():
    print("Most dominant genre by count:", dominant_genres_c)
    print("Most dominant genre by popularity score", dominant_genres_s)


if __name__ == '__main__':
    main()
