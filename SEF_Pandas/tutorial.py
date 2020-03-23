
import pandas as pd
import os.path
import datetime
import codecs
import copy

from collections import defaultdict

THIS_PATH = os.path.abspath(os.path.dirname(__file__))
OUTPUT_FOLDER = os.path.join(THIS_PATH, 'output')
OUTPUT_PATH = os.path.join(OUTPUT_FOLDER, 'output_file.tsv')


def import_excel(input_file_path):
    """Import the Excel file as input file

    Args:
        :param input_file_path: Path of input file

    Returns:
        records (:obj:'list'): List of dict
    """

    dfs = pd.read_excel(input_file_path, skiprows=1)
    dfs = dfs.fillna('')
    records = [dict(row[1]) for row in dfs.iterrows()]
    record = []
    for record_id in records:
        record.append(record_id)

    return records


def create(records):
    """Create a data structure matching a SEF file

    Args:
        records (:obj:'str'): Semantic version of SEF to be supported

    Returns:
        :obj:'dict': Data as key:value pairs.
    """
    version = '1.0.0'

    iversion = [int(x) for x in version.split('.')]
    if iversion[1] > 0 or iversion[2] > 0:
        raise IOError("SEF versions > 0.0 are not supported")

    latitude = round(42 + 19 / 60 + 51.6 / 3600, 4)
    longitude = round(-(83 + 2 / 60 + 45.6 / 3600), 4)
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


def write_file(obs, file_name):
    """Write the specified set of obs to a file in SEF format.

    Args:
        obs (:obj: 'dict'): Dictionary
        file_name (:obj:'str'): File (or 'open'able object)

    Returns:
        :obj:'dict': Data as key:value pairs.

    Raises:
        ValueError: obs not a SEF structure
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


def create_output_file():
    """Create the output file

    """

    input_path = "/home/breno/Documentos/Yuri/example-python.xls"
    records = import_excel(input_path)
    obs = create(records)

    write_file(obs, OUTPUT_PATH)


if __name__ == "__main__":
    create_output_file()
