from tkinter import Button

class TkButton:
    def __init__(self, master, text, command, x, y, width=90, height=40, font=None):
        self.master = master
        self.text = text
        self.command = command
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font

        Button(self.master,
               text=self.text,
               command=self.command,
               font=self.font).place(x=self.x, y=self.y, width=self.width, height=self.height)