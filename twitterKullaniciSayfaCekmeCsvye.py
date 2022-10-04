from twitter import *
import io
import sys
sys.path.append(".")
import config
import csv


twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

outfile = "kriptoVeriARTAN2.csv"

csvfile = open(outfile, "w",encoding="utf-8-sig")
csvwriter = csv.writer(csvfile)

users = ["BTC_Archive",
"Kriptoemre",
"KriptoData",
"kriptoreal1",
"coinmuhendisim",
"btc_magazin",
"CryptoTroia ",
"kripto_expert",
"WolfMS_",
"Btcrobotu",
"kriptowarrior",
"LoyaTheTrader",
"Kriptokoin",
"CryptoSarelf",
"Cointr",
"KoinBulteni",
"BTCHabercom",
"Coinnethaber",
"KriptoTurk_TR",
"Vforrkripto",
"Bycoinhunter",
"Eralpbuyukaslan",
"Cryptosocy",
"Cryptokahin",
"Rovercrc",
"Duffytrader",
"Jesscoin",
"Milyonerzihin",
"MoneyKripto",
"Mgokhanduman",
"CoinnCorner",
"Borsaressami",
"HASOsyalmedya",
"JrKripto",
]

for  i in users:

    user = i

    results = twitter.statuses.user_timeline(screen_name = user)

    for status in results:
     print("(%s) %s" % (status["created_at"], status["text"]))


    for status in results:
        user = user
        text = status["text"]
        createdAt=status["created_at"]
        row = [ user, text ,createdAt]
        csvwriter.writerow(row)
       

csvfile.close()