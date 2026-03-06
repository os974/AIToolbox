import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 1. Charge les variables du fichier .env
load_dotenv()

# 2. Récupère l'URL. Si la variable n'existe pas, on met SQLite par défaut
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# 3. Création de l'engine
# Note : check_same_thread=False est nécessaire uniquement pour SQLite
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
