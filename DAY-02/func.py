# def greet():
#     print("welcome to uber")
# greet() 

# def greet(name):
#     print(f"welcome to uber {name}")
# greet("pallavi")    

# def add(a,b):
#     return a+b
# res=add(5,20)
# print(res)

# def add_all(*args):
#     sum=0
#     for num in args:
#         sum+=num
#     return sum    

# print(add_all(1,2,3,4,5))

# def printdata(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# printdata(name="pallavi",age=21)        

def profile(**kwargs):
    list=[]
    for key,value in kwargs.items():
        list.append(f"{key}:{value}")
    return list    
name=input("enter the name:")
age=int(input("enter the age:"))
address=input("enter the address:")
print(profile(Name=name,Age=age,Address=address))
