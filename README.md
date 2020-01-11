# Cuba Weather

[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

Python3 client for [www.redcuba.cu](https://www.redcuba.cu) weather API.

## Install

```[bash]
pip install git+https://github.com/daxslab/cuba-weather
```

You can also clone or download this repository and at the root of the project do:

```[bash]
python setup.py install
```

## Usage

### CLI

```[bash]
usage: cuba-weather.py [-h] [-v] [-c] [-t] [-d] [-u] [-p] [-w] [-g] location

positional arguments:
  location           location name

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      show program version
  -c, --city-name    show location city name
  -t, --temperature  show location temperature
  -d, --timestamp    show location timestamp
  -u, --humidity     show location humidity
  -p, --pressure     show location pressure
  -w, --wind         show location wind
  -g, --general      show location general information
```

When just speciying the location and no other arguments, all the available information is displayed.

### Package

```[python3]
from cuba_weather import RCApiClient

api = RCApiClient()

weather = api.get(args.location, suggestion=True)

print(weather)
```
