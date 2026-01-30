print("Welcome to Zomato")

try:
    item1=int(input("Enter price of item 1: "))
    item2=int(input("Enter price of item 2: "))
    item3=int(input("Enter price of item 3: "))

    if item1<=0 or item2<=0 or item3<=0:
        raise ValueError("Price cannot be negative")
    total=item1+item2+item3
    print("Total bill amount:", total)
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)       
finally:
    print("Thank you for visiting Zomato")







