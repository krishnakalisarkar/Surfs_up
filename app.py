from flask import Flask
# Create a New Flask App Instance
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
@app.route('/India')
def hello_India():
    return 'Hello India'
@app.route('/India/Kolkata')
def hello_Kolkata():
    return 'Hello Kolkata'
 