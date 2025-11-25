# (b) Write a program to generate Fibonacci series of N terms.

n = int(input("\nEnter the limit: "))
a = 0
b = 1

print("Fibonacci series upto", n, "terms:")
for i in range(n):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b