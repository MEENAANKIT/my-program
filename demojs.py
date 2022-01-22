import json
data='{"vallay":"hello","name":"ankit","age":45}'
print(["age"])
parsed=json.loads(data)
print(parsed["name"])