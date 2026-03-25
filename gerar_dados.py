import pandas as pd
import numpy as np

# Gera um CSV "sujo" para testar a limpeza
data = {
    "nome": ["ana silva", "JOÃO SOUZA", "  Maria Costa  ", "Pedro Lima", "Ana Silva", None, "Carlos Melo"],
    "email": ["ANA@GMAIL.COM", "joao@gmail.com", "maria@gmail.com ", "pedro@gmail.com", "ana@gmail.com", "sem@email.com", None],
    "idade": [25, None, 30, 22, 25, 28, 35],
    "data_cadastro": ["2024-01-15", "15/02/2024", "2024-03-20", "2024-04-10", "2024-01-15", "data-invalida", "2024-05-01"],
    "cidade": ["São Paulo", "Rio de Janeiro", "Curitiba", "Salvador", "São Paulo", "Fortaleza", "Recife"]
}

df = pd.DataFrame(data)
df.to_csv("dados_brutos.csv", index=False)
print("Arquivo 'dados_brutos.csv' gerado com sucesso!")
