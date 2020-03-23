#
# This code is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#

"""
This module provides a python API to newly-rescued weather observations in Station Exchange Format (SEF) files.

It provides three functions :func:`read_file`, :func:`write_file`, and :func:`create`:

.. code-block:: python

    import SEF
    obs=SEF.read_file('/wherever/Exeter_1811.tsv')

Will load the file contents as a :obj:`dict` that replicates the SEF file structure.

.. code-block:: python

    obs=SEF.create()
    # Add data and metadata to the obs structure
    SEF.write_file(obs,'/wherever/Exeter_new.tsv')

Will create the specified SEF file with the obs as specified. 
|
"""

from .create import *
from .read import *
from .write import *

