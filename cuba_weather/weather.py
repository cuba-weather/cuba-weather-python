from datetime import datetime


class Weather:
    '''
    Model class for mapping the json returned by the https://www.redcuba.cu
    weather API.
    '''

    def __init__(self, data: dict):
        self.data = data

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
    def temperature_fahrenheit(self) -> str:
        return (self.data['temp'] * 9/5) + 32

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

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        result = 'City Name: {city_name}\n'
        result += 'Temperature: {temp}°C / {temp_f}°F\n'
        result += 'Timestamp: {timestamp}\n'
        result += 'Humidity: {hum}%\n'
        result += 'Pressure: {hpa} hpa\n'
        result += 'Wind: {wind}\n'
        result += '{general}'
        result = result.format(
            city_name=self.city_name,
            temp=self.temperature,
            temp_f=self.temperature_fahrenheit,
            timestamp=self.timestamp,
            hum=self.humidity,
            hpa=self.pressure,
            wind=self.wind,
            general=self.general)
        return result
