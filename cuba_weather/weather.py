#!/usr/bin/env python3

import argparse
import json
import urllib.parse
import urllib.request
from urllib.error import HTTPError

__version__ = '0.0.2'

API = 'https://www.redcuba.cu/api/weather_get_summary/{location}'


class RCApiClient:
    data = False

    def __init__(self,location):
        escaped_location = urllib.parse.quote(location)
        url = API.format(location=escaped_location)
        try:
            response = urllib.request.urlopen(url)
            content = response.read()
            if type(content) == bytes:
                content = content.decode()
            self.data = json.loads(content)
        except HTTPError as ex:
            raise Exception('Location not found' if ex.code == 404 else ex)

    def getTemperature(self):
        return self.data['data']['temp']

    def getHumidity(self):
        return self.data['data']['humidity']

    def getPressure(self):
        return self.data['data']['pressure']

    def getGeneral(self):
        return self.data['data']['descriptionWeather']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('location', type=str, help='Location name')
    parser.add_argument("-v", "--version", help="Shows program version", action='store_true')
    parser.add_argument("-t", "--temperature", help="Shows location temperature", action='store_true')
    parser.add_argument("-u", "--humidity", help="Shows location humidity", action='store_true')
    parser.add_argument("-p", "--pressure", help="Shows location pressure", action='store_true')
    parser.add_argument("-g", "--general", help="Shows location general information", action='store_true')

    args = parser.parse_args()
    c = RCApiClient(args.location)
    if args.version:
        print("this is myprogram version 0.1")
    if args.general:
        print(c.getGeneral())
    if args.temperature:
        print("Temperature: {temp}°C".format(temp=c.getTemperature()))
    if args.humidity:
        print("Humidity: {hum}%".format(hum=c.getHumidity()))
    if args.pressure:
        print("Pressure: {hpa} hpa".format(hpa=c.getPressure()))

    if args.location and args.version == False and args.temperature == False and args.humidity == False and args.pressure == False and args.general == False:
        print(c.getGeneral())
        print("Temperature: {temp}°C".format(temp=c.getTemperature()))
        print("Humidity: {hum}%".format(hum=c.getHumidity()))
        print("Pressure: {hpa} hpa".format(hpa=c.getPressure()))


if __name__ == '__main__':
    main()
