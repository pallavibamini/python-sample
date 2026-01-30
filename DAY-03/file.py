# file=open("data.txt","w")
# file.write("Hello World")
# file.write("\nWelcome to Python")
# file.close()

# file=open("data.txt","r")
# content=file.read() 
# print(content)      
# file.close()

# file=open("data.txt","a")
# file.write("\nThis is an appended line.")
# file.close()

# with open("data.txt","r") as file:
#     content=file.read()
#     print(content)

#user feedback system
# def get_feedback():
#     with open("feedback.txt","a") as file:
#         feedback=input("Enter your feedback: ")
#         file.write(feedback+"\n")
#     print("Thank you for your feedback!")
# def view_feedback():
#     print("User Feedbacks:")
#     with open("feedback.txt","r") as file:
#         for line in file:
#             print("- "+line.strip())

# # Example usage
# get_feedback()      
# view_feedback()

# feedback=input("Enter your feedback: ")
# with open("feedback.txt","a") as file:
#     file.write(feedback+"\n")
# print("Thank you for your feedback!")  
# 
# 
# read line 
# def greet_user():
#     with open("user.txt","r") as file:
#         name=file.readline().strip()
#         print(f"Hello, {name}!")  

# with open("data.txt","r") as file:
#     print(file.readlines().strip()) 
#     print(file.readline().strip())
#     print(file.readline().strip())

# with open("data.txt","r") as file:
#    while True:
#        line=file.readline()
#        if not line:
#            break
#        print(line.strip())  

# with open("data.txt","r") as file:
#     for i in range(3):
#         print(file.readline().strip())

# # specific line 
# with open("data.txt","r") as file:
#     lines=file.readlines()
#     if len(lines)>=2:
#         print("Second line:",lines[1].strip())
#     else:
#         print("File has less than 2 lines.")