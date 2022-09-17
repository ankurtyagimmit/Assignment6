'''a=str(input("Enter first word:"))
b=str(input("Enter second word:"))
if a<b:
    print(a,b)
elif b<a:
    print(b,a)'''
print("Enter two words")
a,b=input(),input()
print((b,a) if a>b else (a,b))
        
