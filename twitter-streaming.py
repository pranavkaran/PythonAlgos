import tweepy
import sys
import jsonpickle
import os
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


fName = '/Users/pranavkaran/Documents/Knoesis/Interview/Dallastweets.txt' # We'll store the tweets in a text file.
class StdOutListener(StreamListener):

    def on_data(self, data):
    	with open(fName, 'a+') as f:
    		f.write(jsonpickle.encode(data, unpicklable=False))
        print data
        return True

    def on_error(self, status):
        print status

API_KEY = "QFUymBMrssG6nezlwvne6hFBw"
API_SECRET = "EM4GOorDTGa8HYNumtpcm0QbM6VeTpHwV8yUrjyt5HAyT5fFvx"
access_key = "1940813725-EONSf3fZFcA0lRqrSnpH5iJAvROhuH3YFMbe1rs"
access_secret= "7ADkkEG2CknvuhXEd1qH8gPBBCJvNnVHivrcqLRWvfNNj"
# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
                   wait_on_rate_limit_notify=True)
 
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

searchQuery = '#someHashtag'  # this is what we're searching for
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = '/Users/pranavkaran/Documents/Knoesis/Interview/Dallastweets.txt' # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1L

tweetCount = 0
l = StdOutListener()
stream = Stream(auth, l)
#stream.filter(locations = '-122.75,36.8,-121.75,37.8')
stream.filter(locations = [-97,32,-96,33])

print("Downloading max {0} tweets".format(maxTweets))
# with open(fName, 'w') as f:
#     while tweetCount < maxTweets:
#         try:
#             if (max_id <= 0):
#                 if (not sinceId):
#                     new_tweets = api.request('statuses/filter', {'locations':'-97,32,-96,33'}, count=tweetsPerQry)
#                 else:
#                     new_tweets = api.request('statuses/filter', {'locations':'-97,32,-96,33'}, count=tweetsPerQry,
#                                             since_id=sinceId)
#             else:
#                 if (not sinceId):
#                     new_tweets = api.request('statuses/filter', {'locations':'-97,32,-96,33'}, count=tweetsPerQry,
#                                             max_id=str(max_id - 1))
#                 else:
#                     new_tweets = api.request('statuses/filter', {'locations':'-97,32,-96,33'}, count=tweetsPerQry,
#                                             max_id=str(max_id - 1),
#                                             since_id=sinceId)
#             if not new_tweets:
#                 print("No more tweets found")
#                 break
#             for tweet in new_tweets:
#                 f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
#                         '\n')
#             tweetCount += len(new_tweets)
#             print("Downloaded {0} tweets".format(tweetCount))
#             max_id = new_tweets[-1].id
#         except tweepy.TweepError as e:
#             # Just exit if any error
#             print("some error : " + str(e))
#             break

# print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))


# #api.request('statuses/filter', {'locations':'-74,40,-73,41'})
# North Latitude: 40.915256 South Latitude: 40.496044 East Longitude: -73.700272 West Longitude: -74.255735
# #api.request('statuses/filter', {'locations':'-97,32,-96,33'})
# North Latitude: 33.023792 South Latitude: 32.617537 East Longitude: -96.463738 West Longitude: -96.998941
