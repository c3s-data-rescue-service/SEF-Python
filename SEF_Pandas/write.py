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

# Store a set of weather observations in a Station Exchange Format (SEF) file

import codecs
import copy


def write_file(obs, file_name):
    """Write the specified set of obs to a file in SEF format.

    Args:
        obs (:obj:`dict`): Dictionary
        file_name (:obj:`str`): File (or 'open'able object)

    Returns:
        :obj:`dict`: Data as key:value pairs.

    Raises:
        ValueError: obs not a SEF structure

    |
    """
    try:    
        version = obs['SEF']
        iversion = [int(x) for x in version.split('.')]

        if iversion[1] > 0 or iversion[2] > 0:
            raise IOError("SEF versions > 0.0 are not supported")
    except:
        raise ValueError("This does not look like a SEF data structure")

    # Operate on local copy
    obs = copy.deepcopy(obs)
    f = codecs.open(file_name, 'w', encoding='utf-8')
    # Meta might need packing
    obs['Meta'] = _pack(obs['Meta'])
    # Header first
    for header in ('SEF', 'ID', 'Name', 'Source', 'Lat', 'Lon', 'Alt', 'Link', 'Vbl',
                   'Stat', 'Units', 'Meta'):
        if obs[header] is not None and obs[header] == obs[header]:

            f.write("%s\t%s\n" % (header, obs[header]))
        else:
            f.write("%s\t\n" % header)

    # Add the data table
    # obs['Data']['Meta'] = obs['Data']['Meta'].map(_pack, na_action='ignore')

    obs['Data'][0].to_csv(f, sep='\t', header=True, index=False)

    for i in range(1, len(obs['Data'])):
        obs['Data'][i].to_csv(f, sep='\t', header=False, index=False,)


def _pack(m_list):
    if m_list is None:
        return m_list
    elif isinstance(m_list, str):
        return m_list
    else:
        return ','.join(m_list)
