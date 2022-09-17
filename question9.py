'''a=int(input("Enter Year:"))
if(a%4==0):
    print("Leap Year")
else:
    print("Not Leap Year") :'''
#print("Leap" if int(input("Enter year"))%4==0 else "Not")
#print("Not Leap year" if int(input("Enter year:"))%4 else"Leap Year")
print("Enter year:")
year=int(input())
if(year%400==0 or year%100!=0 and year%4==0):
    print("Leap year")
else:
    print("Not Leap year")

