from bs4 import BeautifulSoup
import urllib.request


url = urllib.request.urlopen('https://www.rottentomatoes.com/m/johnny_english_strikes_again_2018')
content = url.read()
soup = BeautifulSoup(content, 'html.parser')

#table = soup.findAll('div',attrs={"class":"media-body"}).find('p')
table = soup.select('div.media-body > p')
for x in table:
    #print(x.text)
    print(x.text.strip()) #strip reduce space 
    print("\n")

