'''
Name: Kristen Do

This file contains functions that will be utilized to answer the following
"What is the relationship between music genre and the number of followers
on Spotify?". This will be based off of our updated dataset,
"artist_success2.csv".
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Dataset/artist_success2.csv")
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


def avg_genre_follower(df: pd.DataFrame) -> float:
    '''
    Takes in the dataframe and computes the average following
    for each genre.
    '''
    df2 = filtering_genre(df)
    avg = df2.groupby('overall_genre')['followers'].mean()
    return avg


def plot_follower_genre(df: pd.DataFrame) -> None:
    '''
    Takes in the dataframe and on one general plots, there will be
    4 subplots of the following trends for each catogorized genres.
    And saves the figure as a png called 'genre_vs_follower.png'.
    '''
    data = filtering_genre(df)
    grouped_df = data.groupby('overall_genre')
    line_colors = ['red', 'blue', 'green', 'orange', 'purple']
    num_subplots = len(grouped_df)

    fig, axs = plt.subplots(num_subplots, figsize=(10, 2 * num_subplots))
    fig.suptitle('Follower Count by Categorized Genre', fontsize=16)

    for i, (genre, group) in enumerate(grouped_df):
        if num_subplots > 1:
            ax = axs[i]
        else:
            ax = axs

        line_color = line_colors[i % len(line_colors)]
        ax.plot(group['followers'], color=line_color)
        ax.set_title(genre)
        ax.set_xlabel('Data Point')
        ax.set_ylabel('Follower Count')
        ax.grid(True)

    plt.tight_layout()
    plt.savefig('genre_vs_follower.png')
    plt.show()


def plot_avg_followers(df: pd.DataFrame) -> None:
    '''
    Takes in the dataframe and one one plot, plots a barchart
    of each genre and its average following count; computed from
    the avg_genre_following function. It saves the plot as a png called
    'genre_avg_follower.png'
    '''
    data = avg_genre_follower(df)
    num_genres = len(data)
    color_palette = sns.color_palette('Set2', num_genres)

    plt.figure(figsize=(10, 6))
    plt.bar(data.index, data.values, color=color_palette)
    plt.title('Average Follower Count by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Average Follower Count')
    plt.tight_layout()
    plt.savefig('genre_avg_follower.png')
    plt.show()


def main():
    print("Average following count per genre:", avg_genre_follower(df))
    plot_follower_genre(df)
    plot_avg_followers(df)


if __name__ == '__main__':
    main()
