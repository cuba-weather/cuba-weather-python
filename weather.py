#!/usr/bin/env python3

import json
import urllib.parse
import urllib.request
from sys import argv

API = 'https://www.redcuba.cu/api/weather_get_summary/{location}'


class RCApiClient:

    def __init__(self, province):
        escaped_prov = urllib.parse.quote(province)
        url = API.format(location=escaped_prov)
        response = urllib.request.urlopen(url)
        content = response.read()
        if type(content) == bytes:
            content = content.decode()
        self.data = json.loads(content)

    def getTemperature(self):
        return self.data['data']['temp']

    def getHumidity(self):
        return self.data['data']['humidity']

    def getPressure(self):
        return self.data['data']['pressure']

    def getGeneral(self):
        return self.data['data']['descriptionWeather']


def main():
    if len(argv) != 2:
        print('Se requiere al menos un parámetro!')

    location = argv[1]

    if location:
        c = RCApiClient(location)
        print(c.getGeneral())
        print("Temperatura: {temp}°C".format(temp=c.getTemperature()))
        print("Humedad: {hum}%".format(hum=c.getHumidity()))
        print("Presión atmosférica: {hpa} hpa".format(hpa=c.getPressure()))


if __name__ == '__main__':
    main()
