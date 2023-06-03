'''
Name: Jayden Set


This file contains functions that will answer the question
"Within a specific genre, which artists are the most popular on Spotify?"
It will be based off of our updated dataset "artist_success2.csv".
'''


import pandas as pd
import matplotlib.pyplot as plt


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


def find_most_popular_artists(df: pd.DataFrame) -> list:
    '''
    Takes the dataframe containg the genre and popularity and finds the most
    popular artists. Returns only the artists that are the most
    popular within each selected genre.
    '''
    df2 = filtering_genre(df)
    max_popularity = df2.groupby('overall_genre')['popularity'].transform(max)
    most_popular_artists = df[df['popularity'] == max_popularity]
    return most_popular_artists


def plot_followers_popularity(df: pd.DataFrame) -> None:
    '''
    Scatter plot that represents the correlation between how much
    followers and artist has and there popularity
    '''
    plt.scatter(most_popular_artists['popularity'], most_popular_artists
                ['followers'])
    plt.xlabel('Popularity')
    plt.ylabel('Follower Count')
    plt.title('Popularity vs. Follower Count for Most Popular Artists')

    for i, row in most_popular_artists.iterrows():
        plt.text(row['popularity'], row['followers'], row['name'],
                 fontsize=8, verticalalignment='bottom')

    plt.show()


def plot_artist_popularity_genre(df: pd.DataFrame) -> None:
    '''
    Bar chart that shows the artists and their popularity
    '''
    most_popular_artists = find_most_popular_artists(df)
    plt.figure(figsize=(10, 6))
    bars = plt.bar(most_popular_artists['name'], most_popular_artists
                   ['popularity'], color='skyblue')
    for i, bar in enumerate(bars):
        genre = most_popular_artists.iloc[i]['overall_genre']
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 genre, ha='center', va='bottom', fontsize=8)
    plt.xlabel('Artist')
    plt.ylabel('Popularity')
    plt.title('Artist Popularity and Genre')
    plt.xticks(rotation=90)
    plt.show()


most_popular_artists = find_most_popular_artists(df)


def main():
    print("Most popular artists by genre:", most_popular_artists)
    plot_followers_popularity(df)
    plot_artist_popularity_genre(df)


if __name__ == '__main__':
    main()
