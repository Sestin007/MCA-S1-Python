s = input("Enter a string: ")
ch = s[0]
s_new = ch + s[1:].replace(ch, '$')
print("Modified string:", s_new)
