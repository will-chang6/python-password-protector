from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from texttable import Texttable

Base = declarative_base()

class DisplayTable(Base):
    # creating table name
    __tablename__ = 'passwords'

    # table attirbutes with key
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    # this line is used create the table with the above attributes
    def __repr__(self):
        return f"Password(id={self.id}, username='{self.username}', password='{self.password}')"

# checks if script run directly and not imported
if __name__ == '__main__':
    # standard command for URL call assigned to engine to be used in the next line
    engine = create_engine('sqlite:///passwords.db')

    # generates required SQL data from stored data in Base class metadata
    Base.metadata.create_all(engine)

    # creates sessionmaker class instance on the engine variable connecting them so we can execute queries in the correct location
    Session = sessionmaker(bind=engine)

    # creates session object that will be used to execute queries in the correct location
    session = Session()

    # this executes the query in the correct location and returns the results in list form
    data = session.query(DisplayTable).all()

    # creates TextTable object that will be used to display results in an easy to read format
    textTable = Texttable()

    # creates TextTable headers that our data will be displayed under
    textTable.header(['Username', 'Password'])

    # loop that will create a new row from each username and password to be displayed
    for datum in data:
        textTable.add_row([datum.username, datum.password])

    # print textTable with draw function to calculate then draw the table based on the data it is given
    print(textTable.draw())
