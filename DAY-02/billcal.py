def personal_details(**kwargs):
     for key,value in kwargs.items():
         print(f"{key}:{value}")
name=input("enter the name:")
age=int(input("enter the age:"))
address=input("enter the address:")
mobile_number=input("enter the 10 digit phnnumber:")
masked=mobile_number[:2]+"******"+mobile_number[-2:]
print(personal_details(Name=name,Age=age,Address=address,Mobile_Number=masked))     
def trip_bills(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        total += value
    print("Total:", total)

bill1 = int(input("enter the transport cost:"))
bill2 = int(input("enter the food cost: "))
bill3 = int(input("enter other cost :"))

trip_bills(bill1=bill1, bill2=bill2, bill3=bill3)


          
     


