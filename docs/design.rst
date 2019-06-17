Why do we need SEF?
===================

Weather data rescue is the process of getting historical weather observations off paper, into digital formats, and into use. This is typically done in two steps:

1. A *transcription* step which finds observations archived on paper and produces digital versions of those observations - typically as Excel spreadsheets or in a similar format.
2. A *database-building* step which converts the new digital observations into the format and `schema <https://en.wikipedia.org/wiki/Database_schema>`_ used by an observations database, and adds the observations to the database.

These two steps are usually done by different people: the first by a large group of observation experts (transcribers), each interested in a different set of to-be-digitised observations; the second by a small group of synthesisers trying to make the best possible database. The split between the steps causes problems: the output of step one (variably-structured Excel spreadsheets) is poorly suited as the input of step 2. We can't ask the transcribers to produce database-ready output, because this requires them to know too much about the precise and ideosyncratic details of each database, and we can't expect the synthesisers to work with millions of variably-structured Excel spreadsheets - partly because they would have to learn too much about the ideosyncrasies of each observation source, and partly because there are many fewer synthesisers than transcribers. The practical effect of this is that observations pile up in a transcribed-but-unusable state, and it takes too long to get them into use.

The Station Exchange Format (SEF) is a proposed new output for the transcription step. It will eliminate the bottleneck between the steps by specifying a single data format that's suitable both as the output of step one and the input to step 2. This means the format must have two, somewhat contradictory, properties:

A. It must be machine readable with NO human involvement – so it needs all the necessary metadata in an unambiguous arrangement. Otherwise it’s too expensive for synthesizers to read.
B. It must be easy for non-experts to read, understand, and create. In particular we need people to look at a couple of examples, think ‘OK, I can make that’ and get on with it, rather than “Oh, looks tricky, I won’t do that right now”. Otherwise it’s too expensive for transcribers to create.

If SEF is successful, 99% of users will be transcribers writing it, and the problems of reading it can be confined to a couple of software libraries. So it needs to be possible to read it unambiguously, but it doesn’t matter how slow or difficult this is – it matters a great deal if it’s hard to create. The best format will adequate for readers, but optimised for creators. That means plain text, editable in a text editor, editable in a spreadsheet format, opens in the right program when double clicked; easy to read and write in python, R, and even Fortran.

Success in data rescue means recruiting a lot of transcribers, and getting them to make SEF files. It's reasonable to assume that every difficulty given to the SEF creator will halve the number of people willing to put their data in the format (and so reduce the data we get). So SEF needs to be so simple that you don’t even need to read the instructions. In particular we need to protect SEF creators from the `Common Data Model <https://github.com/glamod/common_data_model/>`_ and all similar necessary complexities.

:doc:`The current design <SEF>` tries to be both simple enough to be obvious, and powerful enough to be useful, by having a core set of headers and columns which are obvious, and an arbitrarily extensible metadata section. Most users should be able to create a base SEF file by modifying a standard example without ever having to look up what any of the columns mean, and any community can customise the format to their precise requirements by specifying their own set of required metadata. Metadata standards can evolve with use, rather than being specified at the start.


