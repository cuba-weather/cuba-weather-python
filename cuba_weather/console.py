#!/usr/bin/env python3

from argparse import ArgumentParser

try:
    from .api import InvalidLocation, RCApiClient
except:
    from api import InvalidLocation, RCApiClient

__version__ = '0.0.9'


def main():
    api = RCApiClient()

    parser = ArgumentParser()
    parser.add_argument('location', type=str, help='location name')
    parser.add_argument('-v', '--version', help='show program version', action='store_true')
    parser.add_argument('-weather', '--city-name', help='show location city name', action='store_true')
    parser.add_argument('-t', '--temperature', help='show location temperature', action='store_true')
    parser.add_argument('-d', '--timestamp', help='show location timestamp', action='store_true')
    parser.add_argument('-u', '--humidity', help='show location humidity', action='store_true')
    parser.add_argument('-p', '--pressure', help='show location pressure', action='store_true')
    parser.add_argument('-w', '--wind', help='show location wind', action='store_true')
    parser.add_argument('-g', '--general', help='show location general information', action='store_true')

    args = parser.parse_args()

    if args.version:
        print(__version__)
        return

    try:
        weather = api.get(args.location)
    except InvalidLocation:
        suggestion = api.suggestion(args.location)
        print('Location not found, maybe you are asking about {suggestion}.'.format(suggestion=suggestion))
        return

    if args.general:
        print(weather.general)
    if args.city_name:
        print('City Name: {city_name}'.format(city_name=weather.city_name))
    if args.temperature:
        print('Temperature: {temp}°C'.format(temp=weather.temperature))
    if args.timestamp:
        print('Timestamp: {timestamp}'.format(timestamp=weather.timestamp))
    if args.humidity:
        print('Humidity: {hum}%'.format(hum=weather.humidity))
    if args.pressure:
        print('Pressure: {hpa} hpa'.format(hpa=weather.pressure))
    if args.wind:
        print('Wind: {wind}'.format(wind=weather.wind))

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
        print(weather)


if __name__ == '__main__':
    main()
