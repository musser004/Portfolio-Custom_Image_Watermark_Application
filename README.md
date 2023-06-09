# Project: Custom Image Watermark Flask Application (Full Stack Web Development)

Live deployed website: https://web-production-61cb.up.railway.app/

Description: Flask application that allows the user to upload image files and watermark an image either with a text watermark, or with another image file acting as the watermark. Set up with error handling such that the user can either enter no inputs, partial inputs, or full inputs and still get a resulting image. For fields without an entry, the default image/setting is used

Python Libraries: Flask, WTForms, Pillow, OS, Flask-Bootstrap

NOTE: Application requires environmental variables (not included) in order to run properly

# How to use:

For text watermarking:

1.) Click the link above, then click "Text Watermark" button, either from the navbar or at the bottom of the home page

2.) Fill in as much or as little detail as you'd like. For any inputs that are either left empty, or are invalid but not caught by the field validators - those will be given the default values

3.) When ready, click the "Watermark It!" button. If all goes well, the new image will be displayed on the results page

For image watermarking:

1.) Click the link above, then click "Image Watermark" button, either from the navbar or at the bottom of the home page

2.) Add one, both, or neither image file with the "Choose File" buttons. For any button without a valid input, the default image will be used

3.) When ready, click the "Watermark It!" button. If all goes well, the new image will be displayed on the results page
