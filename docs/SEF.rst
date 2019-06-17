The SEF File Format
===================

SEF files look like this:

.. literalinclude:: ../examples/basic.tsv

One SEF file contains observations of one variable from one station. It is a text file encoded as `UTF8 <https://en.wikipedia.org/wiki/UTF-8>`_. It is a `tab-separated values <https://en.wikipedia.org/wiki/Tab-separated_values>`_ file and should have a ``.tsv`` extension. This means it can be easily viewed and edited in any text editor or spreadsheet program (though care should be taken to preserve the tab structure and text encoding).

Header
------

The first 10 lines of the file are a series of headers, each given as a ``name``::``value`` pair separated by a tab. They must be in the order given. Missing values can be given as ``NA`` or left blank. The SEF version number must be present.

   ``SEF``:
   The first three characters in the file must be ``SEF``. The associated value is the `semantic version <https://semver.org/>`_ of the format used. This enables software to recognise the format and read the rest of the file correctly. At the moment, only version 0.2 is in use.

   ``ID``: 
   `WIGOS <http://www.wmo.int/pages/prog/www/wigos/index_en.html>`_ compatible station identifier. "The local identifier may be up to 16 characters long. It must not contain blanks [...]. The local identifier may contain only lower-case or upper-case Latin letters, numbers or the characters: - (dash), _ (underscore) or . (full stop)." (`Source <https://library.wmo.int/opac/doc_num.php?explnum_id=4007>`_). This is the *machine readable* name of the station.

   ``Name``:
   Station name - any string (except no tabs or carriage returns). This is the *human readable* name of the station.

   ``Lat``:
   Latitude of the station (degrees north). 

   ``Lon``:
   Longitude of the station (degrees east). 

   ``Alt``:
   Altitude of the station (meters above sea-level). 

   ``Source``:
   Source identifier. This is for making collections of SEF files and identifies a group of files from the same source. It will be set by the collector.  Any string (except no tabs or carriage returns).

   ``Link``:
   Where to find additional metadata (a `web address <https://en.wikipedia.org/wiki/URL>`_). SEF users are strongly recommended to add their data rescue projects to the `C3S DRS metadata registry <https://data-rescue.copernicus-climate.eu/registry>`_ and then link to the appropriate page in that service.

   ``Var``:
   Name of the variable included in the file. There is a :doc:`recommended list <tables/variable_names>` of standard variable names. Use this if possible.

   ``Stat``:
   What statistic (mean, max, min, ...) is reported from the variable. There is a :doc:`recommended list <tables/statistics>` of standard statistics. Use this if possible.

   ``Units``:
   Units in which the variable value is given (e.g. 'hPa', 'Pa', 'K', 'm/s'). Where possible, this should be compliant with `UDUNITS-2 <https://www.unidata.ucar.edu/software/udunits/>`_.

   ``Meta``:
   Anything else. Pipe-separated (|) string of metadata entries. Each entry may be any string (except no tabs, pipes, or carriage returns). There is a :doc:`standard list of meaningful entries <tables/metadata>`, but other entries can be added as necessary. Metadata specified here is assumed to apply to all observations in this file, unless overwritten by the observation-specific metadata entry.

Data table
----------

Lines 13 and onward in the file are a table of observations. Line 13 is a header, lines 14 and on are observations. Missing values can be given as ``NA`` or left blank. The table must contain these columns in this order:

   ``Year``: 
   Year in which the observation was made (UTC). An integer.

   ``Month``: 
   Month in which the observation was made (UTC). An integer (1-12).

   ``Day``: 
   Day of month in which the observation was made (UTC). An integer (1-31). 

   ``Hour``: 
   Hour at which the observation was made (UTC). An integer (0-23)

   ``Minute``: 
   Minute at which the observation was made (UTC). An integer (0-59)

   ``Period``:
   Time period of observation (instantanious, sum over previous 24 hours, ...). There is a :doc:`table of meaningful codes <tables/time_period_codes>`.

   ``Value``:
   The observation value.

   ``Meta``:
   Anything else. Pipe-separated (|) string of metadata entries. Each entry may be any string (except no tabs, commas, or carriage returns). There is a :doc:`standard list of meaningful entries <tables/metadata>`, but other entries can be added as necessary. Metadata specified here only applies to this observation, and overrides any file-wide specification.
