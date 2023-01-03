from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return render_template('index.html'), 200

@app.route('/about')
def about_page():
    return render_template('about.html'), 200

if __name__ == '__main__':
    app.run()
