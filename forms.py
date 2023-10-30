from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

# Form for adding a new pet
class AddPetForm(FlaskForm):
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )
    
    name = StringField(
        "Pet Name",
        validators=[InputRequired()]
    )

    species = SelectField(
        "Species",
        choices=[("dog","Dog"), ("iguana","Iguana"), ("cat","Cat")]
    )

    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=100)],
    )

    notes = TextAreaField(
        "Fun Facts",
        validators=[Optional(), Length(min=10)]
    )

# Form for editing an existing pet
class EditPetForm(FlaskForm):
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available")
