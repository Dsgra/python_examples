import matplotlib.pyplot as plt

x = [4, 3, 6, 7, 8]
y = [2, 8, 9, 6, 3]

x1 = [9, 3, 10, 4, 8]
y1 = [3, 9, 2, 5, 7]

plt.bar(x, y, label='Bars1', color='r')
plt.bar(x1, y1, label='Bars2', color='y')

plt.xlabel('x')
plt.ylabel('y')
plt.title('That Is A New Graph\nWe had just Created')
plt.legend()
plt.show()

'''

'''
import matplotlib.pyplot as plt

population_ages = [11, 20, 15, 30, 40, 15, 28, 30, 45, 105, 47, 89, 42, 10, 9, 119, 110,
     18, 16, 21, 23, 43, 100, 72, 69]

# In this case instead of getting ids bins are going to be used,
# Bins are like bucket where the data is putted into. Second Example.

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph Using Bins\nBest to Simplify the Code')
plt.legend()
plt.show()

'''

'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x, y, label='skitscat', color='k')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph Created Using\nTheScatter Function')
plt.legend()
plt.show()

'''

'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x, y, label='skitscat', color= 'k', s=500, marker="*")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Another Graph Using\nThe Scatter Function')
plt.legend()
plt.show()

'''

'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x, y, label='skitscat', color='k', s=1000)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph Created Using\nTheScatter Function')
plt.legend()
plt.show()

'''

'''


