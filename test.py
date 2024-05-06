import json

filename = 'records.json'
# JSON data:
with open(filename, 'r') as f:
    json_data = json.load(f)

data = json_data

print(type(json_data))

# new_record = {'date': '2024-05-03', 'category': 'expense', 'amount': 500, 'descritpion': 'car'}



for record in data:
    for k, v in record.items():
        if k == 'Дата':
            print(record)

# with open(filename, 'w')as f:
#     json.dump(data, f, indent=2)