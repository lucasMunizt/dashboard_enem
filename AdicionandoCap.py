import pandas as pd

df = pd.read_csv("limpo_sad.csv",sep=";", encoding="utf-8")

mapa_regioes = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}


lista_capitais = [
    'Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília', 'Vitória', 'Goiânia', 
    'São Luís', 'Cuiabá', 'Campo Grande', 'Belo Horizonte', 'Belém', 'João Pessoa', 'Curitiba', 'Recife', 
    'Teresina', 'Rio de Janeiro', 'Natal', 'Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis', 
    'São Paulo', 'Aracaju', 'Palmas'
]


df["Faixa_Idade"] = pd.cut(
    df["TP_FAIXA_ETARIA"],
    bins=[0, 7, 11, 15, 20],  
    labels=[
        "Até 22 anos",
        "23 - 30 anos",
        "31 - 50 anos",
        "50+ anos"
    ],
    include_lowest=True
)


df['NO_REGIAO'] = df['SG_UF_PROVA'].map(mapa_regioes)
    
    # --- Criando a coluna TP_CAPITAL (Pergunta 8) ---
    # Usamos uma função lambda com `.apply()` para verificar se cada município está na lista de capitais.
df['TP_CAPITAL'] = df['NO_MUNICIPIO_PROVA'].apply(
    lambda municipio: 'Capital' if municipio in lista_capitais else 'Interior'
)

print("\n--- SUCESSO! Colunas 'NO_REGIAO' e 'TP_CAPITAL' criadas. ---")
    
    # --- Verificação ---
print("\nAmostra dos dados com as novas colunas:")
df.to_csv("limpo_atualizado.csv", index=False, sep=";")
    # Exibimos as colunas relevantes para confirmar que as novas colunas foram criadas corretamente.
print(df[['SG_UF_PROVA', 'NO_REGIAO', 'NO_MUNICIPIO_PROVA', 'TP_CAPITAL']].head())