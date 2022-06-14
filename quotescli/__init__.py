from bs4 import BeautifulSoup
import requests
import argparse
import time, random
import colorama
from plyer import notification
from prettytable import PrettyTable

# vars
url = "https://www.brainyquote.com/search_results?x=0&y=0&q="
url_quote_topics = "https://www.brainyquote.com/topics/"
quote_topics = [
    ['Age',
    'Alone',
    'Amazing',
    'Anger',
    'Anniversary',
    'Architecture',
    'Art Favorite',
    'Attitude',
    'Beauty',
    'Best',
    'Birthday'],
    ['Brainy',
    'Business',
    'Car',
    'Chance',
    'Change',
    'Christmas',
    'Communication',
    'Computers',
    'Cool',
    'Courage',
    'Dad'],
    ['Dating',
    'Death',
    'Design',
    'Diet',
    'Dreams',
    'Easter',
    'Education',
    'Environmental',
    'Equality',
    'Experience',
    'Failure'],
    ['Faith',
    'Family',
    'Famous',
    'Father s Day',
    'Fear',
    'Finance',
    'Fitness',
    'Food',
    'Forgiveness',
    'Freedom',
    'Friendship Favorite'],
    ['Funny',
    'Future',
    'Gardening',
    'God',
    'Good',
    'Government',
    'Graduation',
    'Great',
    'Happiness',
    'Health',
    'History'],
    ['Home',
    'Hope',
    'Humor',
    'Imagination',
    'Independence',
    'Inspirational',
    'Intelligence',
    'Jealousy',
    'Knowledge',
    'Leadership',
    'Learning'],
    ['Legal',
    'Life Favorite',
    'Love Favorite',
    'Marriage',
    'Medical',
    'Memorial Day',
    'Men',
    'Mom',
    'Money',
    'Morning',
    'Mother s Day'],
    ['Motivational Favorite',
    'Movies',
    'Moving On',
    'Music',
    'Nature',
    'New Year s',
    'Parenting',
    'Patience',
    'Patriotism',
    'Peace',
    'Pet'],
    ['Poetry',
    'Politics',
    'Positive',
    'Power',
    'Relationship',
    'Religion',
    'Respect',
    'Romantic',
    'Sad',
    'Saint Patrick s Day',
    'Science'],
    ['Smile',
    'Society',
    'Space',
    'Sports',
    'Strength',
    'Success Favorite',
    'Sympathy',
    'Teacher',
    'Technology',
    'Teen',
    'Thankful'],
    ['Thanksgiving',
    'Time',
    'Travel',
    'Trust',
    'Truth',
    'Veterans Day',
    'War',
    'Wedding',
    'Wisdom Favorite',
    'Women',
    'Work'],
]

# argsparser
parser = argparse.ArgumentParser()
parser.add_argument("-sn", "--search-by-name", help="search for the quote of someone by his name")
parser.add_argument("-st", "--search-by-topic", help="search for the quote of a topic")
parser.add_argument("-T", "--Topic", help="show the available topics", action="store_true")
parser.add_argument("-t", "--time", help="set up a time(hour) to show the quote  [you need to let the code run in the background]")
parser.add_argument("-pr", "--print-quote", help="print the quote of this celebritie in the console", action="store_true")

args = parser.parse_args()
celebrity_name = args.search_by_name
quote_topic = args.search_by_topic
notification_time = args.time
print_quote_to_console = args.print_quote
show_topics = args.Topic
quote_content = []
# func 
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

def show_the_topics():
    x = PrettyTable()
    x.field_names = [f"{colorama.Fore.BLUE}Topics{colorama.Fore.WHITE}"]
    for i in range(0,11):
        x.add_rows(
        [
            [f"{colorama.Fore.CYAN} -- {colorama.Fore.WHITE}".join(quote_topics[i])],
        ]
    )   
    print(x)

def get_celebritie_quote():
    url_content = requests.get(f"{url}{celebrity_name.replace(' ', '+')}").content
    soup = BeautifulSoup(url_content, "html.parser")
    if soup.find("h2").text == "No search results were found.":
        print(
            f"{colorama.Fore.BLUE} [ + ] {colorama.Fore.RED} No search results were found for {colorama.Fore.CYAN}{celebrity_name} {colorama.Fore.RED}please check your spelling and try again {colorama.Fore.WHITE}"
        )
    else:
        for quote in soup.find_all("div", {"style": "display: flex;justify-content: space-between"}):
            quote_content.append(quote.text.strip())
        # ***********************************************************************************************************************
        ran_quote = random.choice(quote_content) # selecting a random quote form the list
        if print_quote_to_console:
            print(
                f"{colorama.Fore.BLUE} [ + ] {colorama.Fore.GREEN} Quote of the Day - {colorama.Fore.YELLOW}{celebrity_name} \n {colorama.Fore.CYAN} {ran_quote} {colorama.Fore.WHITE}"
            )
        elif notification_time is not None:
            show_quote_as_notification_by_time()
        else:
            show_quote_as_notification(ran_quote)

def show_quote_as_notification(quote):
    notification.notify(
        title=f"Quote of the Day - {celebrity_name}" if celebrity_name is not None else "Quote of the Day",
        message=quote,
        timeout=10
    )
def show_quote_as_notification_by_time():
     while True:
        if time.localtime().tm_hour == int(notification_time):
            show_quote_as_notification(get_random_quote_by_topic(quote_topic))
            break
        else:
            pass

def run():
    if celebrity_name is not None:
        get_celebritie_quote()
    elif quote_topic is not None:
        if check_from_topic(quote_topic):
            print(
                    f"{colorama.Fore.BLUE} [ + ] {colorama.Fore.GREEN} Quote about {quote_topic} \n {colorama.Fore.CYAN} {get_random_quote_by_topic(quote_topic)} {colorama.Fore.WHITE}"
                ) if print_quote_to_console else show_quote_as_notification(get_random_quote_by_topic(quote_topic))
            if notification_time is not None :
                show_quote_as_notification_by_time()
        else:
            print(
            f"{colorama.Fore.BLUE} [ + ] {colorama.Fore.RED} Unknown Topic use (-T) or (--Topic) to see the available topics {quote_topic} {colorama.Fore.WHITE}"
            )
    elif show_topics:
        show_the_topics()
    else:
        parser.print_usage()

if __name__ == "__main__":
    run()