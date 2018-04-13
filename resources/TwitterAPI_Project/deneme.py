import tweepy,json,_json
consumer_key = 'LtUoLhvWzGOUODCpHkIW1cH7s'
consumer_secret = 'o18cdHxf8YLgLaWJZZ8lMvcv2SACOAIJYZmZB5s7nxmPPHRgc3'
access_token = '984099024402894848-bTCwMxW8o04woXa6OAD2Y7PIoxy3TPb'
access_token_secret = 'ENb06BGdQamMnFHaxqDeUFL8GzafGIylruSW0s3ubXgqs'

#  get authorization from Twitter API using tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#  get the values of the user, and the target

# if 'user_id' in request.POST
# block

print()
print(str)