import pandas as pd

df = pd.read_csv("MICRODADOS_ENEM_2023.csv",sep=";", encoding="latin-1")

df = df[
    (df["TP_PRESENCA_CN"] == 1) &
    (df["TP_PRESENCA_CH"] == 1) &
    (df["TP_PRESENCA_LC"] == 1) &
    (df["TP_PRESENCA_MT"] == 1)
]
df = df.dropna(subset=["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","NU_NOTA_REDACAO"])

df = df[
    (df["NU_NOTA_MT"] > 0) &
    (df["NU_NOTA_CN"] > 0) &
    (df["NU_NOTA_LC"] > 0) &
    (df["NU_NOTA_CH"] > 0) &
    (df["NU_NOTA_REDACAO"] > 0)
]
filtro_redacao = (df['TP_STATUS_REDACAO'] == 1)

print("Após remoção de notas zeradas:", df.shape)

# df = df[df["SG_UF_PROVA"] == "CE"]
# print("NOTAS CE ","\n",df[["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","NU_NOTA_REDACAO"]])

colunas = [
    "TP_PRESENCA_CN","TP_PRESENCA_CH","TP_PRESENCA_LC","TP_PRESENCA_MT","TP_ESCOLA",
    "TP_COR_RACA","TP_STATUS_REDACAO",'TP_SEXO','TP_FAIXA_ETARIA',
    "NU_NOTA_MT","NU_NOTA_CN","NU_NOTA_LC","NU_NOTA_CH","NU_NOTA_REDACAO", 'NU_INSCRICAO',
    "Q006","SG_UF_PROVA",'NO_MUNICIPIO_PROVA'
]


print("\nValores nulos por coluna:")
df_selecionado = df[colunas]
# print("quantidade", len(df_selecionado))
print(df_selecionado.isnull().sum())
#dados novos
df_selecionado.to_csv("limpo_sad.csv", index=False, sep=";", encoding="utf-8")