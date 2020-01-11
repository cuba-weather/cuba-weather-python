from json import loads
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import urlopen

try:
    from .finder import get_location, get_suggestion
except:
    from finder import get_location, get_suggestion
try:
    from .weather import Weather
except:
    from weather import Weather

URL = 'https://www.redcuba.cu/api/weather_get_summary/{location}'

class RCApiClient:

    def get(self, location: str, suggestion=False) -> Weather:
        try:
            location = get_location(location)
            if suggestion:
                location = self.suggestion(location)
            escaped_location = quote(location)
            url = URL.format(location=escaped_location)
            response = urlopen(url)
            response = urlopen(url)
            content = response.read()
            if type(content) == bytes:
                content = content.decode()
            data = loads(content)['data']
            return Weather(data)
        except HTTPError as ex:
            if ex.code == 404:
                raise InvalidLocation(ex)
            else:
                raise Exception(ex)

    def suggestion(self, location: str) -> str:
        return get_suggestion(location)


class InvalidLocation(Exception):
    pass
