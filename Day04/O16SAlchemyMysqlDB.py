
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connect to sqlite3 database
# engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
engine = create_engine("mysql+pymysql://root@localhost/players", echo=True)
# manage tables
base = declarative_base()

class Player(base):

    __tablename__ = "player"

    playerid = Column(String(10), primary_key=True)
    plyname = Column(String(50))
    sport = Column(String(30))
    achmnt = Column(String(50))

    def __init__(self, playerid, plyname, sport, achmt):
        self.playerid = playerid
        self.plyname = plyname
        self.sport = sport
        self.achmnt = achmt

base.metadata.create_all(engine)
