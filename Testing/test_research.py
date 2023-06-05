'''
Name: Kristen Do, Jayden Set, and Justin Le

This file tests the functions within the file
genre_vs_follower.py, top_20_genre.py, most_popular.py.
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import Research.genre_vs_follower as genre_vs_follower
import Research.top_20_genre as top_20_genre
import Research.most_popular as most_popular


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


def test_dominant_genres_count(df: pd.DataFrame) -> None:
    '''
    From the top_20_genre.py file, tests the
    dominant_genres_count function using a generated
    DataFrame of smaller data.
    '''
    df = pd.DataFrame({
        'name': ['Drake', 'Adele', 'Taylor Swift',
                 'Kendrick Lamar', 'Lady Gaga'],
        'popularity': [98.0, 95.0, 92.0, 89.0, 85.0],
        'followers': [61377383.0, 48193976.0, 155433752.0,
                      17051599.0, 45418447.0],
        'updated_genre': ['canadian hip hop', 'pop', 'pop', 'hip hop', 'pop']
    })
    result = top_20_genre.dominant_genres_count(df)
    expected_output = ['pop']
    assert result == expected_output
    print("test dominant genres count passed")


def test_dominant_genres_score(df: pd.DataFrame) -> None:
    '''
    From the top_20_genre.py file, tests the
    dominant_genres_score function using a generated
    DataFrame of smaller data.
    '''
    df = pd.DataFrame({
        'name': ['Drake', 'Adele', 'Taylor Swift',
                 'Kendrick Lamar', 'Lady Gaga'],
        'popularity': [100.0, 95.0, 92.0, 89.0, 85.0],
        'followers': [61377383.0, 48193976.0, 155433752.0,
                      17051599.0, 45418447.0],
        'updated_genre': ['canadian hip hop', 'pop', 'pop', 'hip hop', 'pop']
    })
    result = top_20_genre.dominant_genres_score(df)
    expected_output = ['canadian hip hop']
    assert result == expected_output
    print("test dominant genres score passed")


def test_popular_artists(df: pd.DataFrame) -> None:
    '''
    From the most_popular.py file, tests the
    find_most_popular_artists function using a
    smaller dataframe.
    '''
    df = pd.DataFrame({
        'name': ['Drake', 'The Weeknd', 'Taylor Swift', 'BTS', 'Kanye West',
                 'Juice WRLD', 'Kygo'],
        'popularity': [98.0, 98.0, 98.0, 96.0, 95.0, 95.0, 84.0],
        'overall_genre': ['hip hop', 'r&b', 'pop', 'k-pop', 'rap', 'rap',
                          'edm']
    })
    result = most_popular.popular_artists(df)
    expected_output = ['BTS']
    assert result == expected_output
    print("test popular artist passed")


def test_plot_followers_popularity(df: pd.DataFrame) -> None:
    '''
    From the most_popular.py file, tests the
    plot_followers_popularity function using a
    smaller dataframe.
    '''
    genres = most_popular.most_popular_artists_plot['overall_genre'].unique()
    num_genres = len(genres)
    cmap = plt.get_cmap('tab10')

    plt.figure(figsize=(8, 6))

    for i, genre in enumerate(genres):
        genre_data = most_popular.most_popular_artists_plot
        [most_popular.most_popular_artists_plot['overall_genre'] == genre]
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


def test_plot_artist_popularity_genre(df: pd.DataFrame) -> None:
    '''
    From the most_popular.py file, tests the
    plot_artist_popularity_genre function using a
    smaller dataframe.
    '''
    most_popular_artists = most_popular.find_most_popular_artists_plot(df)
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
    plt.savefig('artist_popularity_genre.png')
    plt.show()


def main():
    test_df = '/Users/krxxsten/Artist-vs-Genre-1/test_data.csv'
    test: pd.DataFrame = pd.read_csv(test_df)
    test_func_follower_genre(test)
    test_plot_avg_followers(test)
    test_dominant_genres_count()
    test_dominant_genres_score()
    test_popular_artists()
    test_plot_followers_popularity(test)
    test_plot_artist_popularity_genre(test)


if __name__ == "__main__":
    main()
