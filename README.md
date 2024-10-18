# NPI_fastapi_project
# L' Application FastAPI avec SQLite et Docker

La notation polonaise inverse (ou notation post-fixée) est une façon d'écrire des expressions mathématiques où les opérateurs viennent après les nombres. Par exemple, au lieu d'écrire 3+4 , on écrit 3 4 +, ce qui permet de faire des calculs sans utiliser de parenthèses.

## Description

    Ce projet utilise FastAPI, une base de données SQLite, pour construire une API qui peut être déployée via Docker et Docker-Compose. Il permet de gérer des expressions mathématiques en notation polonaise inverse (NPI), de les évaluer et de les stocker dans une base de données, et de générer des fichiers CSV avec les résultats des opérations.

## Principales fonctionnalités :

    - Évaluation d'expressions en notation polonaise inverse (NPI).
    - Sauvegarde des expressions inversée, normalisée et des résultats dans une base de données SQLite.
    - Téléchargement des résultats sous forme de fichier CSV.
    - Suppression des résultats dans la base de données.

##Prérequis
    Il est crucial de procéder à l'installation des logiciels suivants :

        - sudo apt install python3-pip
        - [Docker](https://www.docker.com/get-started) installé (version 19.03 ou supérieure).
        - [Docker Compose](https://docs.docker.com/compose/install/) installé (version 1.27 ou supérieure).

## Installation

1. Clonez ce dépôt dans votre machine locale :

    ```bash
    git clone https://github.com/votre-utilisateur/votre-repo.git
    cd votre-repo

2. Veillez à ce que Docker et Docker-Compose soient installés sur votre machine.

3. Élaborez et démarrez les services en utilisant Docker Compose :

    docker-compose up --build
    
    Cette commande implique :

        - Élaborer l'image Docker pour l'application FastAPI.
        - Activer les conteneurs FastAPI et SQLite.
        
## Utilisation de l'interface API.

Pour accéder à l'API, rendez-vous à l'adresse suivante : `http://localhost:8000`

## Endpoints principaux :

#Analyser une expression NPI : ''POST/evalueExpression/.''
   
   - **Exemple de requête** :
  
  ```bash
   Curl -X POST "http://localhost:8000/evalueExpression/" \
   -H "Content-Type: application/json" \
   -d '{"expression": "5 1 2 + 4 * + 3 -"}'
   
   Réponse :
       {
          "result": 14
        }
    
## Télécharger les opérations sous forme de fichier CSV : GET /operations/csv

    Exemple de requête :
    
        curl -X GET "http://localhost:8000/operations/csv"
        
    Les opérations enregistrées dans la base de données seront consignées dans ce fichier CSV et accessibles dans le répertoire outputFiles.
    
## Nottoyer de la base de données : DELETE/clean

    Exemple de requête :
    
        curl -X DELETE "http://localhost:8000/clean"

## Base de données
      
    SQLite est utilisé dans ce projet pour stocker les expressions et les résultats des évaluations dans une base de données locale. SQLite est intégré directement dans l'image Docker sans nécessiter de service externe.

## Structure du projet

    /NPI_fastapi_project
    |-- /controler
    |   |-- controler.py             # Fichier contenant les opérations nécessaires
    |   |-- main.py                  # Fichier FastAPI principal
    |-- /databases
    |   |-- database.py              # Configuration de la base de données SQLite
    |-- /Test_Unitaires
    |   |-- TestCalcul.py            # Fichier pour les tests unitaires réalisés sur les differentes fonctions
    |-- /outputFiles                 # Dossier pour les fichiers CSV générés
    |-- requirements.txt             # Fichier des dépendances Python
    |-- Dockerfile                   # Fichier Docker pour construire l'image
    |-- docker-compose.yml           # Fichier Docker Compose pour orchestration

        
## Test

NB :
Les opérations prises en charge en notation polonaise inverse dans ce contexte sont : addition (+), soustraction (-), multiplication (*), division (/), modulo (%), et puissance. Voici une brève explication de chacune :

    1) Addition (+) : Ajoute deux nombres. Par exemple, en NPI, 3+4 devient 3 4 +.
    2) Soustraction (-) : Soustrait un nombre du précédent. Par exemple, 5−2 devient 5 2 -.
    3) Multiplication (*) : Multiplie deux nombres. Par exemple, 6×3 devient 6 3 *.
    4) Division (/) : Divise le premier nombre par le second. Par exemple, 8/28 devient 8 2 /.
    5) Modulo (%) : Donne le reste d'une division. Par exemple le reste de la division de 7 par 3 devient 7 3 %.
    6) Puissance (^) : Élève un nombre à la puissance d'un autre. Par exemple, 2**3 devient 2 3 ^.

Vous pouvez tester l'API de plusieurs manières, notamment :

    1) Utiliser curl pour envoyer des requêtes HTTP depuis la ligne de commande.

        Voici un exemple de requête POST pour évaluer une expression NPI :
        
            curl -X POST "http://localhost:8000/evaluation/" \
            -H "Content-Type: application/json" \
            -d '{"expression": "5 1 2 + 4 * + 3 -"}'

    2) Pour envoyer des requêtes HTTP via une interface graphique, vous pouvez utiliser Postman ou tout autre client HTTP.
    
        Il est possible de configurer des requêtes GET, POST, DELETE, etc., et d'observer les réponses en temps réel.
        
    3) Grâce à Swagger, FastAPI génère automatiquement une documentation interactive de l'API. Explorez et testez les différentes routes de l'API en utilisant cette interface.
    
        Après avoir lancé le projet, vous pouvez accéder à l'interface Swagger en utilisant l'URL suivante :
         
            http://localhost:8000/docs
            
            Vous pourrez tester chaque endpoint en utilisant une interface conviviale. Vous pouvez envoyer des requêtes, voir les réponses et comprendre la structure des requêtes et des réponses.

    4) Interface Redoc : En plus de Swagger, FastAPI propose également une interface de documentation avec Redoc. Vous pouvez y accéder via l'URL suivante :
    
        http://localhost:8000/redoc
