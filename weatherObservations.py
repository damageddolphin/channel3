import os
import urllib.request
from xml.etree.ElementTree import ElementTree

from setup import *


## Download weather XML file from NWS, change location code in setup.py
def loadWeather():
    try:
        os.remove('weatherObservations.xml')
        urllib.request.urlretrieve(weatherObservationURL, 'weatherObservations.xml')
    #            print("Removed and downloaded new observation file")
    finally:
        urllib.request.urlretrieve(weatherObservationURL, 'weatherObservations.xml')


#            print("Downloaded new observation file")
## Load XML into tree
def getWeather():
    global tree, weatherCredit
    global root
    tree = ""
    root = ""
    tree = ElementTree(file='weatherObservations.xml')
    root = tree.getroot()

    ## Parse XML tree into variables

    ## Get Location Name
    weatherTest = root.find('location')
    if weatherTest is not None:
        observationLocation = root.find('location').text
    else:
        observationLocation = "Not Reported"

    ## Get Last Update Info
    weatherTest = root.find('observation_time')
    if weatherTest is not None:
        observationTime = root.find('observation_time').text
    else:
        observationTime = "Unknown"

    ## Get Sky Conditions
    weatherTest = root.find('weather')
    if weatherTest is not None:
        currentSkys = root.find('weather').text
    else:
        currentSkys = "Not Reported"

    ## Get Last Reported Temperature
    weatherTest = root.find('temperature_string')
    if weatherTest is not None:
        currentTemperature = root.find('temperature_string').text
    else:
        currentTemperature = "Not Reported"

    ## Get Last Reported Dewpoint
    weatherTest = root.find('dewpoint_string')
    if weatherTest is not None:
        currentDewpoint = root.find('dewpoint_string').text
    else:
        currentDewpoint = "Not Reported"

    ## Get Last Reported Heat Indext - If not reported, use current temperature as feels like
    weatherTest = root.find('heat_index_string')
    if weatherTest is not None:
        currentHeatIndex = root.find('heat_index_string').text
    else:
        currentHeatIndex = root.find('temperature_string').text

    ## Get Last Reported Winds and concatenate
    currentWindDir = root.find('wind_dir')
    currentWindSpd = root.find('wind_mph')
    if currentWindDir is not None and currentWindSpd is not None:
        currentWind = root.find('wind_dir').text
        currentWind = currentWind + " " + root.find('wind_mph').text + " mph"
    else:
        currentWind = "Not Reported"

    ## Get Last Reported Wind Guests or if none Not Observed
    currentWindGusts = root.find('wind_gust_mph')
    if currentWindGusts is not None:
        currentWindGusts = root.find('wind_gust_mph').text + " mph"
    else:
        currentWindGusts = "Not Observed"

    ## Get Last Reported Humidity
    currentHumidityTest = root.find('relative_humidity')
    if currentHumidityTest is not None:
        currentHumidity = root.find('relative_humidity').text + " %"
    else:
        currentHumidity = "Not Reported"

    ## Get Last Reported Pressure in inHg and mb
    currentPressureTest = root.find('pressure_in')
    if currentPressureTest is not None:
        currentPressure = root.find('pressure_in').text + "\""
    else:
        currentPressure = "Not Reported"
    currentPressureTest = root.find('pressure_mb')
    if currentPressureTest is not None:
        currentPressure = currentPressure + " (" + root.find('pressure_mb').text + "mb)"

    ## Get Last Reported Visibility
    currentVisibilityTest = root.find('visibility_mi')
    if currentVisibilityTest is not None:
        currentVisibility = root.find('visibility_mi').text + " mi"
    else:
        currentVisibility = "Not Reported"

    ## Get Weather Source Info
    weatherCreditTest = root.find('credit')
    if weatherCreditTest is not None:
        weatherCredit = root.find('credit').text

    ## Retun Values
    return (observationLocation, observationTime, currentSkys, currentTemperature, currentDewpoint, currentHeatIndex,
            currentWind, currentWindGusts, currentHumidity, currentPressure, currentVisibility, weatherCredit)
