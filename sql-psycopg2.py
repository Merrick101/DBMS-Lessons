import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database 
cursor = connection.cursor()

# Query 1 - select all records from the "Artists" table
cursor.execute('SELECT * FROM "Artist"')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print the results
for result in results:
    print(result)