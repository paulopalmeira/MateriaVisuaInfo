# Para este exemplo, vamos usar a biblioteca pandas, que oferece
# métodos práticos de leitura de arquivos. No caso, vamos usar o método
# read_csv para ler o dataset contido no arquivo USD_BRL_hist.csv.

from pandas import read_csv
import matplotlib.pyplot as plt

df = read_csv("USD_BRL_hist.csv", header=0, index_col=0, parse_dates=True)

plt.plot(df)
plt.show()
