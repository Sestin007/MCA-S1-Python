# (c) Prompt user for a list of integers.
#     For all values greater than 100, store the word 'over' instead.

nums = input("Enter integers separated by space: ").split()
updated = []
for n in nums:
    n = int(n)
    if n > 100:
        updated.append("over")
    else:
        updated.append(n)
print("Updated list:", updated)