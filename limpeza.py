import pandas as pd

# Carrega o dataset
df = pd.read_csv("dados_brutos.csv")

print("=== ANTES DA LIMPEZA ===")
print(f"Linhas: {len(df)}")
print(f"Colunas: {list(df.columns)}")
print(f"Nulos:\n{df.isnull().sum()}\n")

# Remove duplicatas
df = df.drop_duplicates()

# Remove linhas onde campos essenciais são nulos
df = df.dropna(subset=["nome", "email"])

# Preenche nulos de idade com a mediana
if "idade" in df.columns:
    df["idade"] = df["idade"].fillna(df["idade"].median()).astype(int)

# Padroniza texto: remove espaços extras e coloca em minúsculo
if "nome" in df.columns:
    df["nome"] = df["nome"].str.strip().str.title()

if "email" in df.columns:
    df["email"] = df["email"].str.strip().str.lower()

# Padroniza coluna de data
if "data_cadastro" in df.columns:
    df["data_cadastro"] = pd.to_datetime(df["data_cadastro"], errors="coerce")
    df = df.dropna(subset=["data_cadastro"])
    df["data_cadastro"] = df["data_cadastro"].dt.strftime("%Y-%m-%d")

print("=== DEPOIS DA LIMPEZA ===")
print(f"Linhas: {len(df)}")
print(f"Nulos:\n{df.isnull().sum()}\n")

# Salva o resultado
df.to_csv("dados_limpos.csv", index=False)
print("Arquivo 'dados_limpos.csv' salvo com sucesso!")
