'''
Name: Jayden Set

This file contains functions that will answer the question
"Within a specific genre, which artists are the most popular on Spotify?"
It will be based off of our updated dataset "artist_success2.csv".
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('/Users/jset/Documents/Artist-vs-Genre/artist_success2.csv')
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



def find_most_popular_artists(df):
    '''
    Takes the dataframe containg the genre and popularity and finds the most
    popular artists. Returns only the artists that are the most popular.
    '''
    # Group the DataFrame by 'overall_genre' and find the maximum 'popularity' within each group
    max_popularity = df.groupby('overall_genre')['popularity'].max()
    # Filter the DataFrame to include only the rows where 'popularity' matches the maximum value within each group
    most_popular_artists = df[df['popularity'].isin(max_popularity)]
    return most_popular_artists


def plot_most_popular_artists(df):
    '''
    This will generate a bar plot showing the most popular artists within each genre, 
    with the artist names on the x-axis and their popularity scores on the y-axis.
    '''
    # Group the DataFrame by 'overall_genre' and find the maximum 'popularity' within each group
    max_popularity = df.groupby('overall_genre')['popularity'].max()
     # Filter the DataFrame to include only the rows where 'popularity' matches the maximum value within each group
    most_popular_artists = df[df['popularity'].isin(max_popularity)]
    # Plot the most popular artists
    plt.figure(figsize=(10, 6))
    plt.bar(most_popular_artists['name'], most_popular_artists['popularity'])
    plt.xlabel('Artist')
    plt.ylabel('Popularity')
    plt.title('Most Popular Artists in Each Genre')
    plt.xticks(rotation=45)
    plt.show()


most_popular_artists = find_most_popular_artists(df)

def main():
    print("Most popular artists by genre:", most_popular_artists)
    plot_most_popular_artists(df)
    

if __name__ == '__main__':
    main()
