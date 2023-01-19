from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

mail = Mail(app)

db = SQLAlchemy(app)

class People(db.Model):
    _id = db.Column('id', db.Integer, primary_key = True)
    firstName = db.Column('first name', db.String(30))
    lastName = db.Column('last name', db.String(40))
    email = db.Column('email', db.String(100))
    business = db.Column('business', db.String(50))
    reason = db.Column('reason for contact', db.Text)

    def __init__(self, firstName, lastName, email, business, reason):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.business = business
        self.reason = reason

@app.route('/')
def home():
    return render_template('index.html'), 200

@app.route('/thankyou', methods = ['POST','GET'])
def contact_form():
    firstName = None
    lastName = None
    email = None
    business = None
    reason = None
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        business = request.form['business']
        reason = request.form['reason']
        form_data = request.form
        person = People(firstName, lastName, email, business, reason)
        db.session.add(person)
        db.session.commit()
        # return render_template('people.html', form_data = form_data), 200
    return render_template('thankyou.html', form_data=form_data, firstName=firstName, lastName=lastName, email=email, business=business, reason=reason), 200

@app.route('/view')
def people():
    return render_template('people.html', values = People.query.all())

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
