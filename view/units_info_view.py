from controller.units_info_controller import *
from view.component import *
from tkinter import messagebox as msg
from model.entity import Units
from model.da.da import session


class UnitsInfoView:
    def reset_form(self):
        self.id.variable.set(0)
        self.unit_no.variable.set(0)
        self.first_name.variable.set("")
        self.family_name.variable.set("")
        self.resident_count.variable.set(0)
        self.user_username.variable.set("")
        self.user_password.variable.set("")

        status, data_list = find_all()


        if not status:
            print("Error fetching data:", data_list)
            return

        if isinstance(data_list, list) and all(isinstance(x, Units) for x in data_list):
            sorted_data_list = sorted(
                [(unit.id, unit.unit_no, unit.name, unit.family, unit.no_people,
                  unit.user.username if unit.user else "", unit.user.password if unit.user else "")
                 for unit in data_list],
                key=lambda x: x[1]  # Sorting by Unit No.
            )
        else:
            print("Unexpected data format:", data_list)
            sorted_data_list = []

        self.table.refresh_table(sorted_data_list)

    def save_click(self):
        status, data = save(
            self.unit_no.variable.get(),
            self.first_name.variable.get(),
            self.family_name.variable.get(),
            self.resident_count.variable.get(),
            self.user_username.variable.get(),
            self.user_password.variable.get()
        )
        if status:
            msg.showinfo("Save", f"Unit Saved\n{data}")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data}")

    def edit_click(self):

        try:
            unit_id = int(self.id.variable.get())

            if unit_id == 0:
                msg.showerror("Edit Error", "No unit selected for editing!")
                return

            status, data = edit(
                unit_id,
                self.unit_no.variable.get(),
                self.first_name.variable.get(),
                self.family_name.variable.get(),
                self.resident_count.variable.get(),
                self.user_username.variable.get(),
                self.user_password.variable.get(),
            )

            if status:
                msg.showinfo("Edit", f"Unit Edited Successfully\n{data}")
                self.reset_form()
            else:
                msg.showerror("Edit Error", f"Error\n{data}")

        except ValueError:
            msg.showerror("Edit Error", "Invalid unit ID format!")

    def remove_click(self):

        unit_id = self.id.variable.get()
        status, data = force_remove_by_id(unit_id)

        if not status and "linked" in data:
            confirm = msg.askyesno("Remove Confirmation", f"{data}\nDo you want to remove it anyway?")
            if confirm:
                status, data = force_remove_by_id(unit_id)

        if status:
            msg.showinfo("Remove", f"Unit Removed\n{data}")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data}")

    def select_table(self, selected_item):

        if not selected_item or len(selected_item) < 7:
            print("Unexpected data format:", selected_item)
            return

        selected_tuple = tuple(selected_item) if isinstance(selected_item, list) else selected_item

        try:
            self.id.variable.set(int(selected_tuple[0]))  # ✅ Ensure ID is set correctly
        except ValueError:
            print(f"DEBUG: Failed to set Unit ID from {selected_tuple[0]}")
            return

        self.unit_no.variable.set(selected_tuple[1])
        self.first_name.variable.set(selected_tuple[2])
        self.family_name.variable.set(selected_tuple[3])
        self.resident_count.variable.set(selected_tuple[4])
        self.user_username.variable.set(selected_tuple[5])
        self.user_password.variable.set(selected_tuple[6] if selected_tuple[6] else "")


        print(f"DEBUG: Selected Unit ID -> {self.id.variable.get()}")

    def __init__(self):

        self.win = Toplevel()
        self.win.title("User Info Panel")
        self.win.geometry("860x600")
        self.win.configure(background='azure2')
        self.win.resizable(width=False, height=False)

        self.id = LabelAndEntry(self.win, "Id", 20, 20, distance=110, state="readonly")
        self.unit_no = LabelAndEntry(self.win, "Unit No:", 20, 60, distance=110)
        self.first_name = LabelAndEntry(self.win, "First Name:", 310, 20, distance=110)
        self.family_name = LabelAndEntry(self.win, "Family Name:", 310, 60, distance=110)
        self.resident_count = LabelAndEntry(self.win, "Resident Count:", 20, 100, distance=110)
        self.user_username = LabelAndEntry(self.win, "User Name:", 310, 100, distance=110)
        self.user_password = LabelAndEntry(self.win, "Password:", 550, 20, distance=110)

        self.table = Table(
            self.win,
            ["Id", "Unit No.", "First Name", "Family Name", "Resident Count", "User Name", "Password"],
            [60, 60, 130, 130, 130, 130, 130],
            290,
            40, 140,
            self.select_table,
        )

        TkButton(self.win, "Save", self.save_click, 80, 445)
        TkButton(self.win, "Edit", self.edit_click, 280, 445)
        TkButton(self.win, "Remove", self.remove_click, 480, 445)
        TkButton(self.win, "Refresh", self.reset_form, 680, 445)

        self.reset_form()
        self.win.mainloop()
