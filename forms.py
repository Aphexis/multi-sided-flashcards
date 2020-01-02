from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required, length


class CreateSet(FlaskForm):
    name = StringField('Set Name', validators=[data_required(), length(max=50)])
    description = StringField('Description')
    # all the cell info
    submit = SubmitField('Create Set')