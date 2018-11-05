from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below
tom_hanks = Actor(name='Tom Hanks')
tom_hanks.roles = [Role(character = 'Forrest Gump'),Role(character = 'Jim Lovell'), Role(character= 'Woody'), Role(character = 'Robert Langdon')]

gwyneth_paltrow = Actor(name='Gwyneth Paltrow')
gwyneth_paltrow.roles = [Role(character='Pepper Potts'), Role(character='Margot Tenenbaum')]

# woody_harrelson = Actor(name='Woody Harrelson')
# woody_harrelson.roles = [Role(character='Detective Marty Hart'), Role(character='Mickey Knox')]

hbc = Actor(name="Helena Bonham Carter")
hbc.roles = [Role(character='Bellatrix Lestrange'), Role(character='Madame Thénardier'), Role(character='Marla Singer'), Role(character='Rose Weil')]

session.add_all([tom_hanks, gwyneth_paltrow, hbc])
session.commit()
