import uuid
from sqlalchemy import Column, create_engine
from sqlalchemy.dialects.oracle import RAW
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def test_issue():
    Base = declarative_base()
    engine = create_engine("oracle://cx_Oracle:dev@localhost", echo=False)
    Session = sessionmaker(bind=engine)


    class TestRaw(Base):
        __tablename__ = 'TEST'
        guid = Column("ID", RAW(16), primary_key=True) # RAW = oracle Binary

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()
    guid = uuid.UUID("05343899-b843-4f10-b460-94410bae1234")

    session.add(TestRaw(guid=guid.bytes))
    test = session.query(TestRaw).filter(TestRaw.guid == guid.bytes).one()
    assert test.guid == guid.bytes
