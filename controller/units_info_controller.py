from model.da.da import DataAccess
from model.entity import Units, Users
from model.entity.unit_user_connector import UnitUserConnector
from model.tools.logging import Logger

def save(unit_no, first, family, resident_count, user_username, user_password):
    try:
        user_da = DataAccess(Users)
        users = user_da.find_by(Users._username == user_username)
        user = users[0] if users else None
        if not user:
            user = Users(username=user_username, password=user_password, role="user")
            user_da.save(user)


        unit = Units(unit_no=unit_no, name=first, family=family, no_people=resident_count, user=user)
        unit_da = DataAccess(Units)
        unit_da.save(unit)

        unit_user_connector = UnitUserConnector(unit=unit, user=user)
        connector_da = DataAccess(UnitUserConnector)
        connector_da.save(unit_user_connector)

        Logger.info(f"Unit {unit} and User {user.username} Connected and Saved")
        return True, unit

    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"

def edit(id, unit_no, first, family, resident_count, user_username, user_password):
    try:
        id = int(id)


        unit_da = DataAccess(Units)
        unit = unit_da.find_by_id(id)
        if not unit:
            Logger.error(f"Unit with ID {id} not found!")
            return False, f"Unit with ID {id} not found!"


        user_da = DataAccess(Users)
        users = user_da.find_by(Users._username == user_username)
        user = users[0] if users else None

        if unit.user and unit.user.username == user_username:
            unit.user.password = user_password
        else:
            if not user:
                user = Users(username=user_username, password=user_password, role="user")
                user_da.save(user)

            unit.user = user


        unit.unit_no = unit_no
        unit.name = first
        unit.family = family
        unit.no_people = resident_count

        unit_da.edit(unit)
        Logger.info(f"Unit {unit._id} Edited Successfully")
        return True, f"Unit {unit._id} updated successfully"

    except Exception as e:
        Logger.error(f"{e} - Edit Failed")
        return False, f"Edit Failed: {e}"

def force_remove_by_id(unit_id):
    try:

        connector_da = DataAccess(UnitUserConnector)
        connectors = connector_da.find_by(UnitUserConnector.unit_id == unit_id)
        for connector in connectors:
            connector_da.remove(connector)


        unit_da = DataAccess(Units)
        unit = unit_da.find_by_id(unit_id)
        if unit:
            unit_da.remove(unit)

        Logger.info(f"Unit {unit_id} removed successfully")
        return True, f"Unit {unit_id} removed successfully"
    except Exception as e:
        Logger.error(f"{e} - Remove Failed")
        return False, f"Remove Failed: {e}"

def find_all():
    try:
        unit_da = DataAccess(Units)
        unit_list = unit_da.find_all()
        Logger.info(f"Units FindALL")
        return True, unit_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"