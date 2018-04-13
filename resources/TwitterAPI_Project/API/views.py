from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Apı_class
from .serializers import Apı_Classserializer
import tweepy,json
from keys import *

class Apı_ClassList(APIView):
    def get(self,request,**kwargs):

        user_id=kwargs['pk']

        #  get authorization from Twitter API using tweepy

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        #  get the values of the user, and the target

        # if 'user_id' in request.POST
        # block
        list = api.followers(id=user_id)
        jsonlist=[]
        print()
        for item in list:
            jsonlist.append(item._json['name']+"  @"+item._json['screen_name'])

        #Apılist=Apı_class.objects.all()
        #serializer=Apı_Classserializer(list,many=True)
        return Response(jsonlist)


    def post(self,request,**kwargs):
        print(request.data)
        pass

class getTrendingTopic(APIView):
    def get(self,request,**kwargs):
        """
        		Author: Yunus Ege Saygılı
        		Returns top ten trending topics for the input location. If the location is invalid,
        		returns the top ten trending topics worldwide.
        	"""

        #  get authorization from Twitter API using tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        auth.secure = True

        api = tweepy.API(auth)

        places = api.trends_available()

        woeid = 1  # woeid for worldwide is 1

        for place in places:  # search for the input parameter
            if place['name'] == kwargs['pk']:  # if found, get the id of the given location
                woeid = place['woeid']
                break

        trends = api.trends_place(woeid)  # get the trending topics of the location
        trendlist = []

        for i in range(10):  # get the top ten tending topics
            trendlist.append(trends[0]['trends'][i]['name'])
        return Response(trendlist)

class block_user(APIView):
    def get(self,request,**kwargs):
        # author: Berke Esmer - 2015400021
        # block_user - params: theTarget user, the user who is logged on

        #  get authorization from Twitter API using tweepy

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        theTarget=kwargs['pk']
        #  get the values of the user, and the target

        list=api.create_block(id=theTarget)


        list1=json.dumps(list._json)
        return Response(list1)

class followUser(APIView):
    def get(self,request,**kwargs):
        """
        	Author: Yusuf Baspinar
        	Follows given user
        	Follows the accounts inside followList.txt that is given as id's.
        	"""
        #  get authorization from Twitter API using tweepy

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        theUser=kwargs['pk']
        api.create_friendship(theUser)  # Follows given user

        # Follow everyone from list. If already following users in the list unfollow



        return Response(api.create_friendship(theUser))

class PostTweet(APIView):



    def get(self,requset,**kwargs):

        """Post a tweet in @MemoristBeavers account using Twitter API."""

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        user=api.update_status(status=kwargs['pk'])
        list=json.dumps(user._json)
        return Response(list)

    def post(self,request,format=None):

        return Response({'received_data':request.data})

# retweet(tweet id)

# retweet(user's last tweet)

# getfavorites

# viewfriends

#