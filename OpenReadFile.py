
def OpenRead():
    try:
        #open the file
        file = open("sample1.txt","r")

        #read the file
        for line in file:
            print(line)

        file.close()
    except FileNotFoundError:
        print("The file 'sample.txt' not found")

