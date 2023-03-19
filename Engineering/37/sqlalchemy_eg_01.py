"""
    SQLAlchemy Example
"""
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


def get_engine(db_name=None):
    """Create SQLAlchemy Engine"""
    if db_name:
        return db.create_engine("mysql+mysqlconnector://rpython:Password-123@192.168.56.101:3306/{}".format(
            db_name
        ))
    else:
        return db.create_engine("mysql+mysqlconnector://rpython:Password-123@192.168.56.101:3306")


def get_connection(db_engine):
    """Creates SQLAlchemy DB Connection"""
    return db_engine.connect()


def get_session(db_engine):
    """Returns an Session"""
    ssn = sessionmaker()
    ssn.configure(bind=db_engine)
    return ssn()


def create_db(db_conn, db_name):
    """Creates a Database"""
    db_conn.execute(db.text("CREATE DATABASE IF NOT EXISTS {}".format(db_name)))


class Offices(Base):
    """Offices Model"""
    # Table
    __tablename__ = 'offices'
    # Columns
    office_id = db.Column(db.Integer(), primary_key=True)
    office_name = db.Column(db.String(50), nullable=False)
    office_city = db.Column(db.String(15), nullable=False)
    office_country = db.Column(db.String(15), nullable=False)
    office_strength = db.Column(db.Integer(), default=1000)

    # Representation
    def __repr__(self):
        return "<Offices: Id={}, Name={}>".format(self.office_id, self.office_name)


class Employees(Base):
    """Employees Model"""
    __tablename__ = 'employees'
    emp_id = db.Column(db.Integer(), primary_key=True)
    emp_name = db.Column(db.String(50), nullable=False)
    emp_phone = db.Column(db.Integer())
    emp_office = db.Column(db.Integer(), db.schema.ForeignKey('offices.office_id'), nullable=False)
    Office = relationship('Offices', backref='employees')

    # Representation
    def __repr__(self):
        return "<Employees: Id={}, Name={}>".format(self.emp_id, self.emp_name)


def create_all_objects(db_engine):
    """Create Database Objects"""
    Base.metadata.create_all(db_engine)


def check_uncommited_object(db_session):
    """Check uncommited object in SQLAlchemy Session"""
    return db_session.new


def commit_session(db_session):
    """Commit and SQLAlchemy Session"""
    db_session.commit()


def add_single_object_in_session(db_session, obj):
    """Adding an object to SQLAlchemy Session"""
    db_session.add(obj)


def add_multiple_object_in_session(db_session, obj_list):
    """Adding an object to SQLAlchemy Session"""
    db_session.add_all(obj_list)


# Self Join Usage
class Managers(Base):
    """Employees Manager Model"""
    __tablename__ = 'managers'
    emp_id = db.Column(db.Integer(), primary_key=True)
    emp_name = db.Column(db.String(50), nullable=False)
    emp_manager = db.Column(db.Integer())

    # Representation
    def __repr__(self):
        return "<Managers: Id={}, Name={}>".format(self.emp_id, self.emp_name)
