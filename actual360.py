"""
ISDA Actual/360 day count convention.
=====

Implemented according to 2006 ISDA definition:
http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf
"""

name = 'actual/360'


def day_count(start_date, end_date):
    """Returns number of days between start_date and end_date, using Actual/360 convention"""
    return (end_date - start_date).days


def year_fraction(start_date, end_date):
    """Returns fraction in years between start_date and end_date, using Actual/360 convention"""
    return day_count(start_date, end_date) / 360.0
