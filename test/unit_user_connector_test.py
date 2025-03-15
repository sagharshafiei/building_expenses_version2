from model.da.da import DataAccess
from model.entity import *


unit_da = DataAccess(Units)
unit = unit_da.find_by_id(1)
print(unit)

user_da = DataAccess(Users)
user = user_da.find_by_id(1)
print(user)

connector_da = DataAccess(UnitUserConnector)
connector = UnitUserConnector(unit, user)
connector_da.save(connector)
print(connector)

