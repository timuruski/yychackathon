from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

consumer_key="Uqp2pItLIvmbTMrLDtswA"
consumer_secret="QqRVaMlbZbsQsPeH6UB8iDJdNDOVRhLVPWZkiuhOQ"

access_token="615753-dOh3c5ypD93yz2voj9qGkXEcKLXAvaYqr7OeojFPmr0"
access_token_secret="P7o4aHQbJdk71tgNSLelVOVnfcvOqfUi8Z1OFG0nR4b77"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
  #  l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

   # stream = Stream(auth, l)
    #stream.filter(track=['hackyyc'])
	
	api = API(auth)

	results = api.search(q="hackyyc")

	for result in results:
		print result.text
