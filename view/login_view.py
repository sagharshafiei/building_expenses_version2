from tkinter import messagebox

from model.da.da import DataAccess
from model.entity import Users
from view.admin_panel_view import AdminPanelView
from view.component import *
from view.user_panel_view import UserPanelView


class LoginView:
    def login_click(self):
        user_admin_da = DataAccess(Users)
        if user_admin_da.find_by((Users._username == self.username.variable.get()) &
                                      (Users._password == self.password.variable.get()) &
                                      (Users._role == "admin")):
            self.win.destroy()
            admin_win = AdminPanelView()

        elif user_admin_da.find_by((Users._username == self.username.variable.get()) &
                                     (Users._password == self.password.variable.get()) &
                                     (Users._role == "user")):
            self.win.destroy()
            user_win = UserPanelView(self.username.variable.get(), self.password.variable.get())

        # if admin:
        #     self.win.destroy()
        #     admin_win = AdminPanelView()
        #
        # elif user:
        #     self.win.destroy()
        #     user_win = UserPanelView(self.username.variable.get(), self.password.variable.get())

        else:
            msg.showerror("Login Error", "Wrong Username or Password")

    def __init__(self):
        self.win = Tk()
        self.win.title("Login")
        self.win.geometry("250x210")
        self.win.configure(background='grey')
        self.win.resizable(width=False, height=False)

        self.username = LabelAndEntry(self.win, "Username", 20, 20,background='white')
        self.password = LabelAndEntry(self.win, "Password", 20, 60,background='white')

        # Button(self.win, text="Login", width=7, command=self.login_click).place(x=95, y=150)
        TkButton(self.win, "Login", self.login_click, 80, 150)

        self.win.mainloop()
# a=LoginView()