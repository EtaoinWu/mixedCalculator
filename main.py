import tkinter as Tk
from assets import Assets
from PIL import ImageTk, Image
from button import Button as Btn
from output_canvas import Outputter
from calc import Calculator, CalculatorMachine
import itertools

tk = Tk.Tk()
tk.title("Calculator")
tk.configure(background="white")
tk.geometry("400x600")

assets = Assets()

outputter = Outputter(tk, 30, 20, assets.output_bg, 20, assets)
machine = CalculatorMachine(outputter.update_text)

button_configuration = [
    ["A", "(", ")", "+"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "/"],
    ["%", "0", "!", "="],
]

font_size_configuration = [
    [25, 25, 25, 25],
    [25, 25, 25, 25],
    [25, 25, 25, 25],
    [25, 25, 25, 25],
    [25, 25, 22, 25],
]

color_configuration = [
    [1, 2, 2, 2],
    [0, 0, 0, 2],
    [0, 0, 0, 2],
    [0, 0, 0, 2],
    [2, 0, 1, 3],
]
display_map = {"A": "AC", "!": "⌫", "*": "×", "/": "÷", "-": "−"}
kbd_map = {
    "A": "<Escape>",
    "!": "<BackSpace>",
}
for c in itertools.chain(*button_configuration):
    tk.bind(kbd_map.get(c, c), lambda e, c=c: machine.input(c))
tk.bind("<Return>", lambda e: machine.input('='))
btns = [
    [
        Btn(
            tk,
            x=25 + 90 * j,
            y=140 + 90 * i,
            images=assets.buttons[color],
            command=lambda t, text=text: machine.input(text),
            text=display_map.get(text, text),
            font_size=font_size_configuration[i][j],
            assets=assets,
        )
        for j, (text, color) in enumerate(
            zip(button_configuration[i], color_configuration[i])
        )
    ]
    for i in range(len(button_configuration))
]

# my_button = Btn(
#     tk, 30, 150, assets.buttons[0], lambda event: machine.update("+"), "+", 20, assets
# )

tk.mainloop()
