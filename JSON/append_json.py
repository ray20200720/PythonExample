import json

with open('data.json', 'r') as f:
    data = json.load(f)

new_data = { "new_key": "new_value" }    
    
if isinstance(data, list):
    data.append(new_data)
elif isinstance(data, dict):
    new_list = [data, new_data]
    data = new_list
else:
    raise TypeError("Data is not a list or a dictionary")

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
