# Twitter-App
This project is an App that fetches searched data from Twitter and saves it in SQL, that data can be graphically displayed on GUI.

* ### TwitterApp.py
This file runs a GUI that has an input field. User can enter query in that field. We access Twitter API function from tweepyTwitterdata.py file. The data from Twitter is based on the Query entered using Search Button. All the twitter data is stored in SQL database. The data in SQL database is loaded on the GUI using Load Button. The Table is scrollable and user interface is good. The redundant data is also removed.

* ### tweepyTwitterData.py
This file fetches data from Twitter API using Tweepy library. API authentication passwords are used to access the Twitter data. The API data is fetched based on Query. The returned data is a list of Tweets that have query-word in them. The data is sent to main file to be stored in SQL Data. Add relevant passwords.

* ### SetupFle.py
This file should be run once you clone this repository. Uncomment everything and add relevant passwords. This file creates basic SQL Databse setup for the user to smoothly use the app.
