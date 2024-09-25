import pandas as pd

movie_data = {
    'Title': ['Inception', 'Avengers: Endgame', 'Interstellar', 'The Dark Knight', 'Lion King'],
    'Runtime': [148, 181, 169, 152, 154], 
    'Year': [2010, 2019, 2014, 2008, 1994]
}

df = pd.DataFrame(movie_data)
df_sorted = df.sort_values(by='Runtime', ascending=False)
print(df_sorted)
