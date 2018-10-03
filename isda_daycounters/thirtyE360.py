"""
ISDA 30E/360 (euro bond basis) day count convention.
=====

Implemented according to 2006 ISDA definition:
https://www.isda.org/2008/12/22/30-360-day-count-conventions/
"""

name = 'thirtyE/360'


def day_count(start_date, end_date):
    """Returns number of days between start_date and end_date, using ThirtyE/360 convention"""
    d1 = min(30, start_date.day)
    d2 = min(30, end_date.day)

    return 360 * (end_date.year - start_date.year) \
           + 30 * (end_date.month - start_date.month) \
           + d2 - d1


def year_fraction(start_date, end_date):
    """Returns fraction in years between start_date and end_date, using Thirty/360 convention"""
    return day_count(start_date, end_date) / 360.0