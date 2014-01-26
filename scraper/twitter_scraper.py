# -*- coding: utf-8 -*-

#from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
#from tweepy import Stream
from tweepy import API
import os
import time
import psycopg2
import urlparse
import urllib2

consumer_key = os.environ['consumer_key'] 
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

database_url = os.environ['database_url']



HASH_TAG = "#hackyyc"


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

def get_db_conn():
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(database_url)
	conn = psycopg2.connect(
		database=url.path[1:],
		user=url.username,
		password=url.password,
		host=url.hostname,
		port=url.port
	)
	return conn



def db_test_insert(tweet_id, image_url, username, created_at, latitude, logitude, raw, text):
	conn = get_db_conn()
	cursor = conn.cursor()
#id | tweet_id | image_url | username | created_at | latitude | longitude | raw | text
	sql_insert_tweet = ("INSERT INTO interesting_tweets (tweet_id, "
						"image_url, "
						"username, "
						"created_at, "
						"latitude, "
						"longitude, "
						"raw, "
						"text) "
		#"VALUES (%s, %s, %s, %s, %s, %s, %s, %s) " #See http://stackoverflow.com/a/15841000/443779
		"SELECT %s, %s, %s, %s, %s, %s, %s, %s "
		"WHERE "
		"NOT EXISTS ( "
		        "SELECT tweet_id FROM interesting_tweets WHERE tweet_id = CAST(%s AS TEXT) " 
			")"
		"RETURNING id"
			)
	data = (tweet_id, image_url, username, created_at, latitude, logitude, raw, text, tweet_id)

	cursor.execute(sql_insert_tweet, data)

	try:

		id_of_new_row = cursor.fetchone()[0]
	except TypeError:
		#tweet insert didn't go ... we've likely already writen this tweet
		return
	conn.commit()

	"""
 id                   | integer                | not null default nextval('images_id_seq'::regclass)
 interesting_tweet_id | integer                |
 original_url         | character varying(255) |
 media_id             | character varying(255) |
 data                 | bytea
	"""
	
	if id_of_new_row:
		image_data = urllib2.urlopen(image_url).read()
		sql_insert_image = ( "INSERT INTO images (interesting_tweet_id, "
					" original_url, "
					" media_id, "
					" data  ) "
				" SELECT %s "
				" WHERE "
				" NOT EXISTS ( "
					" SELECT media_id FROM images WHERE media_id = CAST(%s AS TEST) "
				")"
				)

		data_insert_image = (id_of_new_row, image_url, mid, psycopg2.Binary(image_data))
		cursor.execute(sql_insert_image, data_insert_image)
		conn.commit()	
	
	cursor.close()
	conn.close()
					


def process_photo(**kwargs):
	"""
				tweet_id = tweet_id
				image_url = real_url,
				username = uname,
				text = tweet_text,
				string = tweet_text,
				geo = geo,
				coor = coor,
				source = source,
				datetime = created_at,
				mid = mid,
	def db_test_insert(tweet_id, image_url, username, created_at, latitude, logitude, raw, text):
	"""
	db_test_insert(kwargs.get('tweet_id'),
			kwargs.get('image_url'),
			kwargs.get('username'), 
			kwargs.get('created_at'),
			kwargs.get('latitude'),
			kwargs.get('logitude'),
			kwargs.get('raw'),
			kwargs.get('text')
			)

if __name__ == '__main__':
	while True:	
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		api = API(auth)

		results = api.search(q=HASH_TAG, include_entities = True)

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
							created_at = created_at,
							mid = mid,
						)
						
						#print mid TODO: NEED mid
		time.sleep(15)
