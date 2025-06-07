
def writeNappend():
    strInput = input("enter the input")
    with open("output.txt","w") as f:
        f.write(strInput)
    f = open("output.txt","r")
    print(f.read())
    strAppend = input("enter the input")
    with open("output.txt","a") as f:
        f.write(strInput)
    f = open("output.txt","r")
    print(f.read())