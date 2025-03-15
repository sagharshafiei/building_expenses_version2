from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base
from model.entity.users import Users
from model.entity.units import Units
from model.entity.expenses import Expenses
from model.entity.unit_user_connector import UnitUserConnector



