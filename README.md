# cuba-weather

Python3 client for [redcuba.cu](https://www.redcuba.cu) weather API

## Install

`pip install git+https://github.com/daxslab/cuba-weather`

## Usage

```
usage: cuba-weather [-h] [-v] [-t] [-u] [-p] [-g] location

positional arguments:
  location           Location name

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      Shows program version
  -t, --temperature  Shows location temperature
  -u, --humidity     Shows location humidity
  -p, --pressure     Shows location pressure
  -w, --wind         Shows location wind condition
  -g, --general      Shows location general information
```

When just speciying the location and no other arguments, all the available information is displayed.

