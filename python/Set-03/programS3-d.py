numbers = input("Enter numbers separated by spaces: ").split()

numbers = [int(n) for n in numbers]

result = []
for n in numbers:
    if n % 2 != 0:   
        result.append(n)

print("List after removing even numbers:", result)
