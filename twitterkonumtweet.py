
from twitter import *

import sys
import csv

latitude = 40.9090003   
longitude = 29.2209306    
max_range = 3             
num_results =15        
outfile = "output.csv"

import sys
sys.path.append(".")
import config

twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

csvfile = open(outfile, "w")
csvwriter = csv.writer(csvfile)

row = [ "user", "text", "latitude", "longitude" ]
csvwriter.writerow(row)

result_count = 0
last_id = None
while result_count <  num_results:
    query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)

    for result in query["statuses"]:
        if result["geo"]:
            user = result["user"]["screen_name"]
            text = result["text"]
            text = text.encode('ascii', 'replace')
            latitude = result["geo"]["coordinates"][0]
            longitude = result["geo"]["coordinates"][1]

            row = [ user, text, latitude, longitude ]
            csvwriter.writerow(row)
            result_count += 1
        last_id = result["id"]

    print("got %d results" % result_count)

csvfile.close()

print("written to %s" % outfile)

