import markdown
from flask import Flask
from flask import render_template
from flask import Markup


app = Flask(__name__)

@app.route('/')
def home():
    content = """
# Header

This is a test of the output stuff

* first
* second
    """
    
    content = Markup(markdown.markdown(content))
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run()
