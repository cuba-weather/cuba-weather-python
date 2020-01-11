from json import loads
from urllib.parse import quote
from urllib.request import urlopen

try:
    from .finder import get_location
except:
    from finder import get_location
try:
    from .weather import Weather
except:
    from weather import Weather

URL = 'https://www.redcuba.cu/api/weather_get_summary/{location}'

class RCApiClient:

    def get(self, location: str) -> Weather:
        location = get_location(location)
        escaped_location = quote(location)
        url = URL.format(location=escaped_location)
        response = urlopen(url)
        content = response.read()
        if type(content) == bytes:
            content = content.decode()
        data = loads(content)['data']
        return Weather(data)
