import tkinter as Tk
from assets import Assets

class Outputter:
    def __init__(self, tk, x, y, image, font_size, assets: Assets):
        self.tk = tk
        self.x = x
        self.y = y
        self.image = image
        self.font_size = font_size
        self.assets = assets
        self.canvas = Tk.Canvas(tk, width=340, height=105, bg="white")
        self.canvas.config(highlightthickness=0)
        self.canvas.create_image(0, 0, image=image, anchor="nw")
        self.canvas.place(x=x, y=y)

    def str_len_limit(self, s):
        cvt = {"*": "×", "/": "÷", "%": "%"}
        s = ''.join([cvt.get(c, c) for c in s])
        if len(s) > 21:
            return "…" + s[-20:]
        return s
    
    def update_text(self, proc, result):
        proc = self.str_len_limit(proc)
        result = self.str_len_limit(result)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        self.canvas.create_text(20, 10, text=proc, font=("Sarasa Mono J", self.font_size), fill="black", anchor="nw")
        self.canvas.create_text(320, 60, text=result, font=("Sarasa Mono J Semibold", self.font_size), fill="black", anchor="ne")
    