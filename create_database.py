import os, sqlite3

os.mkdir("images")

con = sqlite3.connect('cipher_fireemblem.db')

cur = con.cursor()

cur.execute("""CREATE TABLE card (
                ID varchar(20)NOT NULL,
                name varchar(55) NOT NULL,
                imageurl varchar(255),
                class varchar(255),
                cost varchar(255),
                symbol1 varchar(100),
                symbol2 varchar(100),
                attack int,
                suppport int,
                range int,
                quote varchar(500),
                illustrator varchar(60),
                comment varchar(500),

                PRIMARY KEY (ID)
            );""")


cur.execute("""CREATE TABLE skill (
                ID varchar(15)NOT NULL,
                skill varchar(255)
            );""")

cur.execute("""CREATE TABLE affinities (
                ID varchar(15)NOT NULL,
                affinities varchar(255)

            );""")