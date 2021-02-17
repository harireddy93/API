# importing the required packages
import markdown
import os

#import framework
from flask import Flask
#from flask_restful import Resource,API,reqparse

#create a instance of flask
app = Flask(__name__)

#create a API
#api = API(app)

@app.route("/")
def hello():
    """ Need to our stuff which has to be communicated """
    # read the file
    with open(os.path.dirname(app.root_path)+ '/README.md','r') as target:
        #read the content in the file
        content = target.read()
        # convert to HTML
        return markdown.markdown(content)
