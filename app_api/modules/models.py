from sqlalchemy import Column, Float, Integer, String

from .connect import Base


class MonDonnee(Base):
    __tablename__ = "donnees"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    valeur = Column(Float)
