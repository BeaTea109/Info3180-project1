from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class PropertyForm(FlaskForm):
    propertyTitle = StringField('Property Title', validators=[DataRequired()])
    propertyPrice = FloatField('Property Price', validators=[DataRequired()])
    propertyLocation = StringField(
        'Property Location', validators=[DataRequired()])
    propertyDescription = StringField(
        'Property Description', validators=[DataRequired()], widget=TextArea())
    propertyBathrooms = IntegerField(
        'Property Bathrooms', validators=[DataRequired()])
    propertyBedrooms = IntegerField(
        'Property Bedrooms', validators=[DataRequired()])
    propertyType = StringField('Property Type', validators=[DataRequired()])
    propertyPhoto = FileField('Property Photo', validators=[FileRequired(),
                                                            FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
