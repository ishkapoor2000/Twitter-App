# -*- coding: utf-8 -*-
"""
Created on Oct 5 17:06:18 2021

@author: ISH KAPOOR
"""

# Importing libraries
from tkinter import *
from tkinter import ttk
import mysql.connector
import tweepyTwitterData

# Connecting to SQL databse
db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "**********",
	database = "testTwitter"
	)
mycursor = db.cursor()

# Setting up GUI Window
root = Tk()
root.title("Ish's Twitter App")
root.geometry("600x600")


# saveButtonFunction
def saveButtonFunction():
	# sourcery skip: use-fstring-for-concatenation, use-named-expression
	"""
	Saves data into SQL databse from Twitter API
	"""
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
tree_scroll_y = Scrollbar(tree_frame)
tree_scroll_y.pack(side=RIGHT, fill=Y)

tree_scroll_x = Scrollbar(tree_frame)
tree_scroll_x.pack(side=BOTTOM, fill=X)

# Add table inside frame
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)

# Make columns in table
my_tree["columns"] = ("ID", "Username", "Tweet Text")

# Setup design of columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=25)
my_tree.column("Username", anchor=W, width=150)
my_tree.column("Tweet Text", anchor=W, width=1000)

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


def loadData(twitterData):
	"""
	Load twitter data into SQL
	"""
	for tweetsValue in twitterData:
		Query, TweetText, UserName = tweetsValue
		mycursor.execute(
			'INSERT INTO SearchedTweets (UserQuery, UserName, TweetText) VALUES (%s, %s, %s)',
			(tweepyTwitterData.removeEmoji(Query), tweepyTwitterData.removeEmoji(UserName), tweepyTwitterData.removeEmoji(TweetText)),
		)

	db.commit() #make final SQL changes



def showData():
	"""
	Take SQL data and show in table
	"""
	clearData()
	mycursor.execute("SELECT * FROM SearchedTweets")
	for s in mycursor:
		print(s)
		_, username, tweet, index = s
		my_tree.insert(
			parent='',
			index='end',
			iid=index,
			text="",
			values=(index, f'@{tweepyTwitterData.removeEmoji(username)}', tweepyTwitterData.removeEmoji(tweet)),
		)


my_tree.pack(pady=20, padx=20, side=TOP, fill=BOTH)
tree_scroll_y.config(orient="vertical", command = my_tree.yview)
tree_scroll_x.config(orient="horizontal", command = my_tree.xview)

# Create loading button
loadButton = Button(root, text = 'Load Data', command = showData)
loadButton.pack(side = TOP, padx=100, fill=BOTH)

# Mainloop runs the GUI
root.mainloop()