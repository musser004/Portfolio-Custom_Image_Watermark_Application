from PIL import Image, ImageFont, ImageDraw


class ImageWatermarker:

    # Default watermark image is brought in and formatted

    def __init__(self, watermark_name):
        self.watermark_name = watermark_name
        self.watermark_image = Image.open(f"{self.watermark_name}").convert("RGBA")

    # Method for implementing image watermark

    def image_wm(self, image):

        # If watermark image is not the same size as the main image, it is resized here

        resized_watermark = self.watermark_image.resize(image.size)

        # Images are overlaid here

        img_output = Image.alpha_composite(image, resized_watermark)

        # Image is saved and shown

        selected_save_file = "static/img/results.png"
        img_output.save(selected_save_file)
        img_output.show()
