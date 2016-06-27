# isda_daycounters
####_ISDA day-count conventions with year-fractions and daycounts_

---

For a small instrument valuation tool I was working on in Python I needed ISDA-convention day counters, but didn't particularly feel like using Fincad or SWIG QuantLib purely for a day-count convention implementation. 

So here is a very minimal ISDA day-count function collection, for the conventions _Actual/360_, _Actual/365_, _Actual/Actual_, and _Thirty/360_ as defined in [the 2006 ISDA definition guidelines](http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf). 

Each day count convention is placed in its own module with both a `day_count` and `year_fraction` function, to leverage Python's treatment of modules as first-class objects. 

___TODO___: A bit more unit-testing if I get around to it. 


