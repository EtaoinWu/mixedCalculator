import tkinter as Tk
from assets import Assets
import serial
import itertools
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

class SerialOutputter:
    operator_names = {
        "+": "PLUS",
        "-": "SUb",
        "*": "MUL",
        "/": "dIv",
        "%": "PErc"
    }

    def __init__(self, port, baudrate=115200, dry_run=False):
        self.port = port
        self.baudrate = baudrate
        self.dry_run = dry_run
        if not dry_run:
            self.ser = serial.Serial(port, baudrate)
    
    def fmt_text(self, proc, result:str):
        if result == 'Error':
            return "Err"
        if result.startswith('='):
            return result[1:]
        lastc = proc[-1]
        if lastc in self.operator_names:
            return self.operator_names[lastc]
        if lastc in "0123456789":
            non_digits = [i for i, x in enumerate(proc) if not x.isdigit()]
            i = 0 if len(non_digits) == 0 else non_digits[-1] + 1
            return proc[i:]
    
    def fmt_text_8(self, proc, result):
        s = self.fmt_text(proc, result)
        if len(s) > 8:
            s = s[-8:]
        if len(s) < 8:
            s = " " * (8 - len(s)) + s
        return s
    
    def update_text(self, proc, result):
        s = self.fmt_text_8(proc, result)
        result = f'[{s}]\u007b{proc}\u007d'
        if not self.dry_run:
            self.ser.write((result + '\n').encode('utf-8'))
        print("Sent: ", result)