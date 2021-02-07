def find_frequency(word_list):
    word_dictionary = {}
    for word in word_list:
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] = word_dictionary[word]+1
    return word_dictionary

def find_mrw(wordcount):
    max = 1
    for w,f in wordcount.items():
        if f > max:
            max = f
            max_word = w
    return max, max_word

s = "Fear is the path to the dark side. " \
    "Fear leads to anger. Anger leads to hate." \
    " Hate leads to suffering"

word_list = s.split(" ")
wordcount = find_frequency(word_list)
max_count, max_word = find_mrw(wordcount)
print("Most repeated word is -->",max_word)
print("Frequency is --->",max_count)