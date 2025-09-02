import json 
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
data1 = {'name': 'Alice', 'age': 30}
json_str1 = json.dumps(data1, ensure_ascii=False)
print(json_str1)

print('--------------------------------------------')
data2 = json.loads(json_str)
print(type(data2))