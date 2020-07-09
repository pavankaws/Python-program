#import IO
filename="D:\words.txt"
linecount=0
wordcount=0
charcount=0
with open(filename,'r') as File:
    for line in File:
        wordlist= line.split()
        linecount+=1
        wordcount=len(wordlist)
        charcount=len(line)
        #wordcount+=1
    print("No of words: "+str(wordcount))
    print("No of Lines: "+str(linecount))
    print("No of characters: "+str(charcount))
