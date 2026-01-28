
from tripbill import personal_details, trip_bills

name = input("Enter the name: ")
age = int(input("Enter the age: "))
address = input("Enter the address: ")
mobile_number = input("Enter the 10 digit phone number: ")

masked = mobile_number[:2] + "******" + mobile_number[-2:]

personal_details(
    Name=name.upper(),
    Age=age,
    Address=address,
    Mobile_Number=masked
)

print()   

bill1 = int(input("Enter transport cost: "))
bill2 = int(input("Enter food cost: "))
bill3 = int(input("Enter other cost: "))

trip_bills(bill1=bill1, bill2=bill2, bill3=bill3)
