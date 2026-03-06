from sqlalchemy.orm import Session

from .models import MonDonnee


# Créer une donnée
def create_donnee(db: Session, nom: str, valeur: float):
    nouvelle = MonDonnee(nom=nom, valeur=valeur)
    db.add(nouvelle)
    db.commit()
    db.refresh(nouvelle)
    return nouvelle


# Lire toutes les données
def get_donnees(db: Session):
    return db.query(MonDonnee).all()


# Lire une donnée par id
def get_donnee(db: Session, id: int):
    return db.query(MonDonnee).filter(MonDonnee.id == id).first()
