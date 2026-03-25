# 🧹 Limpeza de Dados com Python e Pandas

Projeto simples de limpeza e padronização de dados usando Python e Pandas.

## O que o projeto faz

- Remove linhas duplicadas
- Remove registros com campos obrigatórios nulos (nome e email)
- Preenche idade ausente com a mediana
- Padroniza nomes e emails (capitalização, espaços extras)
- Converte e valida datas
- Salva o resultado limpo em um novo CSV

## Tecnologias

- Python 3.x
- Pandas

## Como rodar

1. Instale as dependências:
```bash
pip install pandas
```

2. Gere o arquivo de dados brutos:
```bash
python gerar_dados.py
```

3. Execute a limpeza:
```bash
python limpeza.py
```

4. O arquivo `dados_limpos.csv` será criado na mesma pasta.

## Estrutura

```
01-limpeza-csv/
├── gerar_dados.py     # Gera um CSV com dados bagunçados para teste
├── limpeza.py         # Script principal de limpeza
├── dados_brutos.csv   # Gerado pelo gerar_dados.py
├── dados_limpos.csv   # Gerado pelo limpeza.py
└── README.md
```

## Aprendizados

- Uso de `dropna()`, `drop_duplicates()`, `fillna()`
- Manipulação de strings com `.str`
- Conversão e formatação de datas com `pd.to_datetime()`
