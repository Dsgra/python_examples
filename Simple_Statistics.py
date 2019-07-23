import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]

trabajo= [7, 3, 4, 11, 7]
comida= [2, 3, 4, 3, 2]
descanso = [7, 8, 7, 2, 2]
juego = [8, 5, 7, 3, 1]

slices = [6, 2, 2, 13]

actividades = ['trabajo', 'comida', 'descanso', 'juego']
colum= ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=actividades,
        colors=colum,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Representaciones\nUtilizando la funcion PIE')
plt.legend()
plt.show()