from flask import Flask
from module import demo
from flask_restplus import Api


app = Flask(__name__)
api = Api(title = 'myBNI API')

api.add_namespace(demo,path='/testing')
api.init_app(app)

if __name__=="__main__":
    app.run(port=5002, debug = True)
