import tkinter as Tk
from assets import Assets


class Button:
    def __init__(self, tk, x, y, images, command, text, font_size, assets: Assets):
        self.tk = tk
        self.x = x
        self.y = y
        self.command = command
        self.images = images
        self.text = text
        self.font_size = font_size
        self.assets = assets
        self.state = 0
        self.canvas = Tk.Canvas(tk, width=80, height=80, bg="white")
        self.canvas.config(highlightthickness=0)
        self.canvas.place(x=x, y=y)
        self.canvas.bind("<Enter>", self.on_motion)
        self.canvas.bind("<Leave>", self.on_leave)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Motion>", self.on_motion)
        self.set_state(0)

    def set_state(self, state):
        self.state = state
        self.canvas.create_image(0, 0, image=self.images[state], anchor="nw")
        self.canvas.create_text(
            40,
            40,
            text=self.text,
            font=("Sarasa Gothic J Light", self.font_size),
            fill="black",
        )

    def on_leave(self, event):
        if self.state != 2:
            self.set_state(0)

    def on_motion(self, event):
        if self.state == 2:
            return
        if self.state == 0:
            if self.assets.in_button(event.x, event.y, 0):
                self.set_state(1)
        else:
            if not self.assets.in_button(event.x, event.y, 1):
                self.set_state(0)

    def on_click(self, event):
        if self.assets.in_button(event.x, event.y, self.state):
            self.set_state(2)
            self.command(event)

    def on_release(self, event):
        if self.assets.in_button(event.x, event.y, 1):
            self.set_state(1)
        else:
            self.set_state(0)
