from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

Base = declarative_base()


class Users(Base):
    """Employees Manager Model"""
    __tablename__ = 'users'
    emp_id = db.Column(db.Integer(), primary_key=True)
    emp_name = db.Column(db.String(50), nullable=False)
    emp_city = db.Column(db.String(50))

    # Representation
    def __repr__(self):
        return "<Managers: Id={}, Name={}>".format(self.emp_id, self.emp_name)

