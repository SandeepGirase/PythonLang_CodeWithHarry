import json

data = '{"var1":"harry", "var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))
print(parsed)

dada2 = {
    "channel_name":"Codewithharry",
    "Cars":['bmw', 'audi', 'farrary'],
    "fridge":('roti', 540),
    "isbad":False
}
jscomp = json.dumps(dada2)
print(jscomp)
