import pandas as pd

movies = pd.read_csv('../MCU_Data_Orign.csv')
movies_orign = movies.copy(deep=True)

# Convering values in million
movies['Box office gross U.S. and Canada (Million $)'] = (movies['Box office gross U.S. and Canada'] / 1000000).round(2)
movies['Box office gross Other territories (Million $)'] = (movies['Box office gross Other territories'] / 1000000).round(2)
movies['Box office gross Worldwide (Million $)'] = (movies['Box office gross Worldwide'] / 1000000).round(2)
movies['Budget (Million $)'] = (movies['Budget'] / 1000000).round(2)

# Update the value of CinemaScore column
movies['CinemaScore'] = movies['CinemaScore'].replace('A_', 'A-')

# Drop unnecessary columns
movies.drop(['Box office gross U.S. and Canada', 'Box office gross Other territories', 'Box office gross Worldwide', 'Budget'], axis=1, inplace=True)

# Generate new CSV file after  cleaning the dataset
movies.to_csv('../MCU_Data.csv', index=False)