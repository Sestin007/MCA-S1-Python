# Function to find factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter the number of terms: "))
result = 0

for i in range(1, n + 1):
    f = fact(i)          
    term = (i ** i) / f  
    result += term

print("Sum of the series is:", result)
