from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello, Muhammadtohir!</>'

@app.route('/index')
@app.route('/home')
def home():
    return '<h1> UY!</h1>'
@app.route('/about')
def about():
    return "<h1> O'qish </h1>" 
# This will run the app on http://localhost:5000
if __name__ == '__main__':
    # Run the app in local network
    app.run()