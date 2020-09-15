def first_half(even_string):
    return even_string[:int((len(even_string)) / 2)]


even_string = input("Enter the String: ")
print("First half is ", first_half(even_string))
