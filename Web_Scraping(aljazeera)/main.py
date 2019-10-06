from webscrap import wlog
from webscrap import wscrap
wlog.set_custom_log_info('html/error.log')

"""
try:
    raise Exception
except Exception as e:
    wlog.report(e)
 """
news_scrap = wscrap.NewsScraper(wscrap.url_aj,wlog)
#news_scrap.retrieve_webpage() #call this for first time for retriving the data
#news_scrap.write_webpage_as_html() #call this for first time for retriving the data

news_scrap.read_webpage_from_html()
news_scrap.convert_data_to_bs4()
#news_scrap.print_data()
news_scrap.parse_soup_to_simple_html()
#news_scrap.print_beautiful_soup()





