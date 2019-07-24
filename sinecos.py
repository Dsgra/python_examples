import numpy as np
import matplotlib.pyplot as plt
# Variable x espaciados desde 0 a 20
x = np.linspace(0,20,100)
y1 = np.sin(x)
y2 = np.cos(x)
# Plot funciones sin and cos 
plt.plot(x, y1, "-g", label="sine")
plt.plot(x, y2, "-b", label="cos")
# Insertar leyenda 
plt.legend(loc="upper right")
# Limite de y axis
plt.ylim(-1.5, 1.5)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

salary = np.fromfile("salaries.txt", dtype=int, sep=",")
names = np.genfromtxt("names.txt", dtype='str', delimiter=",")

x = np.arrange(len(names))

plt.bar(x, salary)
plt.xticks(x, names)

plt.xlabel("Names")
plt.ylabel("Salaries")
plt.title("SalRandom")
plt.show()

print(np.max(salary), np.min(salary), np.average(salary), np.mediam(salary))


