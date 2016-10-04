from __future__ import print_function

import json
import tweepy
import logging
from unqlite import UnQLite
from ConfigParser import SafeConfigParser


logging.basicConfig(level=logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

unqlite = UnQLite('pilkadaDKI2017')

config  = SafeConfigParser()
config.read('config.ini')
consumer_key        = config.get('twitter', 'consumer_key')
consumer_secret     = config.get('twitter', 'consumer_secret')
access_token        = config.get('twitter', 'access_token')
access_token_secret = config.get('twitter', 'access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class OwnStreamListener(tweepy.StreamListener):

    def on_data(self, raw_data):
        data = json.loads(raw_data)
        # exclude retweeted's tweet.
        # reference: http://stackoverflow.com/a/30378987/1936697
        if not data.get('retweeted') and 'RT @' not in data.get('text'):
            unqlite[data['id']] = data
            logger.info(data['text'])


if __name__ == '__main__':
    listener    = OwnStreamListener()
    stream      = tweepy.Stream(auth=api.auth, listener=listener)
    tags        = ['ahok', 'pilkada DKI 2017', 'sandiaga uno', 'djarot',
                   'anis baswedan']
    stream.filter(track=tags)
