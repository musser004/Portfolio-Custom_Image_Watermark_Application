from flask_wtf import FlaskForm
from wtforms import StringField, FileField, IntegerField, SubmitField
from wtforms.validators import NumberRange, Optional

# WTForms setup for Image Watermark page


class ImageWatermarkForm(FlaskForm):

    # WTForms FileField so that the user can upload image files

    watermark = FileField('Watermark Image File (PNG recommended for best results)', validators=[Optional()])
    image = FileField('Base Image', validators=[Optional()])

    # WTForms SubmitField to allow watermarking progress to commence

    submit = SubmitField("Watermark It!")

# WTForms setup for Text Watermark page


class TextWatermarkForm(FlaskForm):

    # WTForms FileField so that the user can upload base image file

    image = FileField('Base Image')

    # WTForms StringField and IntegerField for various text watermark settings

    selected_msg = StringField("Selected Text Message To Watermark (e.g. \"COPYRIGHT\")", validators=[Optional()])
    selected_font_size = IntegerField("Text Font Size (Integer)", validators=[
        NumberRange(min=0, max=400, message="Number out of range"),
        Optional()])
    selected_font_type = StringField("Text Font Type (e.g. \"Arial\", \"times new roman\", etc.)",
                                     validators=[Optional()])
    rgb1 = IntegerField("Text RGB Values: Red (0 to 255)", validators=[
        NumberRange(min=0, max=255, message="Number out of range"),
        Optional()])
    rgb2 = IntegerField("Text RGB Values: Green (0 to 255)", validators=[
        NumberRange(min=0, max=255, message="Number out of range"),
        Optional()])
    rgb3 = IntegerField("Text RGB Values: Blue (0 to 255)", validators=[
        NumberRange(min=0, max=255, message="Number out of range"),
        Optional()])
    transparency = IntegerField("Text Transparency (0 to 255)", validators=[
        NumberRange(min=0, max=255, message="Number out of range"),
        Optional()])
    selected_txt_position_x = IntegerField("Text X position mapping (non-negative integer)", validators=[
        NumberRange(min=0, max=255, message="Number out of range"),
        Optional()])
    selected_txt_position_y = IntegerField("Text Y position mapping (non-negative integer)", validators=[
        NumberRange(min=0, max=255, message="Number out of range"),
        Optional()])

    # WTForms SubmitField to allow watermarking progress to commence

    submit = SubmitField("Watermark It!")
