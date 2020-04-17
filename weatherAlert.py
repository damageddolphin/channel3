from setup import *

import feedparser

def weatherAlerts():
# Load URL from NOAA's National Weather Service weather alerts
    alertItems=[]
    alertReturn=[]
    del alertItems[:]
    del alertReturn[:]
    alertFeeds=[
               'https://alerts.weather.gov/cap/wwaatmget.php?x=' + weatherAlertCode + '&y=0'
               ]
    for url in alertFeeds:
        alertFeed = feedparser.parse(url)
        alerts = alertFeed["items"]
        for alert in alerts:
            alertItems.append(alert)
        for alertItem in alertItems:
            alertText = alertItem["title"]
            alertType = ""
            if "warning" in (alert["title"].lower()) or "warning" in (alert["summary"].lower()):
                alertType = "warning"
            elif "advisory" in (alert["title"].lower()) or "advisory" in (alert["summary"].lower()):
                alertType = "advisory"
            elif "watch" in (alert["title"].lower()) or "watch" in (alert["summary"].lower()): 
                alertType = "watch"
            else:
                alertType = "other"
# Check if there is an active alert by seeing if "There are no active watches, warnings or advisories" does not exist
            if "There are no active watches, warnings or advisories" in alertText:
                alertReturn.append("NONE")
            else:
                 alertText = alertItem["title"] + " - " + alertItem["summary"]
                 alertReturn.append(alertText)
        return(alertReturn)

