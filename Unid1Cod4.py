# A visualização do Unid1Cod3.py ficou cheio de informações. 
# Com menos categorias mostra-se mais adequada (embora, sem 
# os rótulos de dados, ficaria difícil distinguir entre as 
# categorias Fundamental e Superior). Portanto, o código modificado:

import matplotlib.pyplot as plt

labels = 'Nenhum','Fundamental','Médio','Superior'
sizes = [86026, 28525, 57394, 25286]
colors = [ 'lightgray', 'orange', 'coral', 'red']
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90)

plt.legend(patches, labels, loc="lower right")
plt.axis('equal')
plt.show()