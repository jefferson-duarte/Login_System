from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# USER = 'root'
# PASSWORD = 'root'
# HOST = 'localhost'
# BANCO = 'sistema_login'
# PORT = '3306'

# CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{BANCO}'

CONN = 'sqlite:///database/sqlite.db'

engine = create_engine(CONN)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class RegisterCustomer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(64))


Base.metadata.create_all(engine)
