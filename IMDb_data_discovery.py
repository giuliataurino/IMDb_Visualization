"""
Follow Instructions Here to Install Programs if needed:
    https://pypi.org/project/imdb-sqlite/
to get column names open database with 'sqlite trek' program (or similar):
    open tables, right click on tables and view schema

"""

import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


######## FILTERS ############
is_original_title = 1
genres = '"comedy"'

######## COLUMNS #############
columns = ("akas.title_id, akas.title, akas.region, akas.language, akas.types, " +
"akas.attributes, akas.is_original_title, titles.primary_title," + 
"titles.is_adult, titles.premiered, titles.ended," + 
"titles.runtime_minutes, titles.genres," +
"ratings.rating, ratings.votes")
limit = 1000000


query = ('SELECT distinct ' + str(columns).strip('()') + ''
' FROM akas'
' INNER JOIN titles ON akas.title_id = titles.title_id  '
' JOIN crew ON akas.title_id = crew.title_id  '
' JOIN ratings ON akas.title_id = ratings.title_id  '

' WHERE titles.genres like ' + str(genres) + ''
' AND akas.title = titles.primary_title'
' AND region NOT NULL'
' LIMIT ' + str(limit))

#' AND akas.is_original_title = ' + str(is_original_title) + ''

os.chdir(r"*insert path*")
######## CREATING CONNECTION ###############

 
 
conn = sqlite3.connect("imdb.db")
c = conn.cursor()

import sqlite3

# Connecting to the database file
sqlite_file = "imdb.db"    # name of the sqlite database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# 1) Contents of all columns for row that match a certain value in 1 column
c.execute(query)
all_rows = c.fetchall()
df = pd.DataFrame(all_rows)
names = list(map(lambda x: x[0], c.description))
df.columns = names
#print('1):', all_rows)

# Closing the connection to the database file
conn.close()

""" # GRAPHING CODE BELOW
### GRAPH SHAPE OF REVIEWS BY COUNTRY
df_rev_country = df[['title_id', 'region', 'rating', 'votes']]


#test test test
test_countries = ['US', 'IN', 'IT', 'CL', 'RS']
df_rev_country = df_rev_country[df_rev_country['region'].isin(test_countries)]
countries = list(set(df_rev_country['region'].values))

for country in countries:
    df_rev_country_temp = df_rev_country[df_rev_country['region']==country]
    
        # Draw the density plot
    sns.distplot(df_rev_country_temp['rating'], hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = country)
    
# Plot formatting
plt.legend(prop={'size': 16}, title = 'Countries')
plt.title('Density Plot with Multiple Countries')
plt.xlabel('Ratings')
plt.ylabel('Density')
"""
