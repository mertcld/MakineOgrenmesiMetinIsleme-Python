from asyncore import write
from itertools import tee
import pandas as pd
import re,csv

data=pd.read_csv("kriptoVeri5Azaldi.csv")
print(data.columns[1])
def cleanTxt(text):
    text=re.sub(r'@[A-Za-z0-9]+','',text)
    text=re.sub(r'#','',text)
    text=re.sub(r'RT[/s]+','',text)
    text=re.sub(r'https?:\/\/\S+','',text)
    text=re.sub(r',','',text)
    emoji_pattern=re.compile("["
      u"\U0001F600-\U0001F64F" #emoticons
      u"\U0001F680-\U0001F6FF" # transport & map symbols
      u"\U0001F1E0-\U0001F1FF" # flags (iOs)
      u"\U0001F300-\U0001F5FF" # symbols & pictographs
      u"\U00002500-\U00002BEF" #chinese char
      u"\U00002702-\U000027B0"
      u"\U00002702-\U000027B0"
      u"\U000024C2-\U0001F251"
      u"\U0001f926-\U0001f937"
      u"\U00010000-\U0010ffff"
      u"\u2640-\u2642"
      u"\u2600-\u2B55"
      u"\u200d"
      u"\u23cf"
      u"\u23e9"
      u"\u231a"
      u"\ufe0f" # dingbats
      u"\u3030"
    "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'',text)
data[data.columns[1]]=data[data.columns[1]].apply(cleanTxt)
with open('temizlenmisTweetlerFORTFIgDF.txt','w',encoding="utf-8-sig") as f:
    for line in data[data.columns[1]]:
      
        f.write(line)
        f.write(' ,0')
        f.write('\n')
f.close()
print(data[data.columns[1]])