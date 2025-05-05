import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)

df1 = pd.read_csv(r"C:\Users\junio\Desktop\faculdade\LaSalle\Introdução a programação em análise de dados\gasto-rs-202401\Gasto-RS-202401.csv", 
                 sep=';',
                 encoding='latin1'
                 )

df2 = pd.read_csv(r"C:\Users\junio\Desktop\faculdade\LaSalle\Introdução a programação em análise de dados\gasto-rs-202402\Gasto-RS-202402.csv", 
                 sep=';',
                 encoding='latin1'
                 )

df3 = pd.read_csv(r"C:\Users\junio\Desktop\faculdade\LaSalle\Introdução a programação em análise de dados\gasto-rs-202403\Gasto-RS-202403.csv", 
                 sep=';',
                 encoding='latin1'
                 )


df_total = pd.concat([df1, df2, df3], ignore_index=True)

#LIMPANDO AS COLUNAS QUE NÃO POSSUEM O MUNICÍPIO E QUE SÃO IGUAIS A CANOAS-----
df_total = df_total[df_total["Municipio"].notnull()]
df_total = df_total[df_total["Municipio"] == "CANOAS"]

df_total = df_total[['Mes', 'TipoGasto', 'Valor', 'Municipio']]

#----------AJUSTANDO FORMATAÇÃO DA COLUNA E CONVERTENDO PARA NUMERIC-----------
df_total["Valor"] = (
    df_total["Valor"]
    .astype(str)
    .str.replace(".", "", regex=False)        # Remove pontos (milhar)
    .str.replace(",", ".", regex=False)       # Troca vírgula decimal por ponto
)
df_total["Valor"] = pd.to_numeric(df_total["Valor"], errors="coerce")
#-----------------------------------------------------------------------------

#Gerando .CSV dos dados após filtragem----------------------------------------
df_total.to_csv("dados_filtrados.csv", index=False, sep=';', encoding='utf-8')
#-----------------------------------------------------------------------------

#-------------MAIOR VALOR GASTO ÚNICO-----------------------------------------
maior_gasto = df_total.loc[df_total["Valor"].idxmax()]

plt.figure(figsize=(8, 4))
plt.bar(["Maior Gasto"], [maior_gasto["Valor"]], color="tomato")
plt.title("Maior Valor Gasto Único")
plt.ylabel("Valor")
plt.tight_layout()
plt.show()
#------------------------------------------------------------------------------

#TIPO DE GASTO QUE MAIS SE REPETE EM CADA MÊS--------------------------------------------------------------
mais_frequente_por_mes = df_total.groupby(["Mes", "TipoGasto"]).size().reset_index(name="Ocorrencias")
indice = mais_frequente_por_mes.groupby("Mes")["Ocorrencias"].idxmax()
tipos_mais_frequentes = mais_frequente_por_mes.loc[indice]

plt.figure(figsize=(12, 6))
plt.bar(tipos_mais_frequentes["Mes"], tipos_mais_frequentes["Ocorrencias"], color="cornflowerblue")
bars = plt.bar(tipos_mais_frequentes["Mes"], tipos_mais_frequentes["Ocorrencias"], color="cornflowerblue")

# Lista com nomes dos meses
nomes_meses_tipogasto = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

#Adiciona o nome dos meses de acordo com o identificador da coluna------
meses_tipogasto = tipos_mais_frequentes["Mes"]
nomes = [nomes_meses_tipogasto[int(m)] for m in meses_tipogasto]
plt.xticks(ticks=meses_tipogasto, labels=nomes, rotation=45)
#-----------------------------------------------------------------------

#Adiciona o nome do tipo de gasto sobre cada coluna---------------------
for bar, tipo in zip(bars, tipos_mais_frequentes["TipoGasto"]):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 5, tipo, 
             ha='center', va='bottom', fontsize=9, fontweight='bold')
#-----------------------------------------------------------------------

plt.title("Tipo de Gasto Mais Frequente por Mês")
plt.xlabel("Mês")
plt.ylabel("Número de Ocorrências")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------------

#SOMA DE GASTOS POR MÊS-------------------------------------------------------------------------
soma_por_mes = df_total.groupby("Mes")["Valor"].sum().reset_index()

# Lista com nomes dos meses
nomes_meses_somatorio = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

plt.figure(figsize=(12, 6))

meses_somatorio = soma_por_mes["Mes"]
bars = plt.bar(meses_somatorio, soma_por_mes["Valor"], color='skyblue')

#Adiciona o nome dos meses de acordo com o identificador da coluna------
nomes_somatorio = [nomes_meses_somatorio[int(m)] for m in meses_somatorio]
plt.xticks(ticks=meses_somatorio, labels=nomes, rotation=45)
#-----------------------------------------------------------------------

#Adiciona leganda com o valor total de cada mês sobre a coluna----------
for bar in bars:
    altura = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, altura + 0.5,
             f'R$ {altura:,.2f}', ha='center', va='bottom', fontsize=9)
#-----------------------------------------------------------------------

plt.title("Soma de Gastos por Mês")
plt.xlabel("Mês")
plt.ylabel("Valor Total")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#-----------------------------------------------------------------------------------------------

