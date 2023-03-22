import json
from datetime import datetime
import dateutil.parser

#load data from data1.json
with open('data1.json') as f1:
    data_1 = json.load(f1)

#load data from data2.json
with open('data2.json') as f2:
    data_2 = json.load(f2)

#create a new JSON object to hold the unified data
unified_data = {}

unified_data['id'] = data_1['message']['id']
unified_data['text'] = data_1['message']['text']
unified_data['sender'] = {} 
unified_data['sender']['id'] = data_1['message']['sender']['id']
unified_data['sender']['name'] = data_1['message']['sender']['name']

time = data_2['message_timestamp']
parsed_time = dateutil.parser.parse(time)
timerstamp =parsed_time.timestamp() * 1000

unified_data['timestamp'] = str(int(timerstamp))
unified_data['confidence_score'] = data_2['confidence_score']

with open('unified_file.json','w') as f:
    json.dump(unified_data,f, indent=4)
print('successful')
