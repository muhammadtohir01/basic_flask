from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """jhgvilgv;kjghiu"""
if __name__ == '__main__':
    # Run the app in local network
    app.run()