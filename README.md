# isda_daycounters
#### _ISDA day-count conventions with year-fractions and day-counts_

---

A very minimal ISDA day-count function collection, for the conventions _Actual/360_, _Actual/365_, _Actual/Actual_, and _Thirty/360_ as defined in [the 2006 ISDA definition guidelines](http://www.hsbcnet.com/gbm/attachments/standalone/2006-isda-definitions.pdf). 

Each day count convention is placed in its own module with both `day_count()` and `year_fraction()` functions, to leverage Python's treatment of modules as first-class objects. 

##### Why?

For a small instrument valuation tool I was working on in Python I needed ISDA-convention day counters, but didn't particularly feel like using Fincad or QuantLib Python bindings purely for day-count convention implementations for an otherwise independent project. 

---




