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
            if ex.code == 404:
                raise Exception('No se ha encontrado la ciudad')
            else:
                raise ex

    def getTemperature(self):
        return self.data['data']['temp']

    def getHumidity(self):
        return self.data['data']['humidity']

    def getPressure(self):
        return self.data['data']['pressure']

    def getGeneral(self):
        return self.data['data']['descriptionWeather']