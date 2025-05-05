#Esta aplicação é referente a análise de dados utilizando a linguagem python. 

#Os dados utilizados na análise foram extraídos do seguinte site: https://dados.rs.gov.br/dataset/2024-despesas-do-estado
#São referentes aos gastos mensais realizados pelo estado do Rio Grande do Sul no ano de 2024.
#Para esta análise utilizei apenas os três primeiros meses do ano.

#A aplicação concatena os dados dos três arquivos .csv exportados no site, e posteriormente realiza uma filtragem:
  # 1 - Seleciona somente as colunas Mes;TipoGasto;Valor;Municipio
  # 2 - Seleciona apenas dados do município de Canoas/RS
  # 3 - Ajusta a formatação dos valores removendo pontos de milhar e substituindo vírgula decimal por ponto


#São gerados três gráficos:
  # 1 - o maior valor gasto único
  # 2 - tipo de gasto que mais se repete ao longo de cada mês
  # 3 - soma do valor total gasto em cada mês