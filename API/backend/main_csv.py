import csv
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo para representar uma operadora
class Operadora(BaseModel):
    registro_ans: str
    cnpj: str
    razao_social: str
    nome_fantasia: str
    modalidade: str
    cidade: str
    uf: str
    telefone: str
    email: str

# Lista onde os dados do CSV serão armazenados
operadoras = []

# Função para carregar os dados do CSV na memória
def carregar_csv():
    global operadoras
    with open("Relatorio_cadop.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            operadoras.append(
                Operadora(
                    registro_ans=row["Registro_ANS"],
                    cnpj=row["CNPJ"],
                    razao_social=row["Razao_Social"],
                    nome_fantasia=row["Nome_Fantasia"] if row["Nome_Fantasia"] else row["Razao_Social"],
                    modalidade=row["Modalidade"],
                    cidade=row["Cidade"],
                    uf=row["UF"],
                    telefone=row["Telefone"],
                    email=row["Endereco_eletronico"],
                )
            )

# Carregar os dados ao iniciar o servidor
carregar_csv()

# Função para calcular a relevância do nome buscado
def calcular_relevancia(termo, nome_operadora):
    termo = termo.lower()
    nome_operadora = nome_operadora.lower()

    if termo == nome_operadora:
        return 3  # Match exato → Prioridade máxima
    elif nome_operadora.startswith(termo):
        return 2  # O termo está no começo do nome → Prioridade alta
    elif termo in nome_operadora:
        return 1  # O termo está em qualquer lugar do nome → Prioridade baixa
    return 0  # Sem correspondência

@app.get("/buscar_operadora", response_model=List[Operadora])
async def buscar_operadora(nome: str):
    resultados = [
        (op, calcular_relevancia(nome, op.nome_fantasia)) for op in operadoras
    ]
    
    # Filtra apenas as operadoras que tiveram alguma correspondência
    resultados_filtrados = [op for op, score in resultados if score > 0]

    # Ordena os resultados pela relevância (do maior para o menor)
    resultados_filtrados.sort(key=lambda x: calcular_relevancia(nome, x.nome_fantasia), reverse=True)

    return resultados_filtrados

@app.get("/")
async def root():
    return {"message": "API FastAPI funcionando!"}
