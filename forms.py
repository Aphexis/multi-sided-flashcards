from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length, DataRequired
from models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter(User.name.ilike(username.data)).first()
        if user is not None:
            raise ValidationError('Username is already in use. Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter(User.email.ilike(email.data)).first()
        if user is not None:
            raise ValidationError('Email is already in use. Please use a different email address.')


class RequiredIf(DataRequired):
    """Validator which makes a field required if another field is set and has a truthy value.

        Sources:
            - http://wtforms.simplecodes.com/docs/1.0.1/validators.html
            - http://stackoverflow.com/questions/8463209/how-to-make-a-field-conditionally-optional-in-wtforms

    """
    field_flags = ('requiredif',)

    def __init__(self, other_field_name, *args, **kwargs):
        self.other_field_name = other_field_name
        super(RequiredIf, self).__init__(*args, **kwargs)

    def __call__(self, form, field):
        other_field = form._fields.get(self.other_field_name)
        if other_field is None:
            raise Exception('no field named "%s" in form' % self.other_field_name)
        if bool(other_field.data):
            super(RequiredIf, self).__call__(form, field)


class SettingsForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[Length(max=500)], render_kw={"rows": 2, "cols": 66})
    email = StringField('Email', validators=[DataRequired(), Email()])
    new_password = PasswordField('New Password', validators=[])
    new_password2 = PasswordField(
        'Confirm New Password', validators=[EqualTo('new_password'), RequiredIf('new_password')])
    password = PasswordField('Current Password', validators=[DataRequired()])
    submit = SubmitField('Save Changes')
