from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager, login_user, current_user, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "Key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reviews.db"
db = SQLAlchemy(app)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    reviews = db.relationship("Review", backref="products", lazy=True)



# Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)


# Home page
@app.route("/")
def home():
    products = Product.query.all()
    return render_template('HomePage.html')

# Product detail page
@app.route('/product/<int:product_id>')
def product_details(product_id):
    product = Product.query.get(product_id)
    return render_template("product_detail.html", product=product)

# Review page
class ReviewForm(FlaskForm):
    author = StringField("Author", validators =[DataRequired(), Length(max=100)])
    content = TextAreaField("Review", validators=[DataRequired()])
    rating = StringField("Rating", validators = [DataRequired()])
    submit = SubmitField("Submit")

# Add review page
@app.route('/product/<int:product_id>/add_review', methods=['GET', 'POST'])
def add_review(product_id):
    product = Product.query.get(product_id)
    form = ReviewForm

    if form.validate_on_submit():
        author = form.author.data
        content = form.content.data
        rating = form.rating.data

        review = Review(author=author, content=content, rating=rating, product=product)
        db.session.add(review)
        db.session.commit()

        flash("Review add successfully!", "success")
        return redirect(url_for("product_details", product_id=product_id))

    return render_template("add_reviews.html", product=product, form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=4000)