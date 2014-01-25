# -*- coding: utf-8 -*-

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


"""
    t.string   "tweet_id"
    t.string   "image_url"
    t.string   "username"
    t.datetime "created_at"
    t.float    "latitude"
    t.float    "longitude"
    t.text     "raw"
    t.string   "text"
"""

def process_photo(**kwargs):
	for key, value in kwargs.iteritems():
		print "%s : %s" % (key, value)
	print '---'


if __name__ == '__main__':
	while True:	
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		api = API(auth)

		results = api.search(q="hackyyc", include_entities = True)
		for result in results:
			uid = result.author.id
			uname = result.author.name
			tweet_text = result.text
			tweet_id = result.id
			entities = result.entities
			geo = result.geo
			coor = result.coordinates
			source = result.source
			created_at = result.created_at
			if 'media' in entities:
				curr_media = entities['media']
				for media_item in curr_media:
					if media_item['type'] == 'photo':
						mid = media_item['id']
						real_url = media_item['media_url']
						twitter_url = media_item['display_url']
						process_photo( tweet_id = tweet_id,
							image_url = real_url,
							username = uname,
							text = tweet_text,
							string = tweet_text,
							geo = geo,
							coor = coor,
							source = source,
							datetime = created_at,
							mid = mid,
						)
						#print mid TODO: NEED mid
		time.sleep(15)
