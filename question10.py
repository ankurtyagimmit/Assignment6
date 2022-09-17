'''a=int(input("Input first number:"))
b=int(input("Input second number:"))
c=int(input("input third number:"))
if(a>b and a>c):
    print(a,"is greater then",b,"and",c)
if(b>a and b>c):
     print(b,"is greater then",a,"and",c)
if(c>a and c>b):
     print(c,"is greater then",a,"and",b)  
else:
    print("All value are same")        
    print()'''
print("Enter three number:")
a,b,c=int(input()),int(input()),int(input())
print(( a if a>c else c) if a>b else (b if b>c else c))
