# (e) List Comprehensions
#     ii. Square of N numbers.

N = int(input("Enter how many numbers: "))
square_list = [i*i for i in range(1, N+1)]
print("Squares of numbers:", square_list)