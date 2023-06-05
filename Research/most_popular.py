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


def popular_artists(df: pd.DataFrame) -> list:
    '''
    Takes the dataframe and only returns genre,
    the artist, and their popularity.
    '''
    df2 = filtering_genre(df)
    max_pop = df2.groupby('overall_genre')['popularity'].transform(max)
    most_pop = df[df['popularity'] == max_pop]
    most_pop = most_pop[['name', 'popularity', 'overall_genre']]
    return most_pop


def find_most_popular_artists_plot(df: pd.DataFrame) -> list:
    '''
    Takes the dataframe containg the genre and popularity and finds the most
    popular artists. Returns only the artists that are the most
    popular within each selected genre.
    popular within each selected genre along with their followers and subgenre.
    Used for the plots below.
    '''
    df2 = filtering_genre(df)
    max_popularity = df2.groupby('overall_genre')['popularity'].transform(max)
    most_popular_artists_plot = df[df['popularity'] == max_popularity]
    return most_popular_artists_plot


def plot_followers_popularity(df: pd.DataFrame) -> None:
    '''
    Scatter plot that represents the correlation between how much
    followers an artist has and there popularity
    '''
    genres = most_popular_artists_plot['overall_genre'].unique()
    num_genres = len(genres)
    cmap = plt.get_cmap('tab10')

    plt.figure(figsize=(8, 6))

    for i, genre in enumerate(genres):
        genre_data = most_popular_artists_plot[most_popular_artists_plot
                                               ['overall_genre'] == genre]
        plt.scatter(genre_data['popularity'], genre_data['followers'],
                    color=cmap(i % num_genres), label=genre)

        for j, row in genre_data.iterrows():
            plt.text(row['popularity'], row['followers'], row['name'],
                     fontsize=8, verticalalignment='bottom')

    plt.xlabel('Popularity')
    plt.ylabel('Follower Count')
    plt.title('Popularity vs. Follower Count for Most Popular Artists')
    plt.legend()
    plt.savefig('artist_followers_popularity.png')
    plt.show()


def plot_artist_popularity_genre(df: pd.DataFrame) -> None:
    '''
    Bar chart that shows the artists and their popularity
    along with their genres
    '''
    most_popular_artists = find_most_popular_artists_plot(df)
    plt.figure(figsize=(10, 6))
    bars = plt.bar(most_popular_artists['name'], most_popular_artists
                   ['popularity'], color='skyblue')

    for i, bar in enumerate(bars):
        genre = most_popular_artists_plot.iloc[i]['overall_genre']
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 genre, ha='center', va='bottom', fontsize=8)

    plt.xlabel('Artist')
    plt.ylabel('Popularity')
    plt.title('Artist Popularity and Genre')
    plt.xticks(rotation=90)
    plt.savefig('artist_popularity_genre.png')
    plt.show()


most_popular_artists_plot = find_most_popular_artists_plot(df)
pop_artists = popular_artists(df)


def main():
    print("Most popular artists by genre:", pop_artists)
    plot_followers_popularity(df)
    plot_artist_popularity_genre(df)


if __name__ == '__main__':
    main()
