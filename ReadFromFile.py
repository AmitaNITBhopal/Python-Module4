try :
    fileObj = open("abc.txt","r")
    data = fileObj.read()
    print("Contents of the file are\n" + data)

except :
    print("Some Error Occured")