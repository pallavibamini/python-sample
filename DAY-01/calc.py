def calc(a,b,op):
    if(op=='+'):
       return a+b
    elif(op=='-'):
        return a-b
    elif(op=='*'):
        return a*b
    elif(op=='/'):
        return a/b
a=int(input())
b=int(input())
op=input()        
print(calc(a,b,op))        
