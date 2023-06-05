# Booming Music Industry: Popularity of Artist vs Genre on Spotify
## CSE 163 Artist-vs-Genre
As avid music listeners, it has always been a thought of how the artists we listen to came about in fame. Among the boom in the music industry over the last few decades, certain genres have risen in popularity. In correlation with the boom, demand, and popularity for these certain genres; would a music artist's success depend on it? These are intriguing questions we are trying to understand in the interest of how we have come to listen to the songs we do in correlation to the popularity of its genre. With this in mind, we decided to analyze our research question through a popular streaming platform; Spotify. Spotify, a commonly used streaming platform will provide us data in regards to our research questions. By answering these questions we are able to further understand the trends in music genres and success it would bring about for music artists.

## For our dataset:
- Our main dataset can be found under the "Dataset" file as "data_w_spotify.csv", which includes data that analyzes the popularity of artists across the Spotify platform and is used to predict an artist's success on Spotify. This data includes features such as the artist's name, genre, popularity, number of followers, and release history.
- We wranggled and cleaned our data within the file "clean_data.py" found under the "Dataset" file in our directory. In this file, we downsized the orignal dataset by eliminating uncessecary columns, NA/NAN values, and adding a column that gives the general catergorized genre for each artist. This file transfers to a csv file, which we will utilize for our functions. 
- The file "Artist_success2.csv" is the result of our cleaning and wranggling from our "clean_data.py". And is the primary csv file used within the rest of our files. 
## For the Research files:
- The data utilized within these files will be found under the "Dataset" file as "Artist_success2.csv". 
- There are three main files, which each focus on one of our research
questions. These files are "genre_vs_follower.py", "top_20_genre.py", and "most_popular.py". Each can be ran to filter and plot data visualizations. 
- These visualizations are saved as a png file into our directory, but ones we have already generated can be found under the file "Plot images" in the directory.
- No new libraries are needed for this module, as all of them are included within each research file. 

## For testing files:
- We created one individual testing file that tests functions across all three of our research files. This can be found within our directory under the file "Testing".
- We test our functions using a smaller 80/20 sample of our dataset, in which we created a seperate duplicate csv file of "Artist_success2.csv" in order for us to be able to manipulate it. This new testing data can be found under the same testing file as "test_data.csv". 
- Our testing file generates testing data visualizations which are saved as a png and saved directly into our directory. However, testing images we already created can be found under our "Testing" file within our directory. 

## Running our files:
In order to run desired .py files, it must be taken out of the file. Using platforms such as, VSCODE requires all files to be in within the direct directory for the code to run from one file to another. Though, even considering this, we put our work into files for organizing purposes. 