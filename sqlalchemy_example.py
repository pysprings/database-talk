from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker

base = declarative_base()


class RolodexEntry(base):
    __tablename__ = 'rolodex'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)


class Address(base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)

    house_number = Column(String)
    apt_number = Column(String)
    street_name = Column(String)

    city = Column(String)
    state = Column(String)
    zipcode = Column(String)

    country = Column(String)


if __name__ == '__main__':
    engine = create_engine('postgresql://user:password@localhost:5111sqlalchemy.db')
    base.metadata.create_all(engine)

    p1 = RolodexEntry(first_name='John', last_name='Doe', phone_number='719-555-1239')

    addr = Address()

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(p1)
    session.add(addr)
    session.commit()

    entry = session.query(RolodexEntry).filter(RolodexEntry.last_name=='Doe').first()
    entry.last_name = 'Foo'
    session.commit()
