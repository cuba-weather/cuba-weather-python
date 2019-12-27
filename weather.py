import urllib.request
import urllib.parse
import json

API = 'https://www.redcuba.cu/api/weather_get_summary/{location}'

class RCApiClient:
    
    def __init__(self, province):
        escapedProv = province.replace(' ', '%20')
        url = API.format(location=escapedProv)
        print(url)
        response = urllib.request.urlopen(url)
        self.data = json.loads(response.read())

    def getTemperature(self):
        return self.data['data']['temp']


    def getHumidity(self):
        return self.data['data']['humidity']

    def getPressure(self):
        return self.data['data']['pressure']

    def getGeneral(self):
        return self.data['data']['descriptionWeather']

def main():
    c = RCApiClient("Santa Clara")
    print(c.getTemperature())

if __name__ == '__main__':
    main()
