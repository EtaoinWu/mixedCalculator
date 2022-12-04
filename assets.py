from PIL import Image, ImageTk


def get_image(path):
    return Image.open(path)


def get_image_tk(img):
    return ImageTk.PhotoImage(img)


class Assets:
    def __init__(self):
        per_button_goal_size = 80

        button_full = get_image("static/btn.png")
        per_button_size = button_full.size[0] // 3
        buttons_full = [
            [
                button_full.crop(
                    (
                        per_button_size * j,
                        per_button_size * i,
                        per_button_size * (j + 1),
                        per_button_size * (i + 1),
                    )
                )
                for j in range(3)
            ]
            for i in range(4)
        ]

        self.button_masks = [
            y.resize((per_button_goal_size, per_button_goal_size))
            for y in buttons_full[0]
        ]

        self.buttons = [
            [
                get_image_tk(y.resize((per_button_goal_size, per_button_goal_size)))
                for y in x
            ]
            for x in buttons_full
        ]

        self.output_bg = get_image_tk(get_image("static/output.png").resize((340, 105)))

    def in_button(self, x, y, type=0):
        if x < 0 or y < 0 or x >= 80 or y >= 80:
            return False
        return self.button_masks[type].getpixel((x, y))[0] < 255
