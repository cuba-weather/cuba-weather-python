# cuba-weather

Python3 client for [redcuba.cu](https://www.redcuba.cu) weather API

## Usage

```
usage: weather.py [-h] [-v] [-t] [-u] [-p] [-g] location

positional arguments:
  location           Location name

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      Shows program version
  -t, --temperature  Shows location temperature
  -u, --humidity     Shows location humidity
  -p, --pressure     Shows location pressure
  -g, --general      Shows location general information
```

When just speciying the location and no other arguments, all the available information is displayed.

