import webbrowser
import feedparser

feed = feedparser.parse("https://www.wowhead.com/news/rss/retail")


feed_entries = feed.entries

for entry in feed.entries:

    article_title = entry.title
    article_link = entry.link
    article_published_at = entry.published # Unicode string
    article_published_at_parsed = entry.published_parsed # Time object
    
    content = entry.summary

    print ("{}[{}]".format(article_title, article_link))

    print ("Published at {}".format(article_published_at))

    print("Content {}".format(content))
    