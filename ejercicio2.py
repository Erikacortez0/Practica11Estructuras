import pandas as pd
import matplotlib.pyplot as plt

estudiante1 = ['rafael', 8, 5]
estudiante2 = ['michelle', 7, 3]

lista_puntajes = [estudiante1, estudiante2]

puntaje = pd.DataFrame(lista_puntajes, columns=['nombre', 'nota1','relacion'])
puntaje
relacionPuntaje = puntaje.sort_values('estudiante1', ascending=False)
plt.scatter(relacionPuntaje['nombre'], relacionPuntaje['estudiante1'], color = ['r', 'b'])
plt.title('Datos Puntajes')

plt.show()