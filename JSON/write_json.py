import json

data = {
    "name": "Ray",
    "age": 40,
    "city": "Taipei"
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
