from Database import data_base
from datetime import datetime,date
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

dt   = datetime.now()
Base = declarative_base()

class User(Base):
    __tablename__ = 'customers'
    id            = Column(Integer,    primary_key=True)
    name          = Column(String)
    dob           = Column(Date)
    updated_at     = Column(DateTime)

    def __init__(self,  id,  name,   dob,    updated_at):
        self.id      = id
        self.name    = name
        self.dob     = dob
        self.updated_at  = updated_at


#CRUD alchemy
datasess = data_base.session
dataquery = datasess.query(User)
# #--Create
#
# adduser = User(id         =  7,
#                 name      = 'Alexander',
#                 dob       = date(1967, 5, 9),
#                 update_at = datetime.now())
# datasess.add(adduser)
# datasess.commit()
#
#
#--Read

for read in dataquery:
    a = f'{read.id}   {read.name}  {read.dob} '
    print(a)

# #--Update User
#
# x = dataquery.get(3)
# x.address = 'Hoang Sa'
# x.updated_at = datetime.now()
# datasess.commit()
#d
# #-- Delete User
# x = dataquery.get(4)
# datasess.delete(x)
# datasess.commit()
