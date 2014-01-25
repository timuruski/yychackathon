from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import os
import time

consumer_key = os.environ['consumer_key'] 
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

if __name__ == '__main__':
	while True:	
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		api = API(auth)

		results = api.search(q="hackyyc", include_entities = True)
		for result in results:
			#print dir(result)
			tweet_text = result.text
			if result.geo:
				print 'GEO not NONE'
			entities = result.entities
			if 'media' in entities:
				curr_media = entities['media']
				for media_item in curr_media:
					if media_item['type'] == 'photo':
						mid = media_item['id']
						real_url = media_item['media_url']
						twitter_url = media_item['display_url']
						print mid
						print real_url, twitter_url
						print (media_item)
						print '----'
		time.sleep(15)
