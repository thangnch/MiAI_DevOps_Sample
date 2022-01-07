from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to DevOps oSHB<br><img src="https://www.shb.com.vn/wp-content/uploads/2016/03/Logo-SHB-VN.png" width="20%" border=1>'

    
if __name__ == '__main__':
   app.run(host='0.0.0.0')