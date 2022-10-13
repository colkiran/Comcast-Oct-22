
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connect to sqlite3 database
engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)

# manage tables
base = declarative_base()

class Player(base):

    __tablename__ = "Player"

    playerid = Column(String, primary_key=True)
    plyname = Column(String)
    sport = Column(String)
    achmnt = Column(String)

    def __init__(self, playerid, plyname, sport, achmt):
        self.playerid = playerid
        self.plyname = plyname
        self.sport = sport
        self.achmnt = achmt

base.metadata.create_all(engine)
