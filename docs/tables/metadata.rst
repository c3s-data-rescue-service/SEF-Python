:orphan:

Standard CEF metadata entries
=============================

The metadata line is deliberately flexible - it's OK to use it for anything, as required. But we should standardise, where possible, on common entries.

|

=====================          ============ =======
Flag                           Values       Meaning
=====================          ============ =======
Orig.                          =any         Original observation value (e.g. '33F, or 29.78in')
Orig. date                     =any         Original observation date (e.g. '23 September 1902')
Orig. time                     =any         Original observation time (e.g. '14:00' or '2:30').
PTC                            =[Y,N,?]     Pressure temperature corrected (Yes,No,unknown)
Alias                          =any         Alternative station name
Data policy                    =any         Data licence, e.g. 'WMO essential', see `here <https://github.com/glamod/common_data_model/blob/master/tables/data_policy_licence.dat>`_ for some examples
=====================          ============ =======
