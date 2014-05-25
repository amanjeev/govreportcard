import os
import sys
from flask import Flask, render_template
import copytext

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), './'))

app = Flask(__name__)
app.debug = True


@app.route('/')
def main():
    copy = copytext.Copy(os.path.join(PROJECT_ROOT, 'data/2014_bjp_manifesto.xlsx'))
    context = {
        'COPY' : copy,
        'title': 'Home',
        'page_title' : 'Manifesto items'
    }
    return render_template('index.html', **context)


@app.route('/manifesto/<id>/')
def manifesto_item(id):
    copy = copytext.Copy(os.path.join(PROJECT_ROOT, 'data/2014_bjp_manifesto.xlsx'))
    sheet = copy['main_manifesto_items']
    context = {
        'COPY' : copy,
        'row' : sheet[int(id) - 1]
    }
    return render_template('manifesto_item.html', **context)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/current-manifesto/')
def current_manifesto():
    return render_template('current_manifesto.html')


#to run Flask locally
if __name__ == '__main__':
    app.run()

