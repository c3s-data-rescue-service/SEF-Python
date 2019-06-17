
import SEF

records = {'ID': 'DWR_Zarate', 'Name': 'Zárate', 'Source': 'NA', 'Lat': '-34.0958', 'Lon': -59.0242,
           'Link': 'https://data-rescue.copernicus-climate.eu/lso/1086267', 'Vbl': 'msl pressure', 'Stat': 0,
           'Units': 'hPa', 'Meta': 'Alias=Zarate|PTC=T|PGC=?|Data policy=Open', 'Year': [2000, 2000], 'Month': [1, 2], 'Day': [2, 3],
           'Hour': [10, 11], 'Minute': [20, 31], 'Value': [0, 1], 'Period': [0, 1], 'Meta2': ['Orig.=754.5mm|Orig.time=', 'Orig.=754.5mm|Orig.time='],
           'orig_time': ['14:00', '14:00']}

obs = SEF.create(records)

SEF.write_file(obs, '/PATH/SEF-master/examples/output.tsv')
