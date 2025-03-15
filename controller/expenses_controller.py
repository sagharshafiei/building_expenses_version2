from model.da.da import DataAccess
from model.entity import Expenses
from model.tools.logging import Logger


def save(month,water, electricity, gas, elevator, cleaning, engine_room,other):
    try:
        expense = Expenses(month, water, electricity, gas, elevator, cleaning, engine_room, other)

        expense_da = DataAccess(Expenses)
        expense_da.save(expense)
        Logger.info(f"Expense {expense} Saved")
        return True, expense
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(id, month,water, electricity, gas, elevator, cleaning, engine_room,other):
    try:
        expense = Expenses(month,water, electricity, gas, elevator, cleaning, engine_room,other)
        expense.id = id

        expense_da = DataAccess(Expenses)
        expense_da.edit(expense)
        Logger.info(f"Expense {expense} Edited")
        return True, expense
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_by_id(id):
    try:
        expense_da = DataAccess(Expenses)
        expense = expense_da.remove_by_id(id)

        Logger.info(f"Expenses {expense} Removed")
        return True, expense
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"


def find_all():
    try:
        expense_da = DataAccess(Expenses)
        expense_list = expense_da.find_all()
        Logger.info(f"expense FindALL")
        return True, expense_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"

def find_by_id(id):
    try:
        expense_da = DataAccess(Expenses)
        expense = expense_da.find_by_id(id)
        if expense:
            Logger.info(f"expense FindById {id}")
            return True, expense
        else:
            raise ValueError("No expense Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {id}")
        return False, f"{e}"

# def total_calculator():
#     status, expense_list = find_all()
#     total_list =
#     for item in expense_list:
#          item.water + item.electricity + item.gas + item.elevator + item.cleaning + item.engine_room + item.other
#
# total_calculator()
