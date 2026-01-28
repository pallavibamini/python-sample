print("hello") 
"""print("comments ")"""
'''print("comments ")'''


# """ data types  int, float, String, bool, list, tuple(immutable ), set(unique vaules , unordered), dict (key-value pairs )"""
a=10
print(type(a))

b=float(input())
print(type(b))

a=13
b=30
print(a+b)

 #four parameters 

 #with parameter with return type
 def add(a,b):
    c=a+b
    return c 
a=10
b=20
res=add(a,b)
print(res)    
  #withoout parameter with return type
 def add():
    a,b=10,20
    c=a+b
    return c 

res=add(a,b)
print(res)      

 #with parameter without return type

  def add(a,b):
   
    c=a+b
    print(c)
a,b=10,20
add(a,b)
   
 #without parameter without return type 
 def add():
    c=a+b
    print(c)
a,b=10,20

add()
   
