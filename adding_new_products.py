import json 

fd = open("record.json",'r')

r = fd.read()

fd.close()

print("Available Inventory Products :")

print(r) 

record = json.loads(r)

prod_id = str(input("Enter product id:"))

name = str(input("Enter name:"))

pr = int(input("Enter price:"))

qn = int(input("Enter quantity:"))

record[prod_id] = {'name': name, 'pr': pr, 'qn': qn}

js = json.dumps(record) 

fd = open("record.json",'w')

fd.write(js)

fd.close()

print("Updated Inventory :",js)