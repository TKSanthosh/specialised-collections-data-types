import pandas as pd
my_dict= {"san": "001", "tho": "002", "sh": "003"}
print(my_dict)
print(type(my_dict))

my_dict1= dict(san= "001", tho= "002", sh= "003")
print(my_dict1)
print(type(my_dict1))
emp_details={"Employee":{"santhosh":{"id":"001","salary":"80000"},
             "sandy":{"id":"002","salary":"70000"}}
             }
df = pd.DataFrame(emp_details["Employee"])
print(df)
