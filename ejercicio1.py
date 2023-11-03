import pandas as pd
import matplotlib.pyplot as plt

jugueteria = ['peluche', 240, 2.40]
electrodomesticos = ['cocina', 500, 3.50]
muebles= ['estante', 1000, 200.00]
ropa = ['chaqueta', 3500, 30.20]
cosmeticos = ['labial', 340, 20.00]

lista_ventas = [jugueteria, electrodomesticos, muebles, ropa, cosmeticos]

ventas = pd.DataFrame(lista_ventas, columns=['nombre', 'cantidad', 'precio'])
ventas
ventas_mensuales = ventas.sort_values('cantidad', ascending=False)
plt.bar(ventas_mensuales['nombre'], ventas_mensuales['cantidad'], color = ['r', 'b', 'r'])
plt.title('Ventas Mensuales')
plt.ylabel('cantidad')
plt.show()