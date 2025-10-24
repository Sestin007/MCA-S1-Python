age = int(input("Enter your age: "))
if age <= 5:
    print("Free Entry")
elif age <= 12:
    print("Ticket rate: ₹20")
elif age <= 60:
    print("Ticket rate: ₹50")
else:
    print("Ticket rate: ₹30")
