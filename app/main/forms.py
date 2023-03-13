from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from wtforms import ValidationError

from ..models import BOXES, Card


class CardForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    description = StringField(validators=[DataRequired()])
    example = TextAreaField(widget=TextArea())
    box = SelectField("box", coerce=int, choices=list(zip(BOXES, BOXES)))
    submit = SubmitField("Save")

    def validate_name(self, field):
        if Card.query.filter_by(name=field.data).first():
            raise ValidationError("Card already exists.")


class EditCardForm(CardForm):

    def __init__(self, oldname, *args, **kwargs):
        super(EditCardForm, self).__init__(*args, **kwargs)
        self._oldname = oldname

    def validate_name(self, field):
        if field.data != self._oldname and \
                Card.query.filter_by(name=field.data).first():
            raise ValidationError("Card already exists.")
