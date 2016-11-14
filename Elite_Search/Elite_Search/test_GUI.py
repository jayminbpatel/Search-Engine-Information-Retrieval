from flask import Flask
#from home import *
from main_program import *
app = Flask(__name__)

#connet a webpage
# froward slash means root directory
# give path in following argument of route method
@app.route('/')
def index():
    return "This is awesome."

@app.route('/about')
def about():
    return "this is about"

@app.route('/profile/<username>')
def profile(username):
    return "hey there %s" % username

@app.route('/post/<int:post_id>')
def show(post_id):
    return "post id is %s" % post_id

@app.route('/results/<searchQuery>')
def search_query(searchQuery):
    results = main(searchQuery)
    display_html = "<html>"
    display_html += "<body>"
    for each_value in results:
        str(each_value).replace("\\","/")
        display_html += "<a href='file:///"+each_value+"'>"+each_value[31:]+"</a><br>"
    display_html += "</body>"
    display_html += "</html>"

    return display_html

if __name__ == "__main__":
    app.run(debug=True)