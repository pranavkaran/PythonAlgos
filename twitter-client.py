from TwitterAPI import TwitterAPI

consumer_key = "QFUymBMrssG6nezlwvne6hFBw"
consumer_secret = "EM4GOorDTGa8HYNumtpcm0QbM6VeTpHwV8yUrjyt5HAyT5fFvx"
access_token_key = "1940813725-EONSf3fZFcA0lRqrSnpH5iJAvROhuH3YFMbe1rs"
access_token_secret= "7ADkkEG2CknvuhXEd1qH8gPBBCJvNnVHivrcqLRWvfNNj"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# r = api.request('statuses/update', {'status':'This is a tweet!'})
# print(r.status_code)

# r = api.request('statuses/show/:%d' % 210462857140252672)
# print(r.text)

# r = api.request('search/tweets', {'q':'pizza'})
# for item in r:
#     print(item)

#Stream tweets from New York City:

r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})
print r.status_code
print r.get_rest_quota
for item in r:
	print(item)