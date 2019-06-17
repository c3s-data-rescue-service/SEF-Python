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

from collections import defaultdict

dict_keys = {
        'Id',
        'Name',
        'Source',
        'Lat',
        'Lon',
        'Alt',
        'Link',
        'Vbl',
        'Vbl',
        'Stat',
        'Units',
        'Meta',
        'Year',
        'Month',
        'Day',
        'Hour',
        'Minute',
        'Period',
        'Value',
        'Meta2',
        'time_offset',
        'orig_time',
    }


def create(records):
    """Create a data structure matching a SEF file

    Args:
        records (:obj:`str`): Semantic version of SEF to be supported

    Returns:
        :obj:`dict`: Data as key:value pairs.

   |
    """
    version = '0.2.0'

    iversion = [int(x) for x in version.split('.')]
    if iversion[0] > 0 or iversion[2] > 0:
        raise IOError("SEF versions > 0.0 are not supported")

    temp_dict = {}

    for k, v in records.items():
        temp_dict.update({k.capitalize(): v})

    for key in dict_keys:
        if key not in temp_dict:
            temp_dict[key] = 'NA'
        else:
            temp_dict.update(records.items())

    result = {
            'SEF': version, 'ID': temp_dict['Id'], 'Name': temp_dict['Name'],
            'Source': temp_dict['Source'], 'Lat': temp_dict['Lat'], 'Lon': temp_dict['Lon'],
            'Alt': temp_dict['Alt'], 'Link': temp_dict['Link'], 'Vbl': temp_dict['Vbl'],
            'Stat': temp_dict['Stat'], 'Units': temp_dict['Units'], 'Meta': temp_dict['Meta'],
        }

    d = defaultdict(list)
    for i in range(len(temp_dict['Year'])):
        temp_result = {
                    'Data': pandas.DataFrame({
                        'Year': temp_dict['Year'][i],
                        'Month': temp_dict['Month'][i],
                        'Day': temp_dict['Day'][i],
                        'Hour': temp_dict['Hour'][i],
                        'Minute': temp_dict['Minute'][i],
                        'Period': temp_dict['Period'][i],
                        'Value': temp_dict['Value'][i],
                        'Meta': temp_dict['Meta2'][i] + str(temp_dict['orig_time'][i])
                    }, index=[0])
                }
        d['Data'].append(temp_result['Data'])

    result.update(d)
    return result
