from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, first DevOps app from Mi AI! Auto deploy!'

    
if __name__ == '__main__':
   app.run(host='0.0.0.0')