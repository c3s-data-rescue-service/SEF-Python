
import pandas as pd
import os.path

import SEF_Pandas


THIS_PATH = os.path.abspath(os.path.dirname(__file__))
OUTPUT_FOLDER = os.path.join(THIS_PATH, 'output')
OUTPUT_PATH = os.path.join(OUTPUT_FOLDER, 'output_file.tsv')


def import_excel(input_file_path):
    dfs = pd.read_excel(input_file_path, skiprows=1)
    dfs = dfs.fillna('')
    records = [dict(row[1]) for row in dfs.iterrows()]
    record = []
    for record_id in records:
        record.append(record_id)

    return records


def create_output_file():

    input_path = "/PATH/FILE/example.xls"
    records = import_excel(input_path)
    obs = SEF_Pandas.create(records)

    SEF_Pandas.write_file(obs, OUTPUT_PATH)


if __name__ == "__main__":
    create_output_file()
