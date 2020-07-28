def wordscount():
    inputfile = open("D:\Words.txt")
    data = inputfile.read()
    numofchars= len(data)
    numofwords = len(data.split())
    numoflines = len(data.splitlines())
    print("numofchars " + str(numofchars) +", numofwords " +str(numofwords) +", numoflines " +str(numoflines))

wordscount()