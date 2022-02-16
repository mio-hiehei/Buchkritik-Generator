from flask import Flask, render_template
from string import Template

app = Flask(__name__)

# http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/

from get_book_critique import *

BOOK_TITLE_TEMPLATE = Template("""
                <p style = "font-size:24px;">${book_title}</p>
                <p>von ${name}</p>
                <p>${sentence}</p>
""")

@app.route('/')
def homepage():

    book_critique = get_book_critique()
    book_title = book_critique["book_title"]
    name = book_critique["name"]
    sentence = book_critique["sentence"]

    return(render_template("index.html") + BOOK_TITLE_TEMPLATE.substitute(book_title= book_title,
                                           name = name,
                                           sentence = sentence)
    + """
                    <br>
                <a href='/..' class="button" >Blick ins Feuilleton!</a>
                         </body>
    
    """)



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
