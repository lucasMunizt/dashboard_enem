import pandas as pd

df = pd.read_csv("limpo_sad.csv",sep=";", encoding="utf-8")

# md_regiaoNordeste = df[df["NO_REGIAO"] == "Nordeste"][
#     ["NU_NOTA_MT", "NU_NOTA_CN", "NU_NOTA_LC", "NU_NOTA_CH", "NU_NOTA_REDACAO"]
# ].mean()

qtdParticipantes = df["NU_INSCRICAO"].count()

df["media_geral"] = df[["NU_NOTA_MT", "NU_NOTA_CN", "NU_NOTA_LC", "NU_NOTA_CH", "NU_NOTA_REDACAO"]].mean(axis=1)

# calcula a média por estado
media_por_estado = df.groupby("SG_UF_PROVA")["media_geral"].mean()
#media da redação por municipio
media_por_munnicipio_redação = df.groupby("NO_MUNICIPIO_PROVA")["NU_NOTA_REDACAO"].mean()

#calcular a media pela faixa socio economica
media_por_faixa_SC = df.groupby("Q006")["media_geral"].mean()
media_por_faixa_SC_genero = df.groupby(["Q006","TP_SEXO"])["media_geral"].mean()

bins = [0, 7, 11, 15, 20]
labels = ["≤22 anos", "23-30 anos", "31-50 anos", "50+ anos"]

df["Faixa_Idade"] = pd.cut(df["TP_FAIXA_ETARIA"], bins=bins, labels=labels)

# print(media_por_estado)
# print(media_por_munnicipio_redação)

# print(media_por_faixa_SC)

# print(media_por_faixa_SC_genero)
print(df.groupby("Faixa_Idade")["NU_NOTA_REDACAO"].mean())


# print("Médias das notas no Nordeste:\n", md_regiaoNordeste)
# print("quantidades de particpantes: ",qtdParticipantes)

# print("soma:\n ",)