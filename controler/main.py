from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from controler import Calcul
import pandas as pd
import io 
import logging
import sys
import os

# Configuration de logging
logging.basicConfig(level=logging.INFO)

# Ajout du répertoire 'databases' au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../databases')))
from database import Operation, SessionLocal 

# Définition du modèle de données pour la requête
class ExpressionRequest(BaseModel):
    expression: str
    

# Création des instances (FastAPI et de la classe Calcul)
app = FastAPI()
calcul = Calcul()


# Dépendance pour optenir une session de base de données pour chaque requête
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#unecreation d'une et avec Flask c'est "@app.route("/")" 
@app.post("/evaluation/")
async def evalueExpression(request: ExpressionRequest,db: Session = Depends(get_db)):

    try:
        # Accédez à l'expression via request
        result = calcul.evaluation(request.expression)  

        infix : str = ""

        if isinstance( result, (int,float) ):
            infix = calcul.normalisation(request.expression)
        
        operation = Operation(expression=request.expression,expressionInfix=infix, result=result)
         # Ajout de l'operation à la session
        db.add(operation)
        # Validez la transaction
        db.commit()
        # Rafraîchir la database pour obtenir l'essemble des données
        db.refresh(operation)  

        print(infix)
        
        return {"result": result}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/operations/csv")
async def get_operations_csv(db: Session = Depends(get_db)):

    try:
        # Récupérer toutes les opérations depuis la base de données(SELECT * FROM database)
        operations = db.query(Operation).all()

        # Vérifier s'il y a des lignes dans la base de données
        if not operations:
            logging.warning("Aucune opération trouvée dans la base de données")
            raise HTTPException(status_code=404, detail="La Base de données est vide.")

        #Création d'un dictionnaire des données en recuperarnt toute les lignes de database
        data = {
            "ID":[op.id for op in operations],
            "Expression":[op.expression for op in operations],
            "ExpressionNormal":[op.expressionInfix for op in operations],
            "Resultat":[op.result for op in operations],
        }

        #Création d'un dataFrame avec pandas
        df = pd.DataFrame(data)

        # déclarer le répertoire où enregistrer le fichier CSV
        outputDIR = os.path.join(os.path.dirname(__file__), '../outputFiles')
        os.makedirs(outputDIR, exist_ok=True)

        # Enregistrer le fichier CSV
        file_path = os.path.join(outputDIR, "output.csv")
        df.to_csv(file_path, index=False)

        # Retourner le fichier CSV sous forme de réponse
        return FileResponse(path=file_path, media_type="text/csv", filename="output.csv")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/clean")
async def clearDatabase(db: Session = Depends(get_db)):

    try:

        db.query(Operation).delete()
        db.commit()
        return {"message": "La base de données à été vidée avec succès."}

    except Exception as e :
        db.rollback()
        raise  HTTPException(status_code=500, detail=str(e))

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
