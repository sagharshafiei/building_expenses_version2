import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class UserTotalView:
    def __init__(self, total_amount):
        self.win = tk.Tk()
        self.win.title("Total Pay")
        self.win.geometry("300x400")
        self.win.configure(background='azure2')
        self.win.resizable(width=False, height=False)

        self.photo = None

        tk.Label(self.win, text="Please pay the amount to this card number",
                 background="azure2", font=("Helvetica", "9")).place(x=30, y=10)

        tk.Label(self.win, text="6219 8619 9984 3005", bg='azure2', font=("Helvetica", "12"),
                 borderwidth=1, relief="solid", border=3).place(x=70, y=80)

        tk.Label(self.win, text="Total amount:", background="azure2", font=("Helvetica", "11")).place(x=20, y=30)
        total_entry = tk.Entry(self.win, font=("Helvetica", "11"), width=15, justify="center", state="readonly")
        total_entry.place(x=150, y=30)

        total_entry.config(state="normal")
        total_entry.delete(0, tk.END)
        total_entry.insert(0, str(total_amount))
        total_entry.config(state="readonly")

        self.image_label = tk.Label(self.win, background='azure2')
        self.image_label.pack(side=tk.BOTTOM)

        def upload_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
            if file_path:
                image = Image.open(file_path)
                image.thumbnail((200, 200))
                self.photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=self.photo)

        upload_button = tk.Button(self.win, text="Upload payment image", bg="black", fg="white",
                                  font=("Arial", "11"), command=upload_image)
        upload_button.place(x=70, y=120)

        self.win.mainloop()




