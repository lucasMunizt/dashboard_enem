import pandas as pd

df = pd.read_csv("DashBoard_limpo_atualizado.csv",sep=";", encoding="latin-1")


colunas_Aluno = [
    "NU_INSCRICAO","TP_FAIXA_ETARIA", "TP_SEXO", "TP_COR_RACA", "TP_ESCOLA", "Q006"

]

colunas_Notas = [
    "NU_INSCRICAO","NU_NOTA_MT","NU_NOTA_CN","NU_NOTA_LC","NU_NOTA_CH","NU_NOTA_REDACAO", 'NU_INSCRICAO',
]

colunas_Loc = [
    "NO_MUNICIPIO_PROVA","SG_UF_PROVA","TP_CAPITAL","NO_REGIAO"
]




print("colunas aluno ", colunas_Aluno) 
print("\n")
print("colunas notas", colunas_Notas)
print("\n")
print("colunas localizacao", colunas_Loc)
df_selecionados_alunos = df[colunas_Aluno]
df_selecionados_notas = df[colunas_Notas]
df_selecionados_loc = df[colunas_Loc]

df_selecionados_alunos.to_csv("colunas_alunos.csv", index=False, sep=";")
df_selecionados_notas.to_csv("colunas_notas.csv", index=False, sep=";")
df_selecionados_loc.to_csv("colunas_loc.csv", index=False, sep=";")




