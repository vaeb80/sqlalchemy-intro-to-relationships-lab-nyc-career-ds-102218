from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# write the Role and Actor classes below
class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    roles = relationship("Role", order_by="Role.id" ,back_populates='actor')

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character = Column(String)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor",uselist=False , back_populates='roles')


engine = create_engine('sqlite:///actors.db', echo=True)
Base.metadata.create_all(engine)
