from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to DevOps of Mi AI<br><img src="https://www.miai.vn/wp-content/uploads/2022/01/Logo_web-2-768x456.png">'

    
if __name__ == '__main__':
   app.run(host='0.0.0.0')