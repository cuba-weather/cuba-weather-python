#!/usr/bin/env python3

import urllib.request
import urllib.parse
import json
from sys import argv

API = 'https://www.redcuba.cu/api/weather_get_summary/{location}'

class RCApiClient:

    def __init__(self, province):
        escapedProv = urllib.parse.quote(province)
        url = API.format(location=escapedProv)
        response = urllib.request.urlopen(url)
        self.data = json.loads(response.read())

    def getTemperature(self):
        return self.data['data']['temp']

    def getHumidity(self):
        return self.data['data']['humidity']

    def getPressure(self):
        return self.data['data']['pressure']

    def getGeneral(self):
        return self.data['data']['descriptionWeather']

def main():
    if len(argv) <= 1 or argv[1] == "--help":
        print("Uso: ./weather.py ubicación")
        return

    location = argv[1]

    if(location):
        c = RCApiClient(location)
        print(c.getGeneral())
        print("Temperatura: {temp}°C".format(temp=c.getTemperature()))
        print("Humedad: {hum}%".format(hum=c.getHumidity()))
        print("Presión atmosférica: {hpa} hpa".format(hpa=c.getPressure()))

if __name__ == '__main__':
    main()
