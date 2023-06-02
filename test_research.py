'''
Name: Kristen Do, Jayden Set, and Justin Le

This file tests the functions within the file
genre_vs_follower.py, top_20_genre.py, most_popular.py. 
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import genre_vs_follower
import top_20_genre
import most_popular



df = pd.read_csv('/Users/krxxsten/Artist-vs-Genre-1/artist_success2.csv')
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
train_df.to_csv('train_data.csv', index=False)
test_df.to_csv('test_data.csv', index=False)

def test_func_follower_genre(df: pd.DataFrame) -> None:
    '''
    Tests the plot_follower_genre within the genre_vs_follower.py
    file using a smaller testing file of our csv data.
    '''
    data = genre_vs_follower.filtering_genre(df)
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
    plt.savefig('test_genre_vs_follower.png')
    plt.show()


def test_plot_avg_followers(df: pd.DataFrame) -> None:
    '''
    From the genre_vs_follower.py file, tests the
    plot_avg_followers function using a smaller testing
    file of our csv data.
    '''
    data = genre_vs_follower.avg_genre_follower(df)
    num_genres = len(data)
    color_palette = sns.color_palette('Set2', num_genres)

    plt.figure(figsize=(10, 6))
    plt.bar(data.index, data.values, color=color_palette)
    plt.title('Average Follower Count by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Average Follower Count')
    plt.tight_layout()
    plt.savefig('test_genre_avg_follower.png')
    plt.show()


def main():
    test_df = '/Users/krxxsten/Artist-vs-Genre-1/test_data.csv'
    test: pd.DataFrame = pd.read_csv(test_df)
    test_func_follower_genre(test)
    test_plot_avg_followers(test)


if __name__ == "__main__":
    main()