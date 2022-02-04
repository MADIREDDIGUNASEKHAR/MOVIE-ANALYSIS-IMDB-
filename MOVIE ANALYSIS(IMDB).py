#!/usr/bin/env python
# coding: utf-8

# # Dataset: '/content/drive/MyDrive/Datasets/movies.sqlite'

# # Importing the libraries

# In[1]:


# NumPy -> To perform the Mathematical operations
import numpy as np

# Pandas -> Data Manipulation tool
import pandas as pd

# Matplotlib -> Data Visualisation tool
import matplotlib.pyplot as plt

# Seaborn -> Data Visualisation tool
import seaborn as sns

# SQLite -> Server-less Database
import sqlite3


# 1. Establishing the connection to the database

# In[ ]:


db = '/content/drive/MyDrive/Datasets/movies.sqlite'
conn = sqlite3.connect(db)
cur = conn.cursor()


# 2. Get all the data about movies?

# In[ ]:


# Fetching the data of the Movies table from the Database
cur.execute("SELECT * FROM movies")
# Creating the cursor object
movies = cur.fetchall()


# In[ ]:


# Displaying the database data
movies


# In[ ]:


# Creating a DataFrame
movies = pd.DataFrame(movies,columns=['id', 'original_title', 'budget', 'popularity',
                                  'release_date', 'revenue', 'title', 'vote_average',
                                  'vote_count', 'overview', 'tagline','uid',
                                  'director_id'] )


# In[ ]:


# Displaying the DataFrame
movies


# In[ ]:


df.info()


# 3. Get all the data about directors?

# In[ ]:


# Fetching the data of the Director table from the Database
cur.execute("SELECT * FROM directors")
# Creating the cursor object
directors = cur.fetchall()


# In[ ]:


directors


# In[ ]:


directors = pd.DataFrame(directors,columns=['name', 'id', 'gender', 'uid',
                                  'department'] )


# In[ ]:


directors


# In[ ]:


directors.info()


# 4. Check how many movies are present in the IMDB table

# In[ ]:


cur.execute('SELECT COUNT(Title) FROM movies')
count = cur.fetchall()
print(f"The number of movies present in the IMDB databse is {count[0]}")


# 5. Find these 3 directors: James Cameron, Luc Besson, John Woo

# In[ ]:


cur.execute("SELECT * FROM directors WHERE name IN ('James Cameron','Luc Besson', 'John Woo')")
cur.execute("SELECT * FROM directors WHERE name =='James Cameron' or name =='Luc Besson' or name == 'John Woo'")
three_directors = cur.fetchall()
print(f"Theses 3 Directors data are: {three_directors}")


# 6. Find all the directors with name starting with 'Steven'

# In[ ]:


cur.execute('SELECT * FROM directors WHERE name LIKE "Steven%"')
name_like = cur.fetchall()
print(f"The directors whose names are starting with the word 'Steven' are: {name_like}")


# 7. Count the Female directors

# In[ ]:


cur.execute("SELECT COUNT(*) FROM directors WHERE gender == '1'")
females = cur.fetchall()
print(f"The number of female directors is {females[0][0]}")


# 8. Find the name of the 10th first women directors

# In[ ]:


cur.execute('SELECT name FROM directors WHERE gender==1')
tenth = cur.fetchall()
print(f"The tenth first women is {tenth[9][0]}")


# 9. What are the 3 most popular movies?

# In[ ]:


cur.execute('SELECT title FROM movies ORDER BY popularity DESC LIMIT 3 ')
most_popular = cur.fetchall()
print(f"The 3 mostpopular movies are: {most_popular[0][0]}, {most_popular[1][0]} and {most_popular[2][0]}")


# 10. What are the 3 most bankable movies?

# In[ ]:


cur.execute('SELECT title FROM movies ORDER BY budget DESC LIMIT 3')
most_bankable = cur.fetchall()
most_bankable
print(f"The three most bankable movies are {most_bankable[0][0]}, {most_bankable[1][0]} and {most_bankable[2][0]}")


# 11. What is the most awarded average rated movie since the Jan 1st, 2000?

# In[ ]:


cur.execute("SELECT Original_title FROM movies WHERE Release_date	 > '2000-01-01' ORDER BY vote_average DESC LIMIT 1")
most_awarded_avg = cur.fetchall()
print(f"The most awarded average rated movie is {most_awarded_avg[0][0]}")


# 12. Which movie(s) were directed by Brenda Chapman?

# In[ ]:


cur.execute("SELECT original_title FROM movies JOIN directors ON directors.id = movies.director_id WHERE directors.name = 'Brenda Chapman'")
directed_by = cur.fetchall()
print(f"The movie(s) directed by Brenda Chapman is {directed_by[0][0]}")


# 13. Name the director who has made the most movies?

# In[ ]:


cur.execute("SELECT name FROM directors JOIN movies ON directors.id = movies.director_id GROUP BY director_id ORDER BY COUNT(name) DESC limit 1")
director_movie = cur.fetchall()
print(f"The director who made the most movies is {director_movie[0][0]}")


# 14. Name of the director who is most bankable

# In[ ]:


cur.execute("SELECT name FROM directors JOIN movies ON directors.id = movies.director_id GROUP BY director_id ORDER BY SUM(budget) DESC limit 1")
most_bankable = cur.fetchall()
print(f'The most bankable director is {most_bankable[0][0]}')


# # Budget Analysis

# 1. Tell the Top 10 highest budget making movie

# In[ ]:


movies.columns


# In[ ]:


cur.execute('Select * FROM movies ORDER BY budget DESC LIMIT 10')
top_10 = cur.fetchall()
most_popular = pd.DataFrame(top_10, columns=['id', 'original_title', 'budget', 'popularity', 'release_date',
       'revenue', 'title', 'vote_average', 'vote_count', 'overview', 'tagline',
       'uid', 'director_id'])
most_popular


# # Revenue Analysis

# 1. Find Top 10 Revenue making movies

# In[ ]:


cur.execute("SELECT * FROM movies ORDER BY revenue DESC LIMIT 10")
top10_movies = cur.fetchall()
most_revenue = pd.DataFrame(top10_movies,  columns= ['id','original_title','budget','popularity','release_date',
                                    'revenue', 'title','vote_average','vote_count','overview',
                                    'tagline','uid','director_id'])
most_revenue


# # Voting Analysis

# 1. Find the most popular movies with highest vote_average

# In[ ]:


cur.execute(("SELECT * FROM movies ORDER BY vote_average DESC LIMIT 10"))
most_pop = cur.fetchall() 
most_popular_movie = pd.DataFrame(most_pop,columns =['id', 'original_title', 'budget', 'popularity', 'release_date',
       'revenue', 'title', 'vote_average', 'vote_count', 'overview', 'tagline',
       'uid', 'director_id'])
most_popular_movie


# # Director Analysis

# 1. Name all the directors with the number of movies and revenue where Revenue should be taken into account for doing the analysis. The director who has the highest revenue should comes at the top and so on and so forth.

# In[ ]:


cur.execute("SELECT name,COUNT(*) AS 'Total Movies',SUM(revenue) AS 'Total Revenue' FROM  directors JOIN movies WHERE directors.id==movies.director_id GROUP BY director_id ORDER BY SUM(revenue) DESC")
director_revenue=cur.fetchall()
director_most_revenue=pd.DataFrame(director_revenue,columns=['Director_Name','Total Movies','Total Revenue'])
director_most_revenue.head(10)


# 2. Name all the directors with the number of movies and revenue where number of movies should be taken into account for doing the analysis. The director who has the highest number of movies should comes at the top and so on and so forth.

# In[ ]:


cur.execute("SELECT name, COUNT(title), SUM(revenue) FROM directors JOIN movies ON movies.director_id = directors.id GROUP by director_id ORDER BY  COUNT(title) DESC LIMIT 10")
director_movies = cur.fetchall()
director_most_movies = pd.DataFrame(director_movies,columns=['name','no_of_title','revenue'])
director_most_movies


# 3. Give the Title of the movie, realease_date, budget, revenue, popularity and vote_average made by Steven Spielberg

# In[ ]:


cur.execute("SELECT title, release_date,budget,revenue,popularity,vote_average FROM directors JOIN movies ON directors.id==movies.director_id WHERE directors.name=='Steven Spielberg'")
movies_list=cur.fetchall()
movies_list_Steven_Spielberg=pd.DataFrame(movies_list,columns=['Movie_Name','Release_Date','Total Budget','Total_Revenue','Popularity','Vote_Average'])
movies_list_Steven_Spielberg

