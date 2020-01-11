#!/usr/bin/env python3

from argparse import ArgumentParser
from datetime import datetime
from json import loads
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import urlopen

from finder import get_location

__version__ = '0.0.8'

API = 'https://www.redcuba.cu/api/weather_get_summary/{location}'

class RCApiClient:

    def __init__(self, location: str):
        location = get_location(location)
        escaped_location = quote(location)
        url = API.format(location=escaped_location)
        response = urlopen(url)
        content = response.read()
        if type(content) == bytes:
            content = content.decode()
        self.data = loads(content)['data']

    @property
    def city_name(self) -> str:
        return self.data['cityName']

    @property
    def timestamp(self) -> datetime:
        datetime_str = self.data['dt']['date']
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')

    @property
    def temperature(self) -> str:
        return self.data['temp']

    @property
    def humidity(self) -> str:
        return self.data['humidity']

    @property
    def pressure(self) -> str:
        return self.data['pressure']

    @property
    def wind(self) -> str:
        return self.data['windstring']

    @property
    def general(self) -> str:
        return self.data['descriptionWeather']


def main():
    parser = ArgumentParser()
    parser.add_argument('-v', '--version', help='show program version', action='store_true')

    args = parser.parse_args()

    if args.version:
        print(__version__)
        return

    parser.add_argument('location', type=str, help='location name')
    parser.add_argument('-c', '--city-name', help='show location city name', action='store_true')
    parser.add_argument('-t', '--temperature', help='show location temperature', action='store_true')
    parser.add_argument('-d', '--timestamp', help='show location timestamp', action='store_true')
    parser.add_argument('-u', '--humidity', help='show location humidity', action='store_true')
    parser.add_argument('-p', '--pressure', help='show location pressure', action='store_true')
    parser.add_argument('-w', '--wind', help='show location wind', action='store_true')
    parser.add_argument('-g', '--general', help='show location general information', action='store_true')

    args = parser.parse_args()

    try:
        c = RCApiClient(args.location)
    except HTTPError as ex:
        if ex.code == 404:
            print('Location not found, try checking your orthography or use a near by location.')
        else:
            raise Exception(ex)
        return

    if args.general:
        print(c.general)
    if args.city_name:
        print('City Name: {city_name}'.format(city_name=c.city_name))
    if args.temperature:
        print('Temperature: {temp}°C'.format(temp=c.temperature))
    if args.timestamp:
        print('Timestamp: {timestamp}'.format(timestamp=c.timestamp))
    if args.humidity:
        print('Humidity: {hum}%'.format(hum=c.humidity))
    if args.pressure:
        print('Pressure: {hpa} hpa'.format(hpa=c.pressure))
    if args.wind:
        print('Wind: {wind}'.format(wind=c.wind))

    params = [
        args.version,
        args.city_name,
        args.temperature,
        args.timestamp,
        args.humidity,
        args.pressure,
        args.wind,
        args.general
    ]

    if args.location and not any(params):
        print(c.general)
        print('City Name: {city_name}'.format(city_name=c.city_name))
        print('Temperature: {temp}°C'.format(temp=c.temperature))
        print('Timestamp: {timestamp}'.format(timestamp=c.timestamp))
        print('Humidity: {hum}%'.format(hum=c.humidity))
        print('Pressure: {hpa} hpa'.format(hpa=c.pressure))
        print('Wind: {wind}'.format(wind=c.wind))


if __name__ == '__main__':
    main()
