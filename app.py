from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_url_path='/static')

@app.route('/')
def index():
    current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    year = datetime.now().year
    return render_template('index.html', date_time=current_date_time, year=year)

@app.route('/blog/')
def blog():
    year = datetime.now().year
    return render_template('blog.html', year=year)

@app.route('/contacts/')
def contacts():
    year = datetime.now().year
    return render_template('contacts.html', year=year)

if __name__ == '__main__':
    app.run(debug=True)