travelling = input("Do you gonna to travel - Yes or NO ")
while travelling == "Yes":
    n= int(input("How many of them travelling"))
    for x in range(1,n+1):
        name=input("Name: ")
        age=input("Age: ")
        sex=input("Sex: Male or Female ")
        print(name,age,sex)
    travelling =str(input("Did you forget anyone? Yes or No "))
