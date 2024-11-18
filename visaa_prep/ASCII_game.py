string = input()
new_string = ""
for i in string:
    if i.islower():
        new_string += i.upper()
    elif i.isupper():
        new_string += i.lower()
    else:
        new_string += i
print(new_string)
        
