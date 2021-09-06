import json
import time
import datetime  


a_datetime = datetime.datetime.now()

formatted_datetime = a_datetime.isoformat()

json_datetime = json.dumps(formatted_datetime)

json_datetime = json_datetime.split("T")


fd = open("record.json",'r')

r = fd.read()

fd.close()

records = json.loads(r)

print("Available Inventory Products : ")

print(r)

ci_name = str(input("Enter the Customer's Name : "))

ui_prod  = str(input("Enter the Product Id: "))

ui_pname  = str(input("Enter the Product Name: "))

ui_price = int(input("Enter the Price : "))

ui_quant = int(input("Enter the Quantity: "))


if (ui_quant>records[ui_prod]['product_quantity']):
	print("*******************************")
	print("WE ARE NOT HAVING THAT MUCH OF QUANTITY. PLEASE INPUT LESS THAN "+str(records[ui_prod]['qn']))
	print("*******************************")


js = json.dumps(records) # Converting the data into text format.

fd = open("record.json",'w')

fd.write(js)

print("** PULKIT'S INVENTORY MANAGEMENT SYSTEM WELCOMES YOU ** ")

print("Customer's Name: ",ci_name)

print("Product ID : ",ui_prod)

print("Product Name : ",ui_pname)

print("Product Quantity : ",ui_quant)

print("Date $ Time : ",json_datetime)

print("Billing Amount: ",ui_price * ui_quant)

print("*******************************")
print("THANKS FOR SHOPPING. PLEASE VISIT AGAIN ")
print("*******************************")

records[ui_prod]['product_price'] = records[ui_prod]['product_quantity'] - ui_quant

fd1 = open("sales.json",'r')

r1 = fd1.read()

fd1.close()

fd.close()

sale = json.loads(r1)


#print("Available Sales are : ")

print("Sales Database Updated Successfully..!!")


sale[(len(sale)+1)] = {"Customer's Name" : ci_name,"Product's Id" : ui_prod, "Product's Name":ui_pname, "Quantity" : ui_quant, "Amount": ui_price * ui_quant, "Date $ Time" : json_datetime }

js1 = json.dumps(sale) # Converting the data into text format.

fd1 = open("sales.json",'w')

fd1.write(js1)

#print(sale)

fd1.close()
