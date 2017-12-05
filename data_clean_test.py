import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# remove the rows where the 'RespondentID' column is null
star_wars = pd.read_csv('C:\git\StarWars.csv',sep=',')
star_wars = star_wars[pd.notnull(star_wars['RespondentID'])]


#Convert the column 'Have you seen any of the 6 films in the Star Wars franchise?' and 'Do you consider
yes_no={'Yes':True,'No':False}
columns = ['Have you seen any of the 6 films in the Star Wars franchise?','Do you consider yourself to be a fan of the Star Wars film franchise?']
for col in columns:
    star_wars[col] = star_wars[col].map(yes_no)

#rename the columns
star_wars = star_wars.rename(columns={"Which of the following Star Wars films have you seen? Please select all that apply.":"seen_1",
                          "Unnamed: 4": "seen_2",
                          "Unnamed: 5": "seen_3",
                          "Unnamed: 6": "seen_4",
                          "Unnamed: 7": "seen_5",
                          "Unnamed: 8": "seen_6"
                          })

#Recont each film if the respondent had seen,and assign values with Boolean type
film_name = {"Star Wars: Episode I  The Phantom Menace":True,
             "Star Wars: Episode II  Attack of the Clones": True,
             "Star Wars: Episode III  Revenge of the Sith": True,
             "Star Wars: Episode IV  A New Hope": True,
             "Star Wars: Episode V The Empire Strikes Back": True,
             "Star Wars: Episode VI Return of the Jedi": True,
             np.nan:False
             }
for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(film_name)

star_wars.to_csv("C:\git\/result.txt",sep='\t')

# rename the columns and convert them to float type

star_wars = star_wars.rename(columns={
"Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1",
        "Unnamed: 10": "ranking_2",
        "Unnamed: 11": "ranking_3",
        "Unnamed: 12": "ranking_4",
        "Unnamed: 13": "ranking_5",
        "Unnamed: 14": "ranking_6"
})
star_wars.to_csv("C:\git\/aa.txt",sep="\t")

columns = ["ranking_1","ranking_2","ranking_3","ranking_4","ranking_5","ranking_6"]
for col in columns:
    star_wars[col] = star_wars[col].astype(float)

#compute the mean of each of the ranking columns
ser = star_wars[star_wars.columns[9:15]].mean()

plt.bar(range(6),ser)
#plt.show()

# compute the sum of each of the seen columns
# When we call methods like pandas.DataFrame.sum() or mean(), they treat Booleans like integers. They consider True a 1, and False a 0
seen_sum = star_wars[star_wars.columns[3:9]].sum()
plt.bar(range(6),seen_sum)
plt.show()

# split a dataframe into two groups

male = star_wars[star_wars["Gender"] == "Male"]
female = star_wars[star_wars["Gender"] == "Female"]

