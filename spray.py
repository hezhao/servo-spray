import sys
import time
import tweepy
import servo

# Old Spice Spray
consumer_key="tLfQ407qRp4nTuyI5Hhp0Q"
consumer_secret="dSCVDjWFppXLvnjQw9WyB5TJYwIfLcTc96zU9GuMA"

# @WKTesty
access_key = "1360181522-uUWNeU9vaolTIGFI9OYDQ8jsQNEhp4Jy3Eihuqh"
access_secret = "iMtIREz0aHFlHHrE7WT9MWnlwp32OsEI4oUDJ0Y" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		# import pdb; pdb.set_trace()
		print('@' + status.user.screen_name + ' ' + status.text)
		tweet = '@' + status.user.screen_name + ' Fresh spray!'
		s = servo.Servo()
		s.run()
		try:
			api.update_status(tweet, status.id)
		except Exception, e:
			print 'Error'
			print(str(e))

	def on_error(self, status_code):
		print >> sys.stderr, 'Encountered error with status code:', status_code
		return True # Don't kill the stream

	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['#givemethespray'])
