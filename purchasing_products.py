import json

fd = open("record.json",'r')

r = fd.read()

fd.close()

records = json.loads(r)

print("Available Inventory Products : ")

print(r)

ui_prod  = str(input("Enter the product_Id: "))

ui_quant = int(input("Enter the quantity: "))

if (ui_quant>records[ui_prod]['qn']):
	print("*******************************")
	print("WE ARE NOT HAVING THAT MUCH OF QUANTITY. PLEASE INPUT LESS THAN "+str(records[ui_prod]['qn']))
	print("*******************************")

print("Product: ",records[ui_prod]['name'])

print("Price: ",records[ui_prod]['pr'])

print("Billing Amount: ",records[ui_prod]['pr'] * ui_quant)

records[ui_prod]['qn'] = records[ui_prod]['qn'] - ui_quant

js = json.dumps(records) # Converting the data into text format.

fd = open("record.json",'w')

fd.write(js)

fd.close()

fd1 = open("sales.json",'r')

r1 = fd1.read()

fd1.close()

sale = json.loads(r1)

#print("Available Sales are : ")

print("Sales Database Updated Successfully..!!")


sale[(len(sale)+1)] = {"prod" : ui_prod, "qn" : ui_quant, "amount": records[ui_prod]['pr'] * ui_quant}

js1 = json.dumps(sale) # Converting the data into text format.

fd1 = open("sales.json",'w')

fd1.write(js1)

#print(sale)

fd1.close()