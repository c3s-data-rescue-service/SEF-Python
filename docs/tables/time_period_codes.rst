:orphan:

Observation time period codes
=============================

|

=========  =======
Code       Meaning
=========  =======
0          instantanious value
p          since previous observation, but see below.
<x>year    *x* calendar years. If *x* is omitted, it defaults to 1, so 'year' is 1 year, '1year' is 1 year, 10year is 10 years. *x* must be an integer.
<x>month   *x* calendar months. If *x* is omitted, it defaults to 1, so 'month' is 1 month, '1month' is 1 month, 3month is 3 months. *x* must be an integer.
<x>day     *x* calendar days. If *x* is omitted, it defaults to 1, so 'day' is 1 day, '1day' is 1 day, 5day is 5 days. *x* must be an integer.
<x>hour    *x* hours. If *x* is omitted, it defaults to 1, so 'hour' is 1 hour, '1hour' is 1 hour, 5hour is 5 hours. *x* must be an integer.
<x>minute  *x* minutes. If *x* is omitted, it defaults to 1, so 'minute' is 1 minute, '1minute' is 1 minute, 60minute is  60 minutes. *x* must be an integer.
<x>second  *x* seconds. If *x* is omitted, it defaults to 1, so 'second' is 1 second, '1second' is 1 second, 86400second is 86,400 seconds. *x* must be an integer.
=========  =======


'p' is a convenience code to stop the user having to work out the period in seconds for each observation. It is mostly to support the very common case of approximately-daily precipitation observations. It will cause problems, however, if the previous observation is missing from the file. To deal with this, 'p' can be combined with another duration code giving the maximum expected duration between observations: so 'p1d' means 'since previous observation, if previous observation was <= 1 day ago; if the previous observation in the file was more than 1 day ago, assume an observation is missing'.

If the time period code 'p' is used at any point in a SEF file, the observations in that file must be in time order, starting with the earliest.

