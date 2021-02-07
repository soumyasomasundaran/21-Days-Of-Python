def key_generator(passcode):
    key_word = 0
    for letter in passcode:
        key_word = key_word + ord(letter)
    return key_word


print("The variable __name__ is ",__name__)

if __name__ == '__main__':
    print("The secret key for apple is")
    print(key_generator("apple"))
