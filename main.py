from flask import Flask, render_template
from string import Template

app = Flask(__name__)

# http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/

from get_book_critique import *
from create_word_lists import *



BOOK_TITLE_TEMPLATE = Template("""
                <h2> ${book_title} </h2>
                <h3>von ${name}</h3>
                <p>${sentence}</p>
""")

@app.route('/')
def homepage():

    book_critique = get_book_critique(
        book_title_list=book_title_list,
                      adjective_list = adjective_list,
                      objekt_list = objekt_list,
                      verb_list = verb_list,
                      was_list = was_list,
                      wessen_list = wessen_list,
                      wowann_list = wowann_list)

    book_title = book_critique["book_title"]
    name = book_critique["name"]
    sentence = book_critique["sentence"]

    return(render_template("index.html") + BOOK_TITLE_TEMPLATE.substitute(book_title= book_title,
                                           name = name,
                                           sentence = sentence)
    + """
                    <br>
                <a id="button" href='/..' class="button" >Blick ins Feuilleton!</a>
                         </body>
    
    """)



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
