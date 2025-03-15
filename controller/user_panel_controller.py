from model.da.da import DataAccess
from model.entity import Expenses, Units

from model.tools.logging import Logger

def find_all():
    try:
        expense_da = DataAccess(Expenses)
        expense_list = expense_da.find_all()
        Logger.info(f"expense FindALL")
        return True, expense_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"

def sum_residents():
    people_counter = []
    units_da = DataAccess(Units)
    people_count_list = units_da.find_by(Units._no_people)

    for item in people_count_list:
        people_counter.append(item.no_people)
    else:
        return sum(people_counter)


def expense_calculator(resident_count):
    status, expense_list = find_all()
    if not status:
        Logger.error("Failed to retrieve expenses")
        return []

    total_residents = sum_residents() or 1
    factor = resident_count / total_residents

    formatted_expenses = []
    for item in expense_list:
        try:
            new_water = max(0, int(item.water * factor))
            new_electricity = max(0, int(item.electricity * factor))
            new_gas = max(0, int(item.gas * factor))
            new_elevator = max(0, int(item.elevator * factor))
            new_cleaning = max(0, int(item.cleaning * factor))
            new_engine_room = max(0, int(item.engine_room * factor))
            new_other = max(0, int(item.other * factor))
            new_total = max(0, int(item.total * factor))

            formatted_expenses.append(
                (item.id, item.month, new_water, new_electricity, new_gas,
                 new_elevator, new_cleaning, new_engine_room, new_other, new_total)
            )
        except ValueError as e:
            Logger.error(f"Expense Calculation Error: {e}")
            continue

    return formatted_expenses



