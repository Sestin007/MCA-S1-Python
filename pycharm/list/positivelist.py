# (e) List Comprehensions
#     i. Generate positive list of numbers from a given list of integers.

nums = list(map(int, input("Enter integers for positive filter: ").split()))
positive_list = [n for n in nums if n > 0]
print("Positive numbers:", positive_list)