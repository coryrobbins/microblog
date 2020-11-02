import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c = execute("""DROP TABLE posts""")
    c = execute("""CREATE TABLE posts(title TEXT, decription TEXT)""")
    c = execute('INSERT INTO posts VALUES("Good,", I\'m good.")')
    c = execute('INSERT INTO posts VALUES("Well,", I\'m well.")')


"""
STOPPED AT VIDEO 4 - COULD NOT GET THE SQLITE3 TO WORK PROPERLY

"""

#TODO -----> finish the Tutorial
