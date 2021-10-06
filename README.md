# edtf-convert [![Build Status](https://github.com/unt-libraries/edtf-convert/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/unt-libraries/edtf-convert/actions)
A library for date format conversions involving Extended Date/Time Format (EDTF).
Currently support is only for EDTF to TEMPER.

## Installation
```sh
$ python setup.py install
```

## Usage

In Python:
```python
>>> from edtf_convert.edtf_to_temper import EDTFToTEMPER
>>> print(EDTFToTEMPER("2012-10-12").temper)
20121012
```

At the command line:
```sh
$ edtf-to-temper "[1980,1983-10-12,1990]"
1980, 1983, 1990
```
