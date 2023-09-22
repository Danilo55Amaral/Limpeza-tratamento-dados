##      Preparação 

# É necessário fazer algumas importações como da Bilioteca Pandas 
# para tratar os dados como um DataFrame, com isso conseguimos importar
# os dados de forma tabular e fazer vários tipos de tratamentos..

# A biblioteca seaborn é utilizada para alguns tipos de gráficos.

# Abiblioteca statistics que permite subistiuir alguns dados faltantes 
# utilizando a mediana, e aqui também vamos calcular o desvio padrão para
# usar como parâmetro.

import pandas as pd
import seaborn as srn
import statistics  as sts

##      Criando DataFrame
# Fazendo a importação de um conjunto de Dados. PS - sep é um separador de ;
dataset = pd.read_csv("Churn.csv", sep=";")
# visulizando esses dados.
dataset.head()

# X0	X1	X2	X3	X4	X4.1	X6	X7	X8	X9	X10	X11
# 0	1	619	RS	Feminino	42	2	0	1	1	1	10134888.0	1
# 1	2	608	SC	Feminino	41	1	8380786	1	0	1	11254258.0	0
# 2	3	502	RS	Feminino	42	8	1596608	3	1	0	11393157.0	1
# 3	4	699	RS	Feminino	39	1	0	2	0	0	9382663.0	0
# 4	5	850	SC	Feminino	43	2	12551082	1	1	1	790841.0	0

# Note que ao observar esses dados que foram retornados do DataFrame as colunas 
# Estão nomeadas sem nenhum significado, isso é um problema comum que pode ser 
# encontrado na hora em que se faz limpeza e tratamento de dados. 
# Uma das coisas que é importante fazer aqui é dá significado a essas colunas.

# checando o tamanho do meu dataset
dataset.shape
# (999, 12)  
# Possue 999 linas e 12 colunas.


##         Tratando as Colunas 
# A primeira coisa que vai ser feita aqui é resolver o problema das colunas 
# par afazer isso basta dar nomes para essas colunas.
dataset.columns = ["Id","Score","Estado","Genero","Idade","Patrimonio","Saldo","Produtos","TemCartCredito",
                    "Ativo","Salario","Saiu"]

#visulizando / Note que as colunas agora possuem nomes e significados.
dataset.head()
# Id	Score	Estado	Genero	Idade	Patrimonio	Saldo	Produtos	TemCartCredito	Ativo	Salario	Saiu
# 0	1	619	RS	Feminino	42	2	0	1	1	1	10134888.0	1
# 1	2	608	SC	Feminino	41	1	8380786	1	0	1	11254258.0	0
# 2	3	502	RS	Feminino	42	8	1596608	3	1	0	11393157.0	1
# 3	4	699	RS	Feminino	39	1	0	2	0	0	9382663.0	0
# 4	5	850	SC	Feminino	43	2	12551082	1	1	1	790841.0	0


# PS - Esses Dados são de uma instituição financeira e o objetivo é criar um modelo de charnel análise. 
# O objetivo desse tipo de análise é prever os clientes que vão deixar a empresa para que possa ser 
# Tomada alguma medida preventiva afim de evitar a saida desses clientes.


##            Análise exploratória dos Dados

# Em qualquer tipo de análise o primeiro passo é realizar uma análise exploratória dos dados
# o objetivo desse tipo de análise é conhece os dados. Com isso é possíveo detectar problemas 
# que esses dados podem ter.

# Existem regras de negócios que são universais como a idade, não se pode ter uma idade negativa
# nem uma idade absurda como 900 anos, porém existem questões que vão depender do tipo do negócio
# como se esse banco atende apenas pessoas de uma determinada região ou todo o país.

# Para limpar e tratar os dados é necessário conhecer as regras de negócios que são do dominio dos 
# dados.

# Uma das coisas que é importante nesse tipo de análise é indentificar os dados faltantes e preencher 
# esses dados. Por que dados faltantes é um problema na hora de utilizar aprendizado de máquina. 
# Geralmente esses valores são subistituidos com a mediana quando são numéricos e com a moda quando 
# são valores categóricos.

