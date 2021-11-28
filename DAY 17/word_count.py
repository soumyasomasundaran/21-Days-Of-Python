def word_count(fp):
    wc = 0
    for line in fp:
        wc = wc + len(line.split(" "))
    return wc


with open('file_demo_read.txt', 'r') as fp:
    print(word_count(fp))
