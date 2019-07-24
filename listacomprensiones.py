''''''''''''''''''''''' This is an Example developed to learn different
python applications such as libraries built in functions, etc.
It's important to follow the steps but also to be capable to implement this
examples within real time applications. In particular, this tutorial will take
information from python for engineers and the introduction of numpy and matplotlib
examples.
'''''''''''''''''''''''
# Start for importing the libraries that are required for the development of your codes.
import numpy as np
# Declare a variable called x with the following values
x = [5,10,15,20,25]
# Create another variable called y with an empty (Open) value.
y = []
# y will contain the values of x divided by 5
for counter in x:
    y.append(counter / 5)
    print("\nOld Fashion Way: x = {} y = {} \n".format(x,y))
'''''''''' The above results will provide a list of different results displaying the
calculations performed in a chain. This could be simplify by using a list of comprehensions
which it is the below code provided.
'''''''''''''''''''''
# Let's create a variable called z that will emcompass the following code
# Declare a variable called x with the following values
x = [5,10,15,20,25]
z = [n/5 for n in x]
print("List Comprehensions: x ={} z = {} \n".format(x,z))
# As is can be seen by just using a simpler code we also acquire a much more resumed answer speeding the process.
x = [5,10,15,20,25]
z = [n/5 for n in x]
print("List Comprehensions: x ={} z = {} \n".format(x,z))
try:
    a = x / 5
except:
    print("No, This operation cannot be performed\nYou cant do that with python libraries")
# So let's try this one to see what are the results acquired by using a numpy array
a = np.array(x)
b = a / 5
print("With Numpy: a = {} b = {} \n".format(a,b))
# This block is working an finished.





