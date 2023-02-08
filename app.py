from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello, World!</>'

@app.route('/index')
@app.route('/home')
def home():
    return '<h1>Home Page!</h1>'

# This will run the app on http://localhost:5000
if __name__ == '__main__':
    # Run the app in local network
    app.run()