"""
ISDA Actual/Actual day count convention.
=====

Implemented according to 2006 ISDA definition:
http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf
"""


name = 'thirty/360'


def day_count(start_date, end_date):
    """Returns number of days between start_date and end_date, using Thirty/360 convention"""
    return 360*(end_date.year - start_date.year)\
           + 30*(end_date.month - start_date.month - 1)\
           + max(0, 30 - start_date.day) + min(30, end_date.day)


def year_fraction(start_date, end_date):
    """Returns fraction in years between start_date and end_date, using Thirty/360 convention"""
    return day_count(start_date, end_date) / 360.0
