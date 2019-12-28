#!/usr/bin/env python3

import json
import urllib.parse
import urllib.request
from sys import argv
from urllib.error import HTTPError

API = 'https://www.redcuba.cu/api/weather_get_summary/{location}'


class RCApiClient:
    data = False

    def __init__(self, province):
        escaped_prov = urllib.parse.quote(province)
        url = API.format(location=escaped_prov)
        try:
            response = urllib.request.urlopen(url)
            content = response.read()
            if type(content) == bytes:
                content = content.decode()
            self.data = json.loads(content)
        except HTTPError as ex:
            print('No se ha encontrado la ciudad' if ex.code == 404 else ex)
            exit(-1)

    def getTemperature(self):
        return self.data['data']['temp']

    def getHumidity(self):
        return self.data['data']['humidity']

    def getPressure(self):
        return self.data['data']['pressure']

    def getGeneral(self):
        return self.data['data']['descriptionWeather']


def main():
    if len(argv) not in [2, 3]:
        print('Se requiere al menos un parámetro!')
        exit(-1)

    location = argv[1]
    response_format = argv[2] if len(argv) == 3 else False

    c = RCApiClient(location)
    if location and not response_format:
        print(c.getGeneral())
        print("Temperatura: {temp}°C".format(temp=c.getTemperature()))
        print("Humedad: {hum}%".format(hum=c.getHumidity()))
        print("Presión atmosférica: {hpa} hpa".format(hpa=c.getPressure()))
    elif response_format:
        print(response_format.format(temp=c.getTemperature(), hum=c.getHumidity(), hpa=c.getPressure()))


if __name__ == '__main__':
    try:
        main()
    except:
        pass
