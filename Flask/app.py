import json
from flask import Flask
var = Flask(__name__)

@var.route('/api')
def method() :
    list1 = ["data1","data2", "data3","data4"]
    str = "default Data"
    try :
        fileObj = open("newFile.txt","a")
        fileObj.write(json.dumps(list1))
        fileObj.close

        fileReadObj = open("newFile.txt","r")
        str = fileReadObj.read()
        fileReadObj.close

        print(str)
    except :
        print ("Some Error in file")
    
    return str
    
if __name__=='__main__' :
    var.run()