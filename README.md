# channel3
Code from probnot's wpg-weatherchan and revised to work with US based weather. https://github.com/probnot/wpg-weatherchan


Channel 3 is a recreation of the teletext service found on US cable systems in the 80s and 90s

----------

PREREQUISITES:

Ensure your system is up to date by running sudo apt update && sudo apt upgrade

Download VCR OSD Mono font and place in /usr/local/share/fonts

Install python3-pip

Install mpg321

During first run, if there are any missing modules install with pip3 install [MODULE NAME]

----------
The program is currently set for Oahu, Hawaii weather. To change, modify setup.py. 
-----

weatherObservationURL - Change your observation office code - ENTER THE CODE FOR YOUR FORECASTING OFFICE

VISIT https://forecast.weather.gov and search for your ZIP CODE. Look for "CURRENT CONDITIONS AT <Name of Location> (NNNN)" The code is in the parentheses. Change PHHI.xml to your CODE.xml.

-----

ObsUrl - Change the lat= and lon= to your lat & long 

Go to https://www.latlong.net/ and enter your address as 123 Main St, Anytown, KS and click find. Be sure to enter your Lat and Long correctly.

-----

WeatherAlertCode

Visit https://alerts.weather.gov/. Scroll down and select your state and click County List. Change the WeatherAlertCode to your six digit county code.

-----

News Feeds

Copy the URL of the RSS feed and include the comma after every entry

-----

excludeList

This is a list of words that the program will check are in the RSS news feeds and exclude those results from appearing. Add a "word" followed by a comma on each line.

-----

SET loadMuisc = 1 to turn on Background Music. ADD LIST OF MP3 FILES TO playlist.lst

-----

Change cableCo = "ADELPHIA CABLE" to any value to display in the top left.

----------

Run by

$ bash start.sh
