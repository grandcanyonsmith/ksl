from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ItemInsertForm(FlaskForm):
    item_name = StringField("Item Name: ", validators=[DataRequired()])
    minimum = StringField("Minimum Price: ", validators=[DataRequired()])
    maximum = StringField("Maximum Price", validators=[DataRequired()])
    submit = SubmitField("Insert")

class ItemRemoveForm(FlaskForm):
    remove_item_name = StringField("Remove Item Name: ", validators=[DataRequired()])
    submit_delete = SubmitField("Delete")
