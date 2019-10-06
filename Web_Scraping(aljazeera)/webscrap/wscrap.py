from urllib.request import urlopen
from bs4 import BeautifulSoup

#Global Variable
url_aj = "http://www.aljazeera.com"
filepath = "html/aj.html"
output_html = 'html/simplenews.html'

class NewsScraper:
    __url = ''
    __data = ''
    __wlog = None
    __soup = None

    def __init__(self,url,wlog):
        self.__url = url
        self.__wlog = wlog

    def retrieve_webpage(self):
        try:
            html = urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__wlog.report(e)
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print("Retrieved Successfully")
    def write_webpage_as_html(self,filepath=filepath,data=''):
        try:
            with open(filepath,'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
    

    def read_webpage_from_html(self,filepath=filepath,data=''):
        try:
            with open(filepath) as fobj:
                self.__data = fobj.read()
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
            
    def change_url(Self,url):
        self.__url = url

    def print_data(self):
        print(self.__data)

    def convert_data_to_bs4(self):
        self.__soup = BeautifulSoup(self.__data,"html.parser")
    
    def parse_soup_to_simple_html(self):
        news_list = self.__soup.find_all(['h1','h2','h3','h4'])
        #print(news_list)
        htmltext = '''
<html>
    <head><title>Simple News Link Scrapper</title></head>
    <body>
        {NEWS_LINKS} #variable
    </body>
</html>
'''


        news_links = '<ol>'

        for tag in news_list:
            if tag.parent.get('href'):
                print (self.__url + tag.parent.get('href'), tag.string)
                link = self.__url + tag.parent.get('href')
                title = tag.string
                news_links += "<li><a href='{}' target='_blank'>{}</a></li>\n".format(link, title)
        
        news_links += '<ol>'
        htmltext = htmltext.format(NEWS_LINKS=news_links)
        # print(htmltext)
        self.write_webpage_as_html(filepath=output_html, data=htmltext.encode())



            

