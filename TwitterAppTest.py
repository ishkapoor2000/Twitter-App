# -*- coding: utf-8 -*-
"""
Created on Oct 5 17:06:18 2021

@author: KASHISH KAPOOR
"""

#importing libraries
from tkinter import *
from tkinter import ttk
import mysql.connector
import tweepyTwitterData

# Connecting to SQL databse
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "********************************",
    database = "testTwitter"
    )
mycursor = db.cursor()

# Setting up GUI Window
root = Tk()
root.title("Kashish's Twitter App")
root.geometry("500x500")

sampletweets = [
    ['Ram Mandir', 'Abhinav Prakash', 'Kejriwal first opposed Shri Ram Mandir in Ayodhya and later on did a tokenism of visiting the Janmbhoomi. These tac… https://t.co/FO4K1DDSTd', 62],
    ['Ram Mandir', 'ANI UP/Uttarakhand', 'Uttar Pradesh | CM Yogi Adityanath visits Hanuman Garhi Mandir and also offers prayers at Ram Lalla in Ayodhya. https://t.co/6xY4Ebtzcc', 63],
    ['Ram Mandir', 'Shehzad Jai Hind', '4) U turn on Mohalla clinics &amp; poly clinics \n5) U turn on Air pollution \n6) U turn on hospitals \n7) U turn on not t… https://t.co/AcKZQLyv6Q', 64],
    ['Ram Mandir', 'Dr. Rutvij Patel', "The plinth work at Shri Ram Janmabhoomi Mandir site is reaching it's final stage. \n\nजय श्री राम! https://t.co/SmHLxf3uTW", 65]
    ,['Manish Sisodia', 'Walter J. Lindner', 'Great meeting Delhi’s Deputy CM Manish Sisodia on occasion of signing MoU for teaching GER language in Delhi school… https://t.co/nlPq1oqtF4', 66]
    ,['Manish Sisodia', 'AajTak', "'जिसे गुजरात की शिक्षा अच्छी नहीं लगती वे राज्य छोड़कर जा सकते हैं', शिक्षा मंत्री जीतू वघानी का बयान \n#Gujarat… https://t.co/33MUglyLmC", 67]
    ,['Manish Sisodia', 'Shehzad Jai Hind', 'If today’s events are “murder attempt” then as per Manish Sisodia, then this violent protest by AAP where stones we… https://t.co/V7hDfbs0tb', 68]
    ,['Manish Sisodia', 'Ajit Datta', 'The Indian Express has brought out its list of most powerful Indians. Arvind Kejriwal is ranked 9, ahead of BL Sant… https://t.co/eah8pvO78m', 69]
    ,['Manish Sisodia', 'TIMES NOW', '#Breaking | "BJP attempted to kill Arvind Kejriwal", Delhi Dy CM Manish Sisodia makes a sensational claim https://t.co/i75I8DEULU', 70]
    ,['Manish Sisodia', 'ANI', 'Former Bengaluru Police Commissioner Bhaskar Rao joined Aam Aadmi Pary (AAP) today in the presence of Delhi Deputy… https://t.co/00CXi98Bpp', 71]
    ,['Manish Sisodia', 'ANI', 'Delhi | Tamil Nadu CM MK Stalin along with CM Arvind Kejriwal and Deputy CM Manish Sisodia visits Rajkiya Sarvodaya… https://t.co/ZdKthMUd6i', 72]
    ,['Manish Sisodia', 'Prashant Kumar', 'BIG BREAKING: Deputy CM Manish Sisodia levels a big allegation against the BJP, says the saffron party is planning… https://t.co/oQUxC93HrN', 73]
    ,['Manish Sisodia', 'Raju Bista', 'Deputy CM of Delhi Manish Sisodia labelled elected BJP MPs and BJYM karyakartas as "gundas" and alleged that BJP tr… https://t.co/10ELupA3Vh', 74]
    ,['Manish Sisodia', 'ANI', "BJP must remember that before 2011-12, the municipality was a single entity under BJP's rule; there used to be corr… https://t.co/GqBvOFuuZb", 75]
    ,['Manish Sisodia', 'TIMES NOW', '"Kejriwal must apologize for mocking Hindu sentiments ... This whole comment of Manish Sisodia that this was an ass… https://t.co/NAdzHgUd6W', 76]
    ,['Manish Sisodia', 'NDTV', '#Delhi | Former Bengaluru Police Commissioner Bhaskar Rao joined Aam Aadmi Pary (AAP) today in the presence of… https://t.co/MJfO4ianU1', 77]
    ,['Manish Sisodia', 'TIMES NOW', "'BJP is conspiring to assassinate Arvind Kejriwal...barriers were broken &amp; Delhi Police were mute spectators', says… https://t.co/H2NM7R2m4s", 78],
    ['Dulquer', 'Dulquer Salmaan', 'The story of sleep!! Here’s presenting to you the quirky teaser of Nanpakal Nerathu Mayakkam produced by Mammootty… https://t.co/aQlp1VOnuz', 79],
    ['Dulquer', 'Dulquer Salmaan', 'All the best for you new directorial @ash_r_dhanush ! Here’s #Yaathrakaaran everyone ! Do check it out __ https://t.co/X9YTBSv6pB', 80],
    ['Dulquer', 'Ralph Alex Arakal', 'Whilst @dulQuer is the latest to be under fire from theatre owners in #Kerala protesting OTT release of #Salute, th… https://t.co/pCXPW6mVTN', 81],
]

# saveButtonFunction()
def saveButtonFunction():
    """
    Saves data into SQL databse from Twitter API
    """
    clearData()
    query = entry1.get() # Get value of Input box as string
    if (query):
        srearchlabel['text'] = "Tweets related to " + query + " stored in SQL Database"
        twitterData = tweepyTwitterData.searchTweets(query=query) # Pass query
        if (twitterData): loadData(twitterData)
        print("Query: ", query)

# Create Entry box
entry1 = Entry(root, width = 25)
entry1.pack(pady=15, padx=50, fill=BOTH)

#Create Search button
srearchlabel = Label(root, text = "")
srearchlabel.pack()

# Create save button
saveButton = Button(root, text = 'Search', command = saveButtonFunction)
saveButton.pack(side = TOP, padx=100, fill=BOTH)

# Create an outer Frame for Table
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# Add scrollbar to Frame
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Add table inside frame
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

# Make columns in table
my_tree["columns"] = ("ID", "Username", "Tweet Text")

# Setup design of columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=25)
my_tree.column("Username", anchor=W, width=150)
my_tree.column("Tweet Text", anchor=W, width=300)

# Setup design of headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="No.", anchor=CENTER)
my_tree.heading("Username", text="Username", anchor=W)
my_tree.heading("Tweet Text", text="Tweet", anchor=W)

def clearData():
    """
    Clear the table to remove any error
    """
    for item in my_tree.get_children():
        my_tree.delete(item)

def removeRedundantData():
    """
    Remove Redundant data from SQL Databse
    """
    mycursor.execute("SELECT DISTINCT TweetText FROM SearchedTweets")
    db.commit()

def loadData(twitterData):
    """
    Load twitter data into SQL
    """
    for tweetsValue in twitterData:
        Query = tweetsValue[0]
        TweetText = tweetsValue[1]
        UserName = tweetsValue[2]
        mycursor.execute("INSERT INTO SearchedTweets (UserQuery, UserName, TweetText) VALUES (%s, %s, %s)", (Query, UserName, TweetText))

    db.commit() #make final SQL changes


def showData():
    """
    Take SQL data and show in table
    """
    clearData()
    mycursor.execute("SELECT * FROM SearchedTweets")
    for s in mycursor:
        query, username, tweet, index = s

    id = 0
    for text in sampletweets:
        my_tree.insert(parent='', index='end', iid=id, text="", values=(id, "@" + text[1], text[2]))
        id += 1


my_tree.pack(pady=20, padx=20, side=TOP, fill=BOTH)
tree_scroll.config(command = my_tree.yview)

# Create loading button
loadButton = Button(root, text = 'Load Data', command = showData)
loadButton.pack(side = TOP, padx=100, fill=BOTH)

# Mainloop runs the GUI
root.mainloop()