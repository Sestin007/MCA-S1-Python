# (a) Create a list of colors from comma-separated color names entered by the user.
#     Display first and last colors.

colors = input("Enter comma separated color names: ")
color_list = colors.split(",")
print("First color:", color_list[0])
print("Last color:", color_list[-1])