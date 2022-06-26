***
# QuotesPy
QuotesPy is an open source program that displays a random quote from a celebritie as a notification
***
# installation
  - build from source :
```
  git clone https://github.com/0RaMsY0/QuotesPy
  cd QuotesPy
  python setup.py
```
- install using pip :
``` cli
    pip install quotescli
```
***
# Usage
  
  | *arguments*    | Arguments form | *usage*     |
  |:--------------:|:--------------:|:---------:|
  | -h             |  --help | show help |
  | -sn            |  --search-by-name | search for the quote of someone by his name|
  | -st            |  --search-by-topic | search for the quote of a topic |
  | -T             |  --Topic | display all the availables Topics |
  | -t             |  --time | set a time to display the quote |
  | -pr            |  --print-quote | print the quote into the console (in default it will be shown as a notification) |
  ---
  <h2> Examples :</h2>
   - search by name (-sn).
  <img src="https://github.com/0RaMsY0/QuotesPy/blob/main/quotescli/examples/search_by_name-pr.png" alt="search by name (-sn)"/>
   - search by Topic (-st)
  <img src="https://github.com/0RaMsY0/QuotesPy/blob/main/quotescli/examples/serach_by_topic.png" alt="search by Topic (-st)"/>
   - this is how the quote well be displaied (as a notification) if the -pr is not used
  <img src="https://github.com/0RaMsY0/QuotesPy/blob/main/quotescli/examples/show_as_notification.png" alt="this is how the quote well be displaied (as a notification) if the -pr is not used"/>
   - the diferents Topics that you can search for quote about them (use -T to diplay them)
  <img src="https://github.com/0RaMsY0/QuotesPy/blob/main/quotescli/examples/show_topics.png" alt="the diferents Topics that you can search for quote about them (use -T to diplay them)"/>
 
# ressourses

 QuotesPy uses https://www.brainyquote.com/ to scrape search resultes and displays it to the user
  by a notification or directly to the terminal
