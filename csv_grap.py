import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('example.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter= ',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[0]))

plt.plot(x, y, label='Loading From File!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('This Graph Loads\nThe Data Form File')
plt.legend()
plt.show()

'''
Contenido del archivo csv
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,

'''