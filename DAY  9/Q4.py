def replace_char(original_string, o_char, r_char):
    replaced_string = original_string.replace(o_char, r_char)
    return replaced_string


sample_string = input("Enter the string:")
original = input("Enter the character to be replaced: ")
replacement = input("Enter the replacement character: ")
print(replace_char(sample_string, original, replacement))
