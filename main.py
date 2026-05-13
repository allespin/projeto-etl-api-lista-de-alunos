from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/puxar-nomes")
def listar_nomes():
    # Lê o arquivo CSV
    df = pd.read_csv('dsproject.csv')
    
    # Converte a coluna 'Nome' em uma lista do Python
    # Certifique-se de que o nome da coluna no CSV é exatamente 'Nome'
    nomes = df['Nome'].tolist()
    
    return {"usuarios": nomes}