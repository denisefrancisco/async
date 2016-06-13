from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TaskForm(Form):
	# DataRequired is to halt the submission process if there is an empty field
	numberOfSeconds = StringField('numberOfSeconds', validators = [DataRequired()])
	
