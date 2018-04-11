import tweepy

def getTwitterApi():
    
    consumerKey = '5GNyqW1qeECVJ6m3dzx6QGD3f'
    consumerSecret = '6Q7N0yZle5qvbDLqnIioRBXzkqODmSMdKSqxIHevrZKnHyWjkf'
    accessToken = '981859542555348992-4VIhOkbS4MJru964CPgrGFteVQIzj1p'
    accessTokenSecret = 'sUaIhvHW91KMgI1EqWijJzcbMMm6BLoSNd9HU76FCB4Go'
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    
    return tweepy.API(auth)




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


search("baby")
