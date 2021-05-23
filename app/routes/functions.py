import os
import time
import hashlib
import requests
import pandas as pd
from app import regions_api, regions_token, countries_api

basedir = os.path.abspath(os.path.dirname(__file__))

def getRegions():

    headers_regions = {
        'x-rapidapi-key': regions_token,
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
    }

    response = requests.request("GET", regions_api, headers=headers_regions)
    regions_data = response.json()
    regions = []

    for r in range(0, len(regions_data)):
        if regions_data[r]["region"] not in regions:
            regions.append(regions_data[r]["region"])

    return regions

def getCountries(regions):

    headers_countries = {
        'Content-Type' : "application/json"
    }

    countries = []

    for c in range(0, len(regions)-1):
        response = requests.request("GET", countries_api+regions[c], headers=headers_countries)
        data = response.json()

        for i in range(0, len(data)):
            countries.append(data[i])

    return countries

def createDataFrrame(countries):

    times = []
    df = pd.DataFrame(columns=['Region','City Name','Languaje'])

    for c in range(0, len(countries)):
        start = time.time()
        h = hashlib.new("sha1", bytes(countries[c]["languages"][0]["name"], encoding="ascii"))
        df = df.append({
            'Region': countries[c]["region"],
            'City Name': countries[c]["name"],
            'Languaje': h.hexdigest(),
        }, ignore_index=True)
        end = time.time()
        times.append(end - start)
    df['Time (seconds)'] = times
    df.to_json(os.path.join(basedir, '../../data.json'))
    times = []

    return df