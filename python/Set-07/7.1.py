def calculate(p,n,r):
 s = (p*n*r)/100
 print("simple intrest=",s)
age=int(input("enter the age:"))
p=int(input("enter the principle amount:"))
n=int(input("enter the number of years:"))
if age<60:
 r=10
else:
 r=12
print("rate of intrest:",r)
calculate(p,n,r)