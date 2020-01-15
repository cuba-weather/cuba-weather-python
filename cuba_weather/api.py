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
    '''
    Class to provide the functionality of making API requests.
    '''

    def get(self, location: str, suggestion=False) -> Weather:
        '''
        Method that given a location of the user searches the known locations to
        find the best match and returns the weather information. The best match
        is considered as the known location of shorter length that contains the
        given location.
        '''
        try:
            location = get_location(location)
            if suggestion:
                location = get_suggestion(location)
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
        return get_suggestion(get_location(location))


class InvalidLocation(Exception):
    pass
