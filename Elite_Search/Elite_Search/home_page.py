from flask import Flask

app = Flask(__name__)

#connet a webpage
# froward slash means root directory
# give path in following argument of route method
@app.route('/')
def index():
    return "This is awesome."
