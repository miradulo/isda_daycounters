"""
ISDA 30E/360 (ISDA) day count convention.
=====

Implemented according to 2006 ISDA definition:
https://www.isda.org/2008/12/22/30-360-day-count-conventions/
"""

import calendar

name = 'thirtyE/360 ISDA'

def day_count(start_date, end_date, is_end_date_on_termination=False):
    """Returns number of days between start_date and end_date, using ThirtyE/360 ISDA convention"""

    def is_last_day_of_feb(curr_date):
        if curr_date.month == 2:
            last_day_of_month = calendar.monthrange(curr_date.year, curr_date.month)[1]
            if curr_date.day == last_day_of_month:
                return True
        return False

    if start_date.day==31 or is_last_day_of_feb(start_date):
        d1 = 30
    else:
        d1 = start_date.day

    if end_date.day==31 or (is_last_day_of_feb(end_date) and not is_end_date_on_termination):
        d2 = 30
    else:
        d2 = end_date.day

    return 360 * (end_date.year - start_date.year) \
           + 30 * (end_date.month - start_date.month) \
           + d2 - d1


def year_fraction(start_date, end_date, is_end_date_on_termination=False):
    """Returns fraction in years between start_date and end_date, using Thirty/360 convention"""
    return day_count(start_date, end_date, is_end_date_on_termination) / 360.0