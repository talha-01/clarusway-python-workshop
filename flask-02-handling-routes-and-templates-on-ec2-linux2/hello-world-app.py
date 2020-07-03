
# https://github.com/callahan-cw/clarusway-python-workshop/blob/master/hands-on-flask-01-hello-world-app-on-ec2-linux2/flask-01-hello-world-app-on-ec2-linux2.md

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from Talha'

@app.route('/test')
def hello_test():
    return 'Hello World from Talha from the test page'

if __name__ ==  '__main__':
    app.run(debug = True)

