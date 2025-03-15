from tkinter import Tk, Label, Button, messagebox
from model.entity import UnitUserConnector, Users, Units
from view.component import LabelAndEntry, Table
from model.da.da import DataAccess
from controller.user_panel_controller import expense_calculator
from view.user_total_view import UserTotalView

class UserPanelView:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.win = Tk()
        self.win.title("User Panel")
        self.win.geometry("790x500")
        self.win.configure(background='azure2')
        self.win.resizable(False, False)

        user_da = DataAccess(Users)
        user_list = user_da.find_by((Users._username == self.username) & (Users._password == self.password))

        if not user_list:
            messagebox.showerror("Login Error", "Invalid username or password!")
            self.win.destroy()
            return

        user = user_list[0]
        user_id = user.id

        connector_da = DataAccess(UnitUserConnector)
        unit_user_list = connector_da.find_by(UnitUserConnector.user_id == user_id)

        if not unit_user_list:
            messagebox.showinfo("No Unit Found", "You are not assigned to any unit.")
            self.win.destroy()
            return

        unit_id = unit_user_list[0].unit_id

        unit_da = DataAccess(Units)
        unit = unit_da.find_by_id(unit_id)

        if not unit:
            messagebox.showerror("Unit Error", "Unit not found!")
            self.win.destroy()
            return

        self.unit_no = unit.unit_no
        self.first_name = unit.name
        self.family_name = unit.family
        self.resident_count = unit.no_people

        Label(self.win, text=f"Welcome {self.first_name} {self.family_name}!",
              font=("Arial", "18"), foreground="green", background='azure2', border="15").place(x=230, y=15)

        LabelAndEntry(self.win, "Unit Number:", 80, 100, 100, state="readonly").variable.set(self.unit_no)
        LabelAndEntry(self.win, "Residents Count:", 450, 100, 120, state="readonly").variable.set(self.resident_count)

        Button(self.win, text="Show Total Amount", font=("Arial", "13"),
               command=self.total_show).place(x=320, y=440)

        self.table = Table(
            self.win,
            ["Id", "Month", "Water", "Electricity", "Gas", "Elevator", "Cleaning", "Engine Room",
             "Other", "Total"],
            [40, 80, 80, 80, 80, 80, 80, 80, 80, 80],
            300, 15, 130)

        self.read_data()
        self.win.mainloop()

    def read_data(self):

        self.total_data = expense_calculator(self.resident_count) or []  # ✅ Use tuples directly

        self.table.refresh_table(self.total_data)

    def total_show(self):

        if hasattr(self, 'total_data') and self.total_data:
            last_total = self.total_data[-1][-1]
        else:
            last_total = 0

        self.win.destroy()
        UserTotalView(total_amount=last_total)

