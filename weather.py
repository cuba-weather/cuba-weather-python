#!/usr/bin/env python3

import urllib
import json

API = 'https://www.redcuba.cu/api/weather_get_summary/{location}'

class RCApiClient:
    
    def __init__(self, province):
        response = urllib.request.urlopen(API.format(location=province))
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
    c = RCApiClient("Provincia de Cienfuegos")
    print(c.getTemperature())

if __name__ == '__main__':
    main()
