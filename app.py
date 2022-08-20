from distutils.log import debug
from json.tool import main
from flask import Flask

app = Flask(__name__)


def getName():
    return {
        "name":"shubham"
    }

@app.route("/")
def hello_world():
    return getName()



if __name__=="__main__":
    app.run(debug=True)