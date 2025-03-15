from model.entity import *

class UnitUserConnector(Base):
    __tablename__ = 'unit_user_connector'

    id = Column(Integer, primary_key=True, autoincrement=True)
    unit_id = Column(Integer, ForeignKey('units.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    unit = relationship("Units", back_populates="unit_users")
    user = relationship("Users", back_populates="user_units")

    def __init__(self, unit, user):
        self.unit = unit
        self.user = user



