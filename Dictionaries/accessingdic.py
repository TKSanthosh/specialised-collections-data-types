my_dict= {"san": "001", "tho": "002", "sh": "003"}
print(my_dict)

#printing keys
print(my_dict.keys())

#printing values
print(my_dict.values())

#printing specific value
print(my_dict.get("san"))

#accessing using for loop
for x in my_dict:
    print(x)

for y in my_dict.values():
    print(y)

for x,y in my_dict.items():
    print(x,y)