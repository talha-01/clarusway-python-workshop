from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from Talha'

@app.route('/test')
def hello_test():
    return 'Hello World from Talha from the test page'

if __name__ ==  '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)
