try :
    fileObj = open("abc.txt","a")
    fileObj.write("Text inserted\n")
except :
    print("Some Error")