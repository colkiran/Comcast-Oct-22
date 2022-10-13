
import O14SqlalchemySqlite301 as db
from sqlalchemy.orm import sessionmaker
import random

Session = sessionmaker(bind=db.engine)
session = Session()

tr = db.Player('PLY1001', "Sachin Tendulkar", "Cricket", "100 centuries")
session.add(tr)

session.commit()

