from email.quoprimime import quote
import colorama
from prettytable import PrettyTable
from info.info import quote_topics

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