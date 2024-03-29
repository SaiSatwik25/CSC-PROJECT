# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
from newsapi import NewsApiClient
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
from flask import request

@app.route('/', methods=['GET', 'POST'])
def home():
    all_articles = None
    if request.method == 'POST':
        question = request.form.get('question')
        newsapi = NewsApiClient(api_key='98881c16be8d43e6b5621091f5268301')
        all_articles = newsapi.get_everything(q=question,
                                               language='en',
                                               from_param='2024-03-23',
                                               sort_by='popularity',
                                               page=1)
    return render_template('home.html', all_articles=all_articles)
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0", port=5000, debug=True)