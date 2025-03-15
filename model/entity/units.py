from model.entity import *
from model.tools.validation import name_validator, resident_count_validator, unit_number_validator

class Units(Base):
    __tablename__ = 'units'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _unit_no = Column("unit_no", Integer, unique=True, nullable=False)
    _name = Column("name", String(30), nullable=False)
    _family = Column("family", String(30), nullable=False)
    _no_people = Column("no_people", Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("Users", back_populates="units")
    unit_users = relationship("UnitUserConnector", back_populates="unit")

    def __init__(self, unit_no, name, family, no_people, user, id=None):
        if id is not None:
            self.id = id
        self.unit_no = unit_no
        self.name = name
        self.family = family
        self.no_people = no_people
        self.user_id = user.id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def __repr__(self):
        return f"<Units(id={self.id}, unit_no={self.unit_no}, name='{self.name}', family='{self.family}', no_people={self.no_people}, user_id={self.user_id})>"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if name_validator(value):
            self._name = value
        else:
            raise ValueError("Invalid name format")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        if name_validator(value):
            self._family = value
        else:
            raise ValueError("Invalid family format")

    @property
    def no_people(self):
        return self._no_people

    @no_people.setter
    def no_people(self, value):
        if resident_count_validator(value):
            self._no_people = value
        else:
            raise ValueError("Invalid number of people")

    @property
    def unit_no(self):
        return self._unit_no

    @unit_no.setter
    def unit_no(self, value):
        if unit_number_validator(value):
            self._unit_no = value
        else:
            raise ValueError("Invalid unit number")
