# -*- coding: utf-8 -*-

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "****",
    database = "testTwitter"
    )
query = ""

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testTwitter")
# Add the `database = "SQLTest1"` in 'mysql.connector.connect', to connect to it specifically.

mycursor.execute("CREATE TABLE SearchedTweets (UserQuery VARCHAR(50) NOT NULL, UserName VARCHAR(50) NOT NULL, TweetText VARCHAR(280) NOT NULL, ID int PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("CREATE TABLE UserTweets (UserName VARCHAR(50) NOT NULL, TweetText VARCHAR(280) NOT NULL, ID int PRIMARY KEY AUTO_INCREMENT)")
db.commit()

mycursor.execute("SELECT * FROM SearchedTweets")
for s in mycursor:
    print(s)

mycursor.execute("SELECT * FROM UserTweets")
for u in mycursor:
    print(u)