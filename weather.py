#!/usr/bin/env python3

import argparse
import json
import urllib.parse
import urllib.request
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
            raise Exception('No se ha encontrado la ciudad' if ex.code == 404 else ex)

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
    parser.add_argument('province', type=str, help='Province name')
    parser.add_argument("-v", "--version", help="Shows program version", action='store_true')
    parser.add_argument("-t", "--temperature", help="Shows province temperature", action='store_true')
    parser.add_argument("-u", "--humidity", help="Shows province humidity", action='store_true')
    parser.add_argument("-p", "--pressure", help="Shows province pressure", action='store_true')

    args = parser.parse_args()
    c = RCApiClient(args.province)
    if args.version:
        print("this is myprogram version 0.1")
    if args.temperature:
        print("Temperatura: {temp}°C".format(temp=c.getTemperature()))
    if args.humidity:
        print("Humedad: {hum}%".format(hum=c.getHumidity()))
    if args.pressure:
        print("Presión atmosférica: {hpa} hpa".format(hpa=c.getPressure()))


if __name__ == '__main__':
    main()
