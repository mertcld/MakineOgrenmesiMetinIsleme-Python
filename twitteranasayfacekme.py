
from twitter import *

import sys
sys.path.append(".")
import config

twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

statuses = twitter.statuses.home_timeline(count = 50)
print(statuses)

for status in statuses:
    print("(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"]))
