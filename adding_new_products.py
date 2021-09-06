import json 

fd = open("record.json",'r')

r = fd.read()

fd.close()

print("Available Inventory Products :")

print(r) 

record = json.loads(r)

prod_id = str(input("Enter Product ID:"))

name = str(input("Enter Name:"))

pr = int(input("Enter Price:"))

qn = int(input("Enter Quantity:"))

weight = int(input("Enter Weight:"))

diameter = int(input("Enter Diameter:"))

material = str(input("Enter Material:"))


record[prod_id] = {'product_name': name, 'product_price': pr, 'product_quantity': qn, 'product_weight': weight, 'product_diameter' : diameter, 'product_material' : material}

js = json.dumps(record) 

fd = open("record.json",'w')

fd.write(js)

fd.close()

print("------------------------------")
print("NEW PRODUCT HAS BEEN ADDED SUCCESSFULLY.")
print("------------------------------")
