from tkinter import *

class LabelAndEntry:
    def __init__(self, window, text, x, y, distance=80,data_type="str",state=None, set_data=None,background='azure2'):
        Label(window, text=text,background=background).place(x=x, y=y)

        match data_type:
            case "str":
                self.variable = StringVar()
            case "int":
                self.variable = IntVar()
            case "float":
                self.variable = DoubleVar()
            case "bool":
                self.variable = BooleanVar()
            case _:
                self.variable = StringVar()

        Entry(window, textvariable=self.variable, state=state).place(x=x + distance, y=y)
