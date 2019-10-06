from bs4 import BeautifulSoup
import requests
import urllib.request
import re
from collections import Counter
import pandas as pd
import time
text = []
final_text = []
df = pd.DataFrame(columns=['Website'])


def search_url(query, page, val):
    url = "http://www.google.com/search?q=" + \
        query + "&start=" + str((page - 1) * 10)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for desc in soup.select("#main > div > div > div > a"):
        try:
            txt = re.search(
                "((http|https)\:\/\/)+[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,3}", str(desc.get('href'))).group()
            val = val + 1
            df.loc[val] = txt
            df.to_csv('dotcomdotbd_domain.csv', index=False)
        except:
            continue
    """
    text.append(desc.text)

    for string in text:
        string = re.sub("[^A-Za-z ]", "", string)
        final_text.append(string)

    count_text = ' '.join(final_text)
    res = Counter(count_text.split())

    keyword_Count = dict(sorted(res.items(), key=lambda x: (-x[1], x[0])))

    for x, y in keyword_Count.items():
        print(x, " : ", y)
    """
    return val


cc = 0
for pg in range(500):
    if pg == 0:
        continue
    cc = search_url(".com.bd", pg, cc)  # find all .com.bd domain
    break
    time.sleep(100)  # after 10 min it will call the url
