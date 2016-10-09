import markdown
from flask import Flask
from flask import render_template
from flask import Markup
import sys


app = Flask(__name__)

@app.route('/')
def home():
    content = file('pages/home.md', 'r').read()
    content = markdown.markdown(content)
    #content = markdown.markdownFromFile('pages/home.md')
    content = Markup(content)

    return render_template('index.html', content=content)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    app.run()
