# (e) Write a program to generate all factors of a number.
#     (Use while loop)

num = int(input("\nEnter a number: "))

i = 1
print(f"Factors of {num} are:")

while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1