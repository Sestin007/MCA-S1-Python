# (d) From a list of integers, create a new list after removing even numbers.

numbers = list(map(int, input("Enter integers: ").split()))
odd_list = [n for n in numbers if n % 2 != 0]
print("List after removing even numbers:", odd_list)