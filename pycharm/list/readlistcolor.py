# (b) Read two lists color-list1 and color-list2.
#     Print colors from color-list1 that are NOT in color-list2.

list1 = input("Enter colors for list1 (comma separated): ").split(",")
list2 = input("Enter colors for list2 (comma separated): ").split(",")
not_common = [c for c in list1 if c not in list2]
print("Colors in list1 not in list2:", not_common)