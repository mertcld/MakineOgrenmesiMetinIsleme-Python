

from twitter import *

import sys
sys.path.append(".")
import config

twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

user = "kriptoemre"

results = twitter.statuses.user_timeline(screen_name = user)

for status in results:
    print("(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore")))


yaz=open('tweet.txt','a',encoding="utf-8")
for status in results:
    yaz.write(str(status)+"\n")
    yaz.write("----------------"+"\n")
yaz.close()