import json

with open('records.json', 'r') as file:
    data = json.load(file)['records']




# r = [{**record, "amount": -record["amount"]} if record["category"] == "Расход" else record for record in data]

r = [-record['amount'] if record['category'] == 'Расход' else record['amount'] for record in data]
print(r)