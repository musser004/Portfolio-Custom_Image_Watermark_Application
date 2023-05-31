# Custom Image WaterMarker Application with Flask
import PIL
from PIL import Image
from text_watermarker import TextWatermarker
from image_watermarker import ImageWatermarker
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import TextWatermarkForm, ImageWatermarkForm
import os

# Initial Flask setup

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = "static/img"

# Loading default image

image_name = app.config['UPLOAD_FOLDER'] + "/base_image.jpg"
image = Image.open(f"{image_name}").convert("RGBA")

# Index page setup


@app.route("/")
def index():
    return render_template("index.html")

# Text watermark page setup


@app.route("/text-watermark", methods=["GET", "POST"])
def text_watermark():

    # Plugging in WTForms

    form = TextWatermarkForm()

    # Starting the text watermark process after user clicks the submit button

    if form.validate_on_submit():

        # Taking data from WTForms and adding it to list

        form.image.data.save("static/img/custom_image.jpg")
        variable_list = [
            form.selected_font_size.data, form.selected_font_type.data, form.rgb1.data, form.rgb2.data, form.rgb3.data,
            form.transparency.data, form.selected_msg.data, form.selected_txt_position_x.data,
            form.selected_txt_position_y.data
        ]

        # Creating list of variable names and a dictionary with default setting values for each variable name

        name_list = ["selected_font_size", "selected_font_type", "rgb1", "rgb2", "rgb3", "transparency",
                     "selected_msg", "selected_txt_position_x", "selected_txt_position_y"]
        default_dict = {"selected_font_size": 70,
                        "selected_font_type": "arial.ttf",
                        "rgb1": 0,
                        "rgb2": 0,
                        "rgb3": 0,
                        "transparency": 128,
                        "selected_msg": "DOGGO MANIA",
                        "selected_txt_position_x": 10,
                        "selected_txt_position_y": 10
                        }

        # Going through list of variables. Unfilled fields are set to default values, and filled field values are kept

        corrected_list = []
        for n in range(0, len(variable_list)):

            # If field was unfilled, default value is used

            if variable_list[n] is None or variable_list[n] == "":
                x = default_dict[name_list[n]]
                corrected_list.append(x)

            # If field was filled, that value is kept

            else:
                x = variable_list[n]
                corrected_list.append(x)

        # Then, plugging the modified list into TextWatermarker module as parameters. First, with custom image

        try:
            custom_image = Image.open("static/img/custom_image.jpg").convert("RGBA")
            text_watermarked = TextWatermarker(image=custom_image,
                                               selected_font_size=corrected_list[0],
                                               selected_font_type=corrected_list[1],
                                               rgb1=corrected_list[2],
                                               rgb2=corrected_list[3],
                                               rgb3=corrected_list[4],
                                               transparency=corrected_list[5],
                                               selected_msg=corrected_list[6],
                                               selected_txt_position=(corrected_list[7], corrected_list[8])
                                               )
            text_watermarked.text_wm()

        # If no custom image was used, the default image will be used instead

        except PIL.UnidentifiedImageError:
            text_watermarked = TextWatermarker(image=image,
                                               selected_font_size=corrected_list[0],
                                               selected_font_type=corrected_list[1],
                                               rgb1=corrected_list[2],
                                               rgb2=corrected_list[3],
                                               rgb3=corrected_list[4],
                                               transparency=corrected_list[5],
                                               selected_msg=corrected_list[6],
                                               selected_txt_position=(corrected_list[7], corrected_list[8])
                                               )
            text_watermarked.text_wm()

        # Regardless of path, it ultimately redirects back to the results page

        return redirect(url_for("results"))
    return render_template("text_watermarker.html", form=form)

# Image watermark page setup


@app.route("/image-watermark", methods=["GET", "POST"])
def image_watermark():

    # Plugging in WTForms

    form = ImageWatermarkForm()

    # Starting the image watermark process after user clicks the submit button

    if form.validate_on_submit():

        # Image files uploaded through WTForms FileFields are saved to static/img directory

        form.watermark.data.save("static/img/custom_watermark.png")
        form.image.data.save("static/img/custom_image.jpg")

        # Attempting to use custom watermark first. If error is raised, default watermark is used instead

        try:
            image_watermarked = ImageWatermarker(watermark_name="static/img/custom_watermark.png")
        except PIL.UnidentifiedImageError:
            image_watermarked = ImageWatermarker(watermark_name="static/img/base_watermark.png")

        # Attempting to use custom base image first. If error is raised, default base image is used instead

        try:
            custom_image = Image.open("static/img/custom_image.jpg").convert("RGBA")
            image_watermarked.image_wm(image=custom_image)
        except PIL.UnidentifiedImageError:
            image_watermarked.image_wm(image=image)

        # Regardless of path, it ultimately redirects back to the results page

        return redirect(url_for("results"))
    return render_template("image_watermarker.html", form=form)

# Results page setup


@app.route("/results")
def results():
    return render_template("results.html")

# Flask run


if __name__ == "__main__":
    app.run(debug=True)
