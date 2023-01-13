from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html'), 200

@app.route('/newsletter', methods = ['GET'])
def newsletter():
    email = request.args.get('email')
    return render_template('index.html'), 200

@app.route('/about')
def about_page():
    return render_template('about.html'), 200

@app.route('/contact')
def contact_page():
    return render_template('contact.html'), 200

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Sorry... {err}"}), 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f"It's not you, it's us"}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
