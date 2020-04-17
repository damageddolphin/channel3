"""
    weatherObservationURL - Change your observation office code
    ENTER THE CODE FOR YOUR FORECASTING OFFICE
    VISIT https://forecast.weather.gov and search for your ZIP CODE
    Look for "CURRENT CONDITIONS AT <Name of Location> (NNNN)" The code is in the parentheses
    ### Change PHHI.xml to your CODE.xml

    ObsUrl
    Change the lat= and lon= to your lat & long
    Go to https://www.latlong.net/ and enter your address as 123 Main St, Anytown, KS and click find
    Be sure to enter your Lat and Long correctly

    WeatherAlertCode
    Visit https://alerts.weather.gov/
    Scroll down and select your state and click County List
    Change the WeatherAlertCode to your six digit county code

    News Feeds
    Copy the URL of the RSS feed and include the comma after every entry

    excludeList
    This is a list of words that the program will check are in the RSS news feeds and exclude those results from appearing
    Add a "word" followed by a comma on each line

    SET loadMuisc = 1 to turn on BGM
    ADD LIST OF MP3 FILES TO playlist.lst
"""


weatherObservationURL = 'http://w1.weather.gov/xml/current_obs/PHHI.xml'

obsUrl = "https://forecast.weather.gov/MapClick.php?lat=21.401&lon=-158.0393&unit=0&lg=english&FcstType=json"

weatherAlertCode = 'HIC003'

feeds = [
    "http://feeds.reuters.com/Reuters/topNews",
    "http://feeds.reuters.com/Reuters/domesticNews",
    "http://feeds.reuters.com/reuters/technologyNews",
    "http://feeds.reuters.com/reuters/scienceNews",
    "http://feeds.reuters.com/reuters/oddlyEnoughNews",
]

excludeList = [
    "spatula",
]

loadMusic = 0

cableCo = "ADELPHIA CABLE"
