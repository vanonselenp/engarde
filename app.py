import markdown
from flask import Flask
from flask import render_template
from flask import Markup
import sys


app = Flask(__name__)

def read_page(page):
    filename = "pages/%s.md" % page
    content = file(filename, 'r').read()
    content = markdown.markdown(content, extensions=['markdown.extensions.tables'])
    content = Markup(content)

    return content

@app.route('/')
def home():
    content = read_page('home')
    return render_template('index.html', content=content)

@app.route('/about', methods=['GET'])
def about():
    content = read_page('about')
    return render_template('index.html', content=content)

@app.route('/why', methods=['GET'])
def why():
    content = read_page('why')
    return render_template('index.html', content=content)

@app.route('/clubs', methods=['GET'])
def clubs():
    content = read_page('clubs')
    return render_template('index.html', content=content)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    app.run()
