# MOVIE-ANALYSIS-IMDB

# STEPS
1. Connect your database (or create a connection) -> sqlite3.connect(database_name)
2. Use the cursor function -> database_variable.cursor()


# Workflow
1. You need to establish a connection to the SQLite database by creating a Connection object
2. Then, you have to create a Cursor object using the cursor() method
3. Then, excute the query -> cursor_object.execute('query')
4. To fetch the data, then use fetchall() method of the cursor object
