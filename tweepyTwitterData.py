# -*- coding: utf-8 -*-

import tweepy

consumerKey = "********************************"
consumerSecret = "********************************"
accessTokenKey = "********************************"
accessTokenSecret = "********************************"

auth = tweepy.OAuth1UserHandler(consumerKey, consumerSecret)
auth.set_access_token(accessTokenKey, accessTokenSecret)

api = tweepy.API(auth)

userAPI = api.user_timeline()


def getUserTweets():

	return [[i.text, i.user.name,] for i in userAPI]


def searchTweets(query, count=300):

    fetched_tweets = api.search_tweets(query, count=count, result_type="popular")

    return [[removeEmoji(query), removeEmoji(tweet.text, "€€€"), removeEmoji(tweet.user.name)] for tweet in fetched_tweets]
    # return [[query, tweet.text, tweet.user.name] for tweet in fetched_tweets]


def removeEmoji(text, alt=""):
    return (''.join([text[j] for j in range(len(text)) if ord(text[j]) in range(65536)]) + " {0}".format(alt)).replace("\n", " ")

tweets = searchTweets(query="Tinder")
userTweets = getUserTweets()