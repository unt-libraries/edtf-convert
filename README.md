# edtf-convert [![Build Status](https://travis-ci.org/unt-libraries/edtf-convert.svg?branch=master)](https://travis-ci.org/unt-libraries/edtf-convert)
A library for date format conversions involving Extended Date/Time Format (EDTF).
Currently support is only for EDTF to TEMPER.

## Installation
```sh
$ python setup.py install
```

## Usage

In Python:
```python
>>> from edtf_to_temper import EDTFToTEMPER
>>> print(EDTFToTEMPER("2012-10-12").temper)
20121012
```

At the command line:
```sh
$ edtf-to-temper "[1980,1983-10-12,1990]"
1980, 1983, 1990
```
