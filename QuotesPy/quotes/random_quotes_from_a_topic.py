from bs4 import BeautifulSoup
import requests
import sys, time, random
from info.info import *

def get_random_quote_by_topic(topic):
    topic_quotes = []
    if "'" in topic:
        topic = topic.replace("'", "")
    topic_quote_content = requests.get(f"{url_quote_topics}{topic.replace(' ', '-').lower()}").content
    soup = BeautifulSoup(topic_quote_content, "html.parser")
    for quote in soup.find_all("div", {"style":"display: flex;justify-content: space-between"}):
        topic_quotes.append(quote.text.strip())
    return random.choice(topic_quotes)

def check_from_topic(topic):
    re_list = []
    for i in quote_topics:
        for x in i:
            re_list.append(x)
    if topic in re_list:
        return True
