from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

class data_base:
    conect_data = 'postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}'.format(
        user='admin',
        pwd='admin',
        host='localhost',
        port='5432',
        db='customerdata'
    )

    engine = create_engine(conect_data)
    Session = sessionmaker(bind=engine)
    session = Session()




