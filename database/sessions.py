from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def return_session():
    # USER = 'root'
    # PASSWORD = 'root'
    # HOST = 'localhost'
    # BANCO = 'sistema_login'
    # PORT = '3306'

    # CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{BANCO}'

    CONN = 'sqlite:///database/sqlite.db'

    engine = create_engine(CONN)
    Session = sessionmaker(bind=engine)

    return Session()
