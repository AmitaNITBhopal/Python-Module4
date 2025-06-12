import json
from flask import Flask, render_template, request, redirect
import requests
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')
uri = MONGO_URI

var = Flask(__name__)


# Create a new client and connect to the server
client = MongoClient(uri)
db = client.test
collection = db['FlaskData']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


@var.route('/')
def indexMethod() :
    return render_template('index.html')

@var.route('/submitPage', methods=["POST"])
def submitPageMethod() :
    name = str(request.form.get('name'))
    password = str(request.form.get('passwordname'))
    responseData = dict(request.form)
    try :
        collection.insert_one(responseData)
        return redirect('/redirectedPage')

    except Exception as ex:
        return "Something went wrong here!" + str(ex)

    return ("hello " + name + ' ' + password)

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
    except Exception as ex:
        print ("Some Error in file")
        str = "Something went wrong" + str(ex)
    
    return str
    
@var.route('/redirectedPage')
def redirectedPageMethod() :
    return 'Data submitted successfully'

if __name__=='__main__' :
    var.run()