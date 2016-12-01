# Magic Mirror 
# twitter.py
# Collects information from the twitter API to be displayed on a monitor behind a mirror.
# Author: Kevin Hewitt
# Derived from Michael Fahy's "twitterexample.py"
# Version 1.1
# Date: February 15, 2016

import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

print 'Example 1'
print 'Establish Authentication Credentials'
CONSUMER_KEY = 'bTVpNmFa2Q4Kh7LPRHelgYa4M'
CONSUMER_SECRET = 'K2DeTKGlVshW4beSfKmgFC8MpbmDxv4ipvj4lwm425DZ2'
OAUTH_TOKEN = '775173115760390145-SGyPhaXVEeJr988qRXxZx48dWCnYxpv`'
OAUTH_TOKEN_SECRET = 'K2DeTKGlVshW4beSfKmgFC8MpbmDxv4ipvj4lwm425DZ2'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# 'Example 2 - Display world and US trends'
# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
print 'Display World Trends'
print
print world_trends
print
print 'Display US trends'
print
print us_trends
import json
#'Example 6. Extracting text, screen names, and hashtags from tweets'
print
status_texts = [ status['text']
                 for status in statuses ]

screen_names = [ user_mention['screen_name']
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w
          for t in status_texts
              for w in t.split() ]

# Explore the first 5 items for each...

print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)