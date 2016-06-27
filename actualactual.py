"""
ISDA Actual/Actual day count convention.
=====

Implemented according to 2006 ISDA definition:
http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf
"""

import calendar
import datetime


name = 'actual/actual'


def day_count(start_date, end_date):
    """Returns number of days between start_date and end_date, using Actual/Actual convention"""
    return (end_date - start_date).days


def year_fraction(start_date, end_date):
    """Returns fraction in years between start_date and end_date, using Actual/Actual convention"""
    if start_date == end_date:
        return 0.0
    if start_date > end_date:
        return - year_fraction(end_date, start_date)
    start_year = start_date.year
    end_year = end_date.year
    year_1_diff = 366 if calendar.isleap(start_year) else 365
    year_2_diff = 366 if calendar.isleap(end_year) else 365

    total_sum = end_year - start_year - 1
    diff_first = datetime.date(start_year + 1, 1, 1) - start_date
    total_sum += diff_first.days / year_1_diff
    diff_second = end_date - datetime.date(end_year, 1, 1)
    total_sum += diff_second.days / year_2_diff
    return total_sum
