# (C) British Crown Copyright 2017, Met Office
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

# Create an empty data structure corresponding to a Station Exchange 
#   Format (SEF) file

import pandas

def create(version='0.0.1'):
    """Create a data structure matching a SEF file

    Args:
        version (:obj:`str`): Semantic version of SEF to be supported

    Returns:
        :obj:`dict`: Data as key:value pairs.

   |
    """
 
    iversion=[int(x) for x in version.split('.')]
    if iversion[0]>0 or iversion[1]>0:
        raise IOError("SEF versions > 0.0 are not supported")
    result={'SEF'   : version,
            'ID'    : None,
            'Name'  : None,
            'Lat'   : None,
            'Lon'   : None,
            'Alt'   : None,
            'Source': None,
            'Repo'  : None,
            'Var'   : None,
            'Units' : None,
            'Meta'  : None,
            'Data'  : pandas.DataFrame({'Year' : None,
                                        'Month': None,
                                        'Day'  : None,
                                        'HHMM' : None,
                                        'TimeF': None,
                                        'Value': None,
                                        'Meta' : None},
                                       index=[0])}
    return result
    
 
