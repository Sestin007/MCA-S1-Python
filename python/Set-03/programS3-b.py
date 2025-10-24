color_list1 = input("Enter colors for list1 separated by commas: ").split(',')
color_list2 = input("Enter colors for list2 separated by commas: ").split(',')

color_list1 = [color.strip() for color in color_list1]
color_list2 = [color.strip() for color in color_list2]

result = [color for color in color_list1 if color not in color_list2]

print("Colors from list1 not contained in list2:", result)
