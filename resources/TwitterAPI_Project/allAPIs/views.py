from django.shortcuts import render,HttpResponse
import tweepy
import json
from tweepy import OAuthHandler

def retweet(request):
	consumer_key='LtUoLhvWzGOUODCpHkIW1cH7s'
	consumer_secret='o18cdHxf8YLgLaWJZZ8lMvcv2SACOAIJYZmZB5s7nxmPPHRgc3'

	access_token='984099024402894848-bTCwMxW8o04woXa6OAD2Y7PIoxy3TPb'
	access_token_secret='ENb06BGdQamMnFHaxqDeUFL8GzafGIylruSW0s3ubXgqs'

	#  get authorization from Twitter API using tweepy

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	#  get the values of the user, and the target

	#if 'user_id' in request.POST
	userid=request.POST['user_id']
	# block
	list=api.followers_ids(id=userid)

	return render(request,'followers_ids.html',{'list':list})

def home(request):
	return render(request,'home.html')


def followerid_index(request):
	return render(request,'followerid_index.html')
	# Create your views here.

def get_trending_topics(name):
	"""
		Author: Yunus Ege Saygılı

		Returns top ten trending topics for the input location. If the location is invalid,
		returns the top ten trending topics worldwide.
	"""

	# set up the consumer key and access token (obtained from https://apps.twitter.com/app/new)
	consumer_key='Di6z6xXCwJrvduPmXSbNZdILG'
	consumer_secret='VgfCkLt8QCmmVmBa8VJss6FQiE866L3Bs5DDSm8M9k5s3IDjwE'

	access_token='121485173-PXoF8a0MkroQQisbN89BwntiLtZIe31nDZnXtJyH'
	access_token_secret='CtHbI0YnoMCXMOxcEDYQZTMFqCRgXlJHYd3Umu1Pjpf2i'


	#  get authorization from Twitter API using tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	auth.secure = True

	api = tweepy.API(auth)

	places = api.trends_available()
	
	woeid = 1 # woeid for worldwide is 1

	for place in places: # search for the input parameter
		if place['name'] == name: # if found, get the id of the given location
			woeid = place['woeid']
			break

	trends = api.trends_place(woeid) # get the trending topics of the location
	trendlist = []

	for i in range(10) : # get the top ten tending topics
		trendlist.append(trends[0]['trends'][i]['name'])
	return trendlist

def search(queryString):
    """
        This method returns search results of user up to 20 tweets.
        It has one parameter, queryString where queryString is compulsory.
        Author: Busra Hilal Cirit
    """
    
    resultArray = []
    
    # Get Twitter API
    api = getTwitterApi()
        
        query = api.search(q = queryString,count = 20)
        
        for result in query:
        #print "Created at: (%s) \nUser: @%s \nTweet: %s" % (result.created_at, result.user.screen_name, result.text)
        resultArray.append([result.created_at,result.user.screen_name,result.text])
    return resultArray


