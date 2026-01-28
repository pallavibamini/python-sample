def check(email,password,name,age):
    if "@" not in email:
        return "invalid"
    if (len(password)<5):
        return "invalid"
    if (len(name)<2):
        return "invalid username"
    if not age.isdigit():
        return "invalid"   
    return "valid details "         




email=input("enter email : ")
password=input("enter password : ")
name=input("enter name :")
age=input("enter age : ")
print(check(email,password,name,age))