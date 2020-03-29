from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, HiddenField, TextAreaField, FileField, BooleanField
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms.fields.html5 import IntegerField

class LoginForm(FlaskForm):
    log_username = StringField('Username:', validators=[InputRequired('Username requiered'), Length(min=3, max=20, message='Username must be at least 3 characters long')])
    log_password = PasswordField('Password:', validators=[InputRequired('Password requiered'), Length(min=3, max=40, message='Password must be at least 3 characters long')])
    log_submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name:', validators=[InputRequired('First name required'), Length(min=3, max=20, message='First name must be at least 3 characters long')])
    last_name = StringField('Last Name:', validators=[InputRequired('Last name required'), Length(min=3, max=20, message='Last name must be at least 3 characters long')])
    city = StringField('City:', validators=[InputRequired('City required'), Length(min=3, max=20, message='City must be at least 3 characters long')])
    address = StringField('Address:', validators=[InputRequired('Address required'), Length(min=3, max=20, message='Address must be at least 3 characters long')])
    country = SelectField('Country:' ,choices=[('Norway', 'Norway'), ('Denmark', 'Denmark'), ('Sweden', 'Sweden'), ('Finland', 'Finland'), ('Iceland', 'Iceland')])
    username = StringField('Username:', validators=[InputRequired('Username required'), Length(min=3, max=20, message='Username must be at least 3 characters long')])
    password = PasswordField('Password:', validators=[InputRequired('Password required'), Length(min=3, max=20, message='Password must be at least 3 characters long')])
    confirm = PasswordField('Confirm Password:', validators=[InputRequired('Password must be confirmed'), EqualTo('password', message='Passwords do not match')])
    submit = SubmitField('Register') 

class AddForm(FlaskForm):
    quan = IntegerField('Quantity:')
    prod_submit = SubmitField('ADD TO CART')

class BuyForm(FlaskForm):
    buy = SubmitField('BUY')

class RoleForm(FlaskForm):
    role = SelectField('Role:', choices=[('User', 'user'), ('Admin', 'admin')])
    change = SubmitField('Change')

class ProductForm(FlaskForm):
    name = StringField('Name:')
    supplier = StringField('Supplier:')
    quantity = IntegerField('Quantity:')
    price = IntegerField('Price:')
    year = StringField('Year:')
    isbn = StringField('ISBN:')
    status = SelectField('Status:', choices=[('new', 'New'), ('old', 'Old')])
    description = TextAreaField('Description:')
    upload = FileField('Image:')
    elec = BooleanField('Electronics:')
    home = BooleanField('Home:')
    car = BooleanField('Car:')
    fashion = BooleanField('Fashion:')
    sport = BooleanField('Sports:')
    media = BooleanField('Media:')
    submit = SubmitField('ADD')
    