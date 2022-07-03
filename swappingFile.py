
def swapFileData():
    file1 = input("Enter the 1st FILE NAME:")
    file2 = input("Enter the 2nd FILE NAME:")

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file2, 'w') as b:
        b.write(data_a)

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file1, 'r') as a:
        data_a = a.read()


swapFileData()
     