import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Person(Base):
    __tablename__ = 'Person'

    id = Column('id', Integer, primary_key=True)
    first_name = Column('Name', String)
    last_name = Column('Surname', String)
    date_of_birth = Column('Date of Birth', String)
    position = Column('Position', String)
    salary = Column('Salary', Integer)
    creation_date = Column('Entry time', DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'{self.id}: {self.first_name} {self.last_name}, {self.date_of_birth}, {self.position}, {self.salary}. {self.creation_date}'

engine = create_engine('sqlite:///employees.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

# Creating session for function placement

session = Session()

def pull_from_database():
    return session.query(Person).all()

def add_to_database(name,last_name,date_of_birth,position,salary):
    addition = Person()
    addition.first_name = name
    addition.last_name = last_name
    addition.date_of_birth = date_of_birth
    addition.position = position
    addition.salary = salary

    session.add(addition)
    session.commit()

def delete_from_database(item):
    session.delete(item)
    session.commit()

def update_information(item,name,last_name,date_of_birth,position,salary):
    the_person = item
    the_person.first_name = name
    the_person.last_name = last_name
    the_person.date_of_birth = date_of_birth
    the_person.position = position
    the_person.salary = salary
    session.commit()

session.close()