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

import datetime
import pandas as pd
from collections import defaultdict


def create(records):
    """Create a data structure matching a SEF file

    Args:
        records (:obj:`str`): Semantic version of SEF to be supported

    Returns:
        :obj:`dict`: Data as key:value pairs.

   |
    """
    version = '1.0.0'

    iversion = [int(x) for x in version.split('.')]
    if iversion[1] > 0 or iversion[2] > 0:
        raise IOError("SEF versions > 0.0 are not supported")

    latitude = 42.331
    longitude = -83.046
    altitude = 'NA'

    header = {
        'SEF': version, 'ID': 'Detroit_Anthon', 'Name': 'Detroit, MI',
        'Lat': latitude, 'Lon': longitude, 'Alt': altitude, 'Source': 'C3S-DRS',
        'Link': '', 'Vbl': 'ta', 'Stat': 'point',
        'Units': 'C', 'Meta': 'Observer=George Christian Anthon',
    }

    index_temperatures = 0
    index_times = 0

    time_offset = longitude * 12 / 180

    temp_dict = defaultdict(list)

    temperatures = []

    times = [datetime.time(7, 0), datetime.time(12, 0), datetime.time(20, 0)]
    original_time = ["7:00AM", "12:00PM", "20:00PM"]

    for index in range(len(records)):
        temperatures.append(records[index][datetime.time(7, 0)])
        temperatures.append(records[index][datetime.time(12, 0)])
        temperatures.append(records[index][datetime.time(20, 0)])
        for time in original_time:
            if isinstance(temperatures[index_temperatures], str):
                value = 'NA'
            else:
                value = round(((float(temperatures[index_temperatures]) - 32) * 5 / 9), 1)

            date = str(records[index]['Year']) \
                + "-" \
                + str(records[index]['Month']) \
                + "-" + str(records[index]['Day']) \
                + " " + str(times[index_times])

            date_time = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

            utc = date_time - datetime.timedelta(hours=time_offset)

            year = str(utc)[:4]
            month = str(utc)[5:7]
            day = str(utc)[8:10]
            hour = str(utc)[11:13]
            minutes = str(utc)[14:16]

            data_dict = {
                'Data': pd.DataFrame({
                    'Year': year,
                    'Month': month,
                    'Day': day,
                    'Hour': hour,
                    'Minute': minutes,
                    'Period': 0,
                    'Value': value,
                    'Meta': "orig=" + str(temperatures[index_temperatures])
                            + 'F' + "|orig.time=" + str(time)
                            + "|orig.date=" + str(records[index]['Year']) + '-' + str(records[index]['Month'])
                            + '-' + str(records[index]['Day'])

                }, index=[0])
            }
            temp_dict['Data'].append(data_dict['Data'])

            index_times += 1
            if index_times > 2:
                index_times = 0

            index_temperatures += 1

        header.update(temp_dict)

    return header
