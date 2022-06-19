import os, sqlite3

os.mkdir("images")

con = sqlite3.connect('cipher_fireemblem.db')

cur.execute("""CREATE TABLE skill (
                ID varchar(15)NOT NULL,
                skill varchar(255)
            );""")

cur.execute("""CREATE TABLE affinities (
                ID varchar(15)NOT NULL,
                affinities varchar(255)

            );""")