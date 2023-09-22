# Analise Exploratória 

# Temos duas técnicas que podemos usar para explorar os dados
# Técnicas gráficas que geram gráficos visuais e alguns resumos 
# estatisticos.

# Explorando os Dados categoricos, contamos as categorias e podemos 
# utilizar um gráfico de barras ou um gráfico de setor para visualizar 
# essas categorias. Com dados numericos geramos um resumo estatistico 
# podemos gerar um histograma para visualizar a distribuição desses dados.

import pandas as pd
import seaborn as srn
import statistics  as sts

##      Criando DataFrame
# Fazendo a importação de um conjunto de Dados. PS - sep é um separador de ;
dataset = pd.read_csv("Churn.csv", sep=";")
# visulizando esses dados.
dataset.head()

#  Explorarando dados categoricos
# É necessário agrupar os estados, cada valor individual dos estados
# quais valores existem e qual a frequencias de cada um desses valores
# para isso eu crei uma variável que chamei de agrupado, é necessário 
# chamar o método groupby que é do dataFrame que foi criado, ou seja 
# aqui estamos agrupando pela coluna estado e calculando pelo tamanho.
agrupado = dataset.groupby(['Estado']).size()
agrupado
# Estado
# PR    257
# RP      1
# RS    478
# SC    258
# SP      4
# TD      1
# dtype: int64

# Note que na saída a cima conseguimos visualizar alguns problemas, o primeiro 
# é que tem estados que não existem como RP e TD, e outro problema é que tem 
# estados que estão fora do dominio ou seja não faz parte da regra de negócio 
# não é permitido que se tenha algum estado que não faz parte da região Sul.
# É necessário eliminar esses Estados pois são erros para nosso DataFrame.
# Se esses Dados são mantidos podem causar algum erro mais para frente na construção 
# do modelo ou seja o modelo pode aprender alguma coisa que não é verdade.
# Para Substituir esses Estados que estão errados utilizamos a regra da Moda.

#  Gráfico de Barras
# Visualizando em um Gráfico / Aqui temos uma outra forma de visualizar esses dados.
agrupado.plot.bar(color = 'gray')
# Essa saída vai gerar um gráfico de barras.


#  Agrupando pelo Gênero com o tamanho
agrupado = dataset.groupby(['Genero']).size()
agrupado
# Genero
# F              2
# Fem            1
# Feminino     461
# M              6
# Masculino    521
# dtype: int64

# Com essa saída podemos visualizar os dados do genero, Note que 
# temos alguns dados com F ou Fem ao invés de Feminino outros dados 
# estão com M no lugar de Masculina, esse é um problema bem comum 
# encontrado no tratamento de dados, uma mesma informação pode vim com 
# nomes diferentes, mas note que por exemplo diferente da análise dos 
# Estados F FEM e Feminino possuem dados corretos e são a mesma coisa 
# com isso não podemos excluir essas informações e subistiuir pela Moda que 
# nesse caso aqui é o Masculino que é o que mais se repete. Nesse caso aqui 
# é necessário unificar esses dados como F Fem e Femininino e M e Masculino.
# É necessário fazer isso por que esse problema também pode causar problemas na
# criação do Modelo.

# Visualizando esses mesmo dados de forma gráfica.
agrupado.plot.bar(color = 'gray')


#    Explorando colunas numéricas
# Utilizandoo a coluna Score, podemos encontrar problemas em variáveis numéricas 
# ou não podemos encontrar e está tudo ok, o Score é muito utilizado em instituições 
# Financeiras utilizam para avaliar o potencial de crédito do cliente. Utilizando o 
# Método describe ele irá retornar uma análise estatística desses dados, como média, quantidade, mediana e outros dados.
dataset['Score'].describe()
# count    999.000000
# mean     648.621622
# std       98.264219
# min      376.000000
# 25%      580.000000
# 50%      653.000000
# 75%      721.000000
# max      850.000000
# Name: Score, dtype: float64

# Analisando essa saída não notamos nenhum tipo de problema com esses dados a princípio.

# Visualizando esses dados com um gráfico 
srn.boxplot(dataset['Score']).set_title('Score')

# Essa saída vai retornar um gráfico de boxplot que podemos avaliar 
# vai mostrar que os dados aqui vão de 400 a 800, mediana e outros.

# Visualizando os mesmo Dados utilizando um Histograma
srn.distplot(dataset['Score']).set_title('Score')

# Analisando esse gráfico também podemos ver que está tudo normal indicando 
# que não existem problemas com esses dados. Até aqui não indicou que é necessário
# fazer algum tratamento com esses dados.


##   Analisando os Dados de Idade 
# Primeiramente fazemos uma descrição da coluna de idade.
dataset['Idade'].describe()
# count    999.000000
# mean      38.902903
# std       11.401912
# min      -20.000000
# 25%       32.000000
# 50%       37.000000
# 75%       44.000000
# max      140.000000
# Name: Idade, dtype: float64

# Note que ao aobservar essa saída podemos notar que existem algumas 
# coisas estranhas, note que o valor minimo é -20 e é notório que não 
# existe uma idade de -20, provavelmente isso é algum erro de cadastro 
# ou algum erro no processo de importação dos Dados. Note também que 
# o maior valor é 140 e não existe uma idade de 140 anos então também 
# é um erro.

# Gerando o BoxPlot desses dados
srn.boxplot(dataset['Idade']).set_title('Idade')

# Note que o BoxPlot Considera dois desvios padrões que são os pontos que 
# aparecem no Gráfico. É justamente onde tem esses erros. Note que são poucos 
# pontos de desvio padrão indicando que o problema não é generalizado e sim 
# em Pontos especificos.

# Gerando o Histograma desses Dados
srn.distplot(dataset['Idade']).set_title('Idade')

# Note que os Dados estão concentrados na média e na mediana, existe um 
# pequeno pico no zero, e dois pequenos picos no -25 e isso também indica 
# que o problema é em casos bem especificos e não algo generalizado.
# Na estapa de Tratamento desses dados será necessário resolver esse problema 
# com essas idade que estão fora do padrão.


## Analisando os Dados da Coluna Saldo 
dataset['Saldo'].describe()
# count    9.990000e+02
# mean     7.164928e+06
# std      6.311840e+06
# min      0.000000e+00
# 25%      0.000000e+00
# 50%      8.958835e+06
# 75%      1.258684e+07
# max      2.117743e+07
# Name: Saldo, dtype: float64

# Os saldos vão retornar valores muito altos e por isso estão em 
# formato de notação ciêntifica. Podemos notar através do min que 
# existe saldo com o valor 0, que o primeiro quartil também está 0
# isso indica que existe uma concentração dos Dados a cima do segundo 
# quartil, podemos visualizar isso melhor no gráfico.

# Gerando o BoxPlot desses Dados.
srn.boxplot(dataset['Saldo']).set_title('Saldo')

# Note que no gráfico o valume de saldos começa no 0, temos a mediana próxima a 1.0 
#  e o valor máximo em 2.0

# Gerando o Histograma desses Dados.
srn.distplot(dataset['Saldo']).set_title('Saldo')

# Note que no gráfico os dados parecem está concentrado proximos a média 
# porém o gráfico indica também que existe um grande pico no zero. Isso 
# indica que tem muitas pessoas com o saldo 0 na conta.
# É importante ressaltar que não existem motivos para retirar esses dados pois 
# são dados corretos e estão dentro das regras de negócios. Por isso não devo 
# mexer nesses dados, só seria necessário mexer se fossem dados incorretos.


## Analisando os Dados da Coluna Salário 
dataset['Salario'].describe()
# count    9.920000e+02
# mean     3.528762e+07
# std      5.305800e+08
# min      9.677000e+03
# 25%      3.029011e+06
# 50%      8.703250e+06
# 75%      1.405213e+07
# max      1.193469e+10
# Name: Salario, dtype: float64

# Note que na saída desses dados existe uma distancia maior entre a mediana e a media 
# indicando que existe alguma desregularidade nesses dados porém não significativa.

# Gerando o BoxPlot desses Dados
srn.boxplot(dataset['Salario']).set_title('Salario')

# analisando o Gráfico note que existe uma grande concentração no 0
# isso deforma o BoxPlot, existem pontos também que ele considera 
# valores muito altos. Note que isso são altlines(Erros). Sendo erros 
# ou não isso pode prejudicar o modelo, por isso podemos remover esses dados 
# e atribuir a mediana.

# Gerando um gráfico de Histograma desses Dados.
srn.distplot(dataset['Salario']).set_title('Salario')

# Note na saída do gráfico que existe uma distorção no zero 
# isso pode indicar que os clientes não informaram os salários.
# Isso está distorcendo o gráfico fazendo com que não visualizemos 
# os outros salários.


## Verificando no DataFrame se existem valores NAN
#contamos valores NAN
#genero e salário
dataset.isnull().sum()
# Id                0
# Score             0
# Estado            0
# Genero            8
# Idade             0
# Patrimonio        0
# Saldo             0
# Produtos          0
# TemCartCredito    0
# Ativo             0
# Salario           7
# Saiu              0
# dtype: int64

# Valores NAN acontecem quando a informação não foi preenchida 
# isso tem que ser tratado para a criação do modelo.
# Essa saída vai mostrar um resumo onde existem a ocorencia de NAN 
# nas colunas que não tem ele mostra 0
# Note nessa saída que existem 8 na coluna de Genero e 7 na coluna de Salario
# Esse é mais um problema que precisa ser tratado e resolvido. Esses valores 
# precisam ser removidos.