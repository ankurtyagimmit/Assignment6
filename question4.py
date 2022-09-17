'''x=int(input("Enter first Value:"))
y=int(input("Enter second Value:"))
if(x>y):
    print(x,"Number is greater then",y)
if(x<y):
    print(y,"number is greater",x)
if(x==y):
    print("Given number are same")    
    print() '''
print("Enter two numbers")
a,b=int(input()),int(input())
print(a if a>b else b)
