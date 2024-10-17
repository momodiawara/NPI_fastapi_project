import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Définir le chemin absolu pour le répertoire 'databases'
base_dir = os.path.abspath(os.path.dirname(__file__))
db_directory = os.path.join(base_dir, '../databases')

# Créer le répertoire 'databases' s'il n'existe pas
os.makedirs(db_directory, exist_ok=True)

# Définir l'URL de la base de données pour qu'elle soit dans le répertoire 'databases'
DATABASE_URL = f"sqlite:///{os.path.join(db_directory, 'operations.db')}"

# Création du moteur SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Définition de la base pour les modèles
Base = declarative_base()

# Modèle de la table 'operations'
class Operation(Base):
    __tablename__ = "operations"
    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String, index=True)
    expressionInfix = Column(String, default="")
    result = Column(Float)

# Création des tables dans la base de données
Base.metadata.create_all(bind=engine)

# Création d'une session pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
