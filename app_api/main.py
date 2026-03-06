from fastapi import Depends, FastAPI
from modules import crud
from modules.connect import Base, SessionLocal, engine
from pydantic import BaseModel  # <--- AJOUTE CECI
from sqlalchemy.orm import Session


# --- AJOUTE CE SCHÉMA ICI ---
class DonneeSchema(BaseModel):
    nom: str
    valeur: float


# ----------------------------

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# MODIFIE CETTE ROUTE :
@app.post("/donnees")
def create(data: DonneeSchema, db: Session = Depends(get_db)):  # Utilise le schéma ici
    return crud.create_donnee(db, data.nom, data.valeur)


# GET : lire toutes les données
@app.get("/donnees")
def read_all(db: Session = Depends(get_db)):
    return crud.get_donnees(db)


# GET : lire une donnée par id
@app.get("/donnees/{id}")
def read_one(id: int, db: Session = Depends(get_db)):
    return crud.get_donnee(db, id)
