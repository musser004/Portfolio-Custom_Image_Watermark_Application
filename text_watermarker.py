from PIL import Image, ImageFont, ImageDraw


class TextWatermarker:

    # Text watermark settings and constants are brought in

    def __init__(self, image,
                 selected_font_size,
                 selected_font_type,
                 rgb1,
                 rgb2,
                 rgb3,
                 transparency,
                 selected_msg,
                 selected_txt_position):
        self.image = image
        self.font = ImageFont.truetype(selected_font_type, selected_font_size)
        self.selected_rgb = (rgb1, rgb2, rgb3, transparency)
        self.txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
        self.txt_draw = ImageDraw.Draw(self.txt)
        self.selected_msg = selected_msg
        self.selected_txt_position = selected_txt_position

    # Method to draw text onto the image at the selected position, then the text image is merged with the original image

    def text_wm(self):

        self.txt_draw.text(self.selected_txt_position, self.selected_msg, font=self.font, fill=self.selected_rgb)
        txt_output = Image.alpha_composite(self.image, self.txt)

        # Image is saved and shown

        selected_save_file = "static/img/results.png"
        txt_output.save(selected_save_file)
        txt_output.show()
