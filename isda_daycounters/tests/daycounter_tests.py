import datetime
from unittest import TestCase

from isda_daycounters import (actual360, actual365,
                              actualactual, thirty360)


class Actual360Test(TestCase):

    start_date = datetime.date(2010, 1, 13)
    end_date = datetime.date(2012, 1, 3)

    def test_day_count(self):
        """Test the day_count function"""

        # Case 1: test day count for same date
        self.assertEqual(
            actual360.day_count(self.start_date, self.start_date),
            0.0
        )

        # Case 2: test day count for arbitrary date difference
        self.assertEqual(
            actual360.day_count(self.start_date, self.end_date),
            720
        )

        # Case 3: test day count for negative date difference
        self.assertEqual(
            actual360.day_count(self.end_date, self.start_date),
            -720
        )

    def test_year_fraction(self):
        """Test the year_fraction function"""

        # Case 1: test year fraction for same date
        self.assertEqual(
            actual360.year_fraction(self.start_date, self.start_date),
            0.0
        )

        # Case 2: test year fraction for arbitrary date difference
        self.assertEqual(
            actual360.year_fraction(self.start_date, self.end_date),
            2.0
        )

        # Case 3: test year fraction for negative date difference
        self.assertEqual(
            actual360.year_fraction(self.end_date, self.start_date),
            -2.0
        )


class Actual365Test(TestCase):

    start_date = datetime.date(2010, 1, 13)
    end_date = datetime.date(2012, 1, 13)

    def test_day_count(self):
        """Test the day_count function"""

        # Case 1: test day count for same date
        self.assertEqual(
            actual365.day_count(self.start_date, self.start_date),
            0.0
        )

        # Case 2: test day count for arbitrary date difference
        self.assertEqual(
            actual365.day_count(self.start_date, self.end_date),
            730
        )

        # Case 3: test day count for negative date difference
        self.assertEqual(
            actual365.day_count(self.end_date, self.start_date),
            -730
        )

    def test_year_fraction(self):
        """Test the year_fraction function"""

        # Case 1: test year fraction for same date
        self.assertEqual(
            actual365.year_fraction(self.start_date, self.start_date),
            0.0
        )

        # Case 2: test year fraction for arbitrary date difference
        self.assertEqual(
            actual365.year_fraction(self.start_date, self.end_date),
            2.0
        )

        # Case 3: test year fraction for negative date difference
        self.assertEqual(
            actual365.year_fraction(self.end_date, self.start_date),
            -2.0
        )


class ActualActualTest(TestCase):

    start_date = datetime.date(2010, 1, 13)
    end_date = datetime.date(2014, 1, 13)

    def test_day_count(self):
        """Test the day_count function"""

        # Case 1: test day count for same date
        self.assertEqual(
            actualactual.day_count(self.start_date, self.start_date),
            0.0
        )

        # Case 2: test day count for arbitrary date difference
        self.assertEqual(
            actualactual.day_count(self.start_date, self.end_date),
            1461
        )

        # Case 3: test day count for negative date difference
        self.assertEqual(
            actualactual.day_count(self.end_date, self.start_date),
            -1461
        )

    def test_year_fraction(self):
        """Test the year_fraction function"""

        # Case 1: test year fraction for same date
        self.assertEqual(
            actualactual.year_fraction(self.start_date, self.start_date),
            0.0
        )

        # Case 2: test year fraction for arbitrary date difference
        self.assertEqual(
            actualactual.year_fraction(self.start_date, self.end_date),
            4.0
        )

        # Case 3: test year fraction for negative date difference
        self.assertEqual(
            actualactual.year_fraction(self.end_date, self.start_date),
            -4.0
        )


class Thirty360Test(TestCase):

    start_date = datetime.date(2010, 1, 13)
    end_date = datetime.date(2012, 1, 13)

    def test_day_count(self):
        """Test the day_count function"""

        # Case 1: test day count for same date
        self.assertEqual(
            thirty360.day_count(self.start_date, self.start_date),
            0.0
        )

        # Case 2: test day count for arbitrary date difference
        self.assertEqual(
            thirty360.day_count(self.start_date, self.end_date),
            720
        )

        # Case 3: test day count for negative date difference
        self.assertEqual(
            thirty360.day_count(self.end_date, self.start_date),
            -720
        )

    def test_year_fraction(self):
        """Test the year_fraction function"""

        # Case 1: test year fraction for same date
        self.assertEqual(
            thirty360.year_fraction(self.start_date, self.start_date),
            0.0
        )

        # Case 2: test year fraction for arbitrary date difference
        self.assertEqual(
            thirty360.year_fraction(self.start_date, self.end_date),
            2.0
        )

        # Case 3: test year fraction for negative date difference
        self.assertEqual(
            thirty360.year_fraction(self.end_date, self.start_date),
            -2.0
        )



