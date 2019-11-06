# The DP Archives

This tool allows you to scrape all the articles made available through [the Daily Pennsylvanian Archives](https://dparchives.library.upenn.edu/)

### Installation

Clone the repo into your local folder:

```
git clone https://github.com/joelslee/thedparchives
```
Running is simple and at this point will download every issue from 1885 to 2002.

```
python webscraper.py
```
Between 1885 to 2002, there are around 16,000 articles, amounting to a little over 1 GB of .txt files. Towards that end, the scraping takes awhile, and you likely will be "timed out" by the dp archives' API. When the script is running, you will see a count being printed to your console. If you get timed out, simply add the last count that you got to the end of the script.

```
python webscraper.py
7433
```

### To Do list
- Be able to add flags to only scrape articles from certain dates
- Automatically catch timeout and wait with a timer, and then start again.

### About the project

the dp archives web scraper was created for the final project for the class, Introduction to Digital Humanities taught by [Scott Enderle](https://github.com/senderle) in Spring 2019. The [topic modeling tool](github.com/senderle/topic-modeling-tool) was used on the files scraped by this project. The early code for this was written in a jupyter notebook. After completion of the project, I decided to make it a python executable script for those who want to scrape the daily pennsylvanian archives for themselves.

Special thanks go to [Matthew Pilecki](https://www.library.upenn.edu/people/staff/matthew-pilecki) and [Jessica Dummer](https://www.library.upenn.edu/people/staff/jessica-dummer) from [Penn Libraries](https://www.library.upenn.edu/), [Stefan Boddie](https://veridiansoftware.com/about/) from [Veridian Software](https://veridiansoftware.com/) for helping me with the API, and [Scott Enderle](https://github.com/senderle) for oversight for the project.
