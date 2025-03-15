from model.entity import *

class Users(Base):
    __tablename__ = 'users'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _username = Column("username", String(20), unique=True, nullable=False)
    _password = Column("password", String(20), nullable=False)
    _role = Column("role", String(10), nullable=False)

    units = relationship("Units", back_populates="user")
    user_units = relationship("UnitUserConnector", back_populates="user")

    def __init__(self, username, password, role, id=None):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
