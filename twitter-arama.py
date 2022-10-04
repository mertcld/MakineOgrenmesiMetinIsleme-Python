
from twitter import *
import sys
sys.path.append(".")
import config

twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))


query = twitter.search.tweets(q = "bitcoin")

print("Arama tamamlandı (%.3f seconds)" % (query["search_metadata"]["completed_in"]))


for result in query["statuses"]:
    print("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))
