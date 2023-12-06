# DAB 111 - Python Final Project

### Group Members:

Group No. 13

 - Jigar Donga - 0836668
 - Ayush Raj Saxena - 0832578
 - Shreyas Joshi - 0837922
 
### Project Objective:

This project contains the usage of Python, Pandas, SQLite3, and Flask. Using Pandas, we are reading data from dataset and stored in database using SQLite3 package. Flask is used to present stored data of database on web.
Website contains mainly 3 pages, Home, About Us, and Movies (data). About Us page shows the details about dataset and defination of each variable. Movies (data) page shows the data stored in database using SQLite3.

## Marvel Cinematic Universe (MCU) Movies Dataset

### Overview

The Marvel Cinematic Universe (MCU) Movies Dataset is a comprehensive collection of data related to the Marvel Studios' film franchise. The dataset covers movies released from 2008 onwards when the MCU was introduced. The information includes details such as movie phases, duration, release year, IMDB ratings, genre, cast, box office collections in different regions, rankings, CinemaScore, budget, director, producer, and more.

### Source of Data

The dataset is sourced from Kaggle and is named "mcu-movies-dataset."

**Link to Source:** [mcu-movies-dataset](https://www.kaggle.com/datasets/dalepeh/mcu-movies-dataset)

### Data Variables

- **Phase:** Phase of the movie
- **Film:** Name of the movie
- **Duration:** Duration of the movie
- **Year_Release:** Year when the movie was released
- **IMDB Rating:** IMDB rating of the movie
- **Genre:** Type of movie (comedy, action, etc.)
- **Cast:** Actor and actress who worked in the movie
- **U.S. Release Date:** Release date in the U.S.
- **Box Office Gross U.S. and Canada:** Box office collection in the U.S. and Canada
- **Box Office Gross Other Territories:** Box office collection in other territories
- **Box Office Gross Worldwide:** Box office collection worldwide
- **All-Time Ranking U.S. and Canada:** Ranking of the movie in the U.S. and Canada
- **All-Time Ranking Worldwide:** Ranking of the movie worldwide
- **Rotten Tomatoes Rating:** Rating given by Rotten Tomatoes
- **CinemaScore:** CinemaScore of the movie
- **Budget:** Budget of the movie
- **Director:** Director of the movie
- **Producer:** Producer of the movie
- **Movie Image:** Poster of the movie (URL)

### Marvel Phases

Marvel Studios releases its films in groups called "Phases." The first three phases are collectively known as "The Infinity Saga," and the following three phases as "The Multiverse Saga."

## Example Usage
 Download required modules first:

 - Run command "pip install -r requirements.txt"
 - This will install all required packages for this project

 Run app Locally:

 (Follow first 2 steps if you not see 'MCU_Data.csv' or 'MCU.db' file in root directory)
 - If you not see 'MCU_Data.csv' file in root directory, then open new terminal in 'data processing' folder
 - Run "python clean_data.py" command, this will clean up original file and generate new file called 'MCU_Data.csv'
 
 - If you not see 'MCU.db' file in root directory, then open new terminal in 'database' folder
 - Run "python build_db.py" command, this will create new database file, create a table and insert data from 'MCU_Data.csv' file
 
 - Open 'terminal' or 'cmd' in root directory of the project
 - Run "python app.py" command
 - Go to http://127.0.0.1:5000
 - And explore the website
