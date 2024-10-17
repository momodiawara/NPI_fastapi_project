# Utiliser une image officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail à /app
WORKDIR /app

# Copier le fichier requirements.txt dans l'image Docker
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le contenu du répertoire controler et databases dans le répertoire de travail de l'image
COPY controler/ ./controler/
COPY databases/ ./databases/
COPY Test_unitaires/ ./Test_unitaires/

# Exposer le port 8000 (FastAPI fonctionne par défaut sur ce port)
EXPOSE 8000

# Commande pour démarrer FastAPI
CMD ["uvicorn", "controler.main:app", "--host", "0.0.0.0", "--port", "8000"]

