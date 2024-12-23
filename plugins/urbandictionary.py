# https://www.urbandictionary.com/daily.rss
def get_urbandictionary_daily_html():
    import feedparser
    feed = feedparser.parse('https://www.urbandictionary.com/daily.rss')
    return f"""<h1>{feed.entries[0].title}</h1>
<p>{feed.entries[0].summary}</p>
"""

if __name__ == "__main__":
        print(get_urbandictionary_daily_html())