import math
a=float(input("Enter value a:"))
b=float(input("Enter value b:"))
c=float(input("Enter value c:"))
d=(b)**2-((4*a)*c)
if(d>0):
    x=((-1*(b))-math.sqrt(d))/(2*(a))
    y=((-1*(b))-math.sqrt(d))/(2*(a))
    print("There are two roots:{x} and {y}")
    print("There are two roots:{round(x,2} and {round(y,2}")
elif d==0:
     z=(-1*(b))/(2*(a))
     print("There are only one root:{round(z,2)}")
else:
     print("There are no root because d is Negative")
         