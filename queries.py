from models import *
from sqlalchemy import create_engine, and_

engine = create_engine('sqlite:///actors.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


# def return_gwyneth_paltrows_roles():
#     return session.query(Actor).filter(Actor.name == "Gwyneth Paltrow").\
#             first().roles

def return_tom_hanks_2nd_role():
    return session.query(Role).join(Actor).\
        filter(and_(Actor.name == "Tom Hanks", Role.id == 2)).first()

def return_gwyneth_paltrows_roles():
    return session.query(Role).join(Actor).filter(Actor.name == "Gwyneth Paltrow").all()
