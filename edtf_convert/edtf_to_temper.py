#!/usr/bin/env python
"""
Convert EDTF strings to TEMPER format.
Information about the Extended Date/Time Format can be found at:
http://www.loc.gov/standards/datetime/pre-submission.html
Information about the TEMPER format can be found at:
https://tools.ietf.org/html/draft-kunze-temper-01
"""
from __future__ import print_function
import argparse
import re


COMMA = re.compile(r'(?: *, *)')

# Any number of consecutive digits.
DATES = re.compile(r'\d+')

# Pattern to identify a TEMPER date. Pattern does not currently support
# timezones.
TEMPER = re.compile(r'^(?:(?:(?<![?])(?:bce|-)?\d{4,})[?]?~?(?:-|, (?=(?:bce|-)?\d{4,}))?)+$',
                    re.I)

# Dates with a season look like 2016-21.
SEASON_DATE = re.compile(r'(?<!\d)(\d{4})-2\d(?!\d)')

# Match dash between digits or uncertainty sign,
# but not negative sign.
DASH = re.compile(r'(?<=\d|[?])(-)(?=\d])?')

# Exactly six digits.
SIX_DIGITS = re.compile(r'(?<!\d)(\d{6})(?!\??\d)')

UNAVAILABLE = '(:unav) unavailable'

UNKNOWN = '(:unkn) unknown'


class EDTFToTEMPER:
    """Handles conversion of EDTF to TEMPER."""

    def __init__(self, edtf_date_str):
        self.edtf = edtf_date_str.strip()
        self.temper = self.make_temper()

    def make_temper(self):
        """Convert EDTF to TEMPER format."""
        if self.edtf.lower() == 'unknown':
            return UNKNOWN
        if self.edtf.startswith('[') or self.edtf.startswith('{'):
            # Handle lists of dates/date ranges.
            temper = self.edtf_list_to_temper()
        else:
            # Handle single date or date range.
            temper = self.convert_date_point(self.edtf)
        return self.validated_temper(temper)

    def validated_temper(self, date_str):
        """Verify date is TEMPER or return 'unavailable' value."""
        match = TEMPER.search(date_str)
        if match is not None:
            return match.group()
        else:
            return UNAVAILABLE

    def strip_list_chars(self):
        """Remove characters used in EDTF date lists."""
        strip_str = self.edtf
        for char in ['[', ']', '{', '}']:
            strip_str = strip_str.strip(char)
        return strip_str

    def edtf_list_to_temper(self):
        """Convert a list of EDTF dates to TEMPER."""
        date_str = self.strip_list_chars()
        # Standardize comma spacing.
        date_list = COMMA.split(date_str)
        comma_str = ', '.join([self.convert_date_point(x) for x in date_list])
        if UNAVAILABLE in comma_str:
            return UNAVAILABLE
        return self.adjust_date_lengths(comma_str)

    def adjust_date_lengths(self, date_list_str):
        """Adjust dates to the same precision.

        Finds the date with the shortest number of digits, and rewrites
        all dates to use that precision.
        """
        shortest = len(min(DATES.findall(date_list_str), key=len))
        shortest_matcher = re.compile(r'(?<!\d)(\d{%s})\d*' % str(shortest))
        return shortest_matcher.sub(r'\g<1>', date_list_str)

    def convert_date_point(self, date_point):
        """Convert EDTF date point to TEMPER."""
        date_point = date_point.lower()
        if '..' in date_point or ' - ' in date_point:
            date_point = self.standardize_range_syntax(date_point)
        if '/' in date_point:
            return self.convert_range(date_point)
        # Remove seasons and just use year.
        date_point = SEASON_DATE.sub(r'\g<1>', date_point)
        # Remove dashes delineateing year, month, day. Keep negative signs.
        date_point = DASH.sub('', date_point)
        # Zero pad yyyymm dates that are missing days.
        date_point = SIX_DIGITS.sub(r'\g<1>00', date_point)
        return date_point

    def standardize_range_syntax(self, date_point):
        """Standardize EDTF range/interval syntax.

        This simplifies conversion.
        """
        for syntax in ['..', ' - ']:
            date_point = date_point.replace(syntax, '/')
        return date_point

    def convert_range(self, edtf_range):
        """Convert EDTF range to TEMPER."""
        for uncertainty in ['open', 'unknown']:
            edtf_range = edtf_range.replace(uncertainty, '')
        range_dates = edtf_range.split('/')
        if range_dates[0] == '' or len(range_dates) > 2:
            # Do not convert open-start ranges;
            # they are indistinguishable from negative dates.
            # More than 2 dates is a malformed range.
            return UNAVAILABLE
        return '-'.join([self.convert_date_point(x) for x in range_dates])


def main():
    """Allow date string to be converted at command line."""
    description = ('Converts EDTF strings to TEMPER format.')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('datestr', type=str, help='date string')
    args = parser.parse_args()
    print(EDTFToTEMPER(args.datestr).temper)


if __name__ == '__main__':
    main()
