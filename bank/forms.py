from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, RadioField, \
    SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from bank.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username *', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email *', validators=[DataRequired(), Email()])
    password = PasswordField('Password *', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password *', validators=[DataRequired(), EqualTo('password')])
    phone = IntegerField('Phone number * ', validators=[DataRequired()])
    post_index = IntegerField('Post index * ', validators=[DataRequired()])
    address = StringField('Address')
    city = StringField('City')
    blood_group = SelectField('Blood group *', [DataRequired()], default='1', choices=[
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    ])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one. ')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email already registered.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username * ', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email * ', validators=[DataRequired(), Email()])
    about = TextAreaField('About Me')
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    old_pass = PasswordField('Old password')
    new_pass = PasswordField('New password')
    confirm_pass = PasswordField('Confirm password', validators=[EqualTo('new_pass')])
    phone = IntegerField('Phone number * ', validators=[DataRequired()])
    post_index = IntegerField('Post index * ', validators=[DataRequired()])
    address = StringField('Address * ', validators=[DataRequired()])
    city = StringField('City * ', validators=[DataRequired()])
    blood_group = SelectField('Blood group * ', [DataRequired()], default='1', choices=[
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    ])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class DonateForm(FlaskForm):
    name_blood = SelectField('Blood group * ', [DataRequired()], default='1', choices=[
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    ])
    quantity = IntegerField('Quantity on pints', validators=[DataRequired()])
    submit = SubmitField('Donate')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
