with open('file_demo_read.txt', 'r') as fp:
    print(fp.read(10))
    print("The current position is ", fp.tell())
    fp.seek(0)
    print(fp.read())

