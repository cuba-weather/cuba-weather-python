#!/usr/bin/env python3

from urllib import request
import json

API = 'https://www.redcuba.cu/api/weather_get_summary/{location}'

class RCApiClient:
    def __init__(self, province):
        response = request.urlopen(API.format(location=province))
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
    c = RCApiClient("Provincia%20de%20Cienfuegos")
    print(c.getTemperature())

if __name__ == '__main__':
    main()
