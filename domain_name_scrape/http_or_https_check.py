import pandas as pd
import requests
import time
df = pd.read_csv('dotcomdotbd_domain.csv')

df = df.Website.unique()
add_lst = []
for ad in df:
    add_lst.append(ad.split('//')[1])

website_df = pd.DataFrame(columns=['Website', 'http', 'https'])
type_pro = ['http', 'https']
for addr_dom in type_pro:
    for addr in range(len(add_lst)):
        website_df.loc[addr, 'Website'] = add_lst[addr]
        try:
            try:
                response = requests.get(addr_dom+'://'+add_lst[addr])
                website_df.loc[addr, addr_dom] = response
            except requests.exceptions.ConnectionError:
                website_df.loc[addr, addr_dom] = "not reachable"
            website_df.to_csv('test.csv', index=False)
            if (addr % 10 == 0):
                time.sleep(120)
        except:
            continue
    break


print(website_df)
