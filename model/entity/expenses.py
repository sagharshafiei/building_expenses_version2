from sqlalchemy import event

from model.entity import *
from model.tools.validation import expense_validator, month_validator


class Expenses(Base):
    __tablename__ = 'expenses'
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _month = Column("month", String(30), nullable = False)
    _water = Column("water", Integer, nullable = False)
    _electricity = Column("electricity", Integer, nullable = False)
    _gas = Column("gas", Integer, nullable = False)
    _elevator = Column("elevator", Integer, nullable = False)
    _cleaning = Column("cleaning", Integer, nullable = False)
    _engine_room = Column("engine_room", Integer, nullable = False)
    _other = Column("other", Integer, nullable = True)
    _total = Column("total", Integer)

    def __init__(self ,month, water, electricity,gas , elevator, cleaning, engine_room, other):
        self.id = None
        self.month = month
        self.water = water
        self.gas = gas
        self.electricity = electricity
        self.elevator = elevator
        self.cleaning = cleaning
        self.engine_room = engine_room
        self.other = other
        self.total = None
    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # month
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if month_validator(value):
            self._month = value.capitalize()

    # water
    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, value):
        if expense_validator(value):
            self._water = value

    #gas
    @property
    def gas(self):
        return self._gas

    @gas.setter
    def gas(self, value):
        if expense_validator(value):
            self._gas = value

    # electricity
    @property
    def electricity(self):
        return self._electricity

    @electricity.setter
    def electricity(self, value):
        if expense_validator(value):
            self._electricity = value

    # elevator
    @property
    def elevator(self):
        return self._elevator

    @elevator.setter
    def elevator(self, value):
        if expense_validator(value):
            self._elevator = value

    # cleaning
    @property
    def cleaning(self):
        return self._cleaning

    @cleaning.setter
    def cleaning(self, value):
        if expense_validator(value):
            self._cleaning = value

    #engine_room
    @property
    def engine_room(self):
        return self._engine_room

    @engine_room.setter
    def engine_room(self, value):
        if expense_validator(value):
            self._engine_room = value

    # other
    @property
    def other(self):
        return self._other

    @other.setter
    def other(self, value):
        self._other = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


def calculate_total(mapper, connection, target):
    target.total = (
        int(target.water) +
        int(target.electricity) +
        int(target.gas) +
        int(target.elevator) +
        int(target.cleaning) +
        int(target.engine_room) +
        int(target.other)
    )

event.listen(Expenses, "before_insert", calculate_total)
event.listen(Expenses, "before_update", calculate_total)