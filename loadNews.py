from setup import *
import feedparser

def loadNews():
    items=[]
    del items[:]
    for url in feeds:
        feed = feedparser.parse(url)
        posts = feed["items"]
        for post in posts:
            wordCheck = str(post)
            if not any(word in wordCheck for word in excludeList):
                items.append(post['published']+ " " + post['title'])
    return(items)

