#squares = [1, 4, 9, 16, 25]
#print(squares)
#print(squares[0])
#print(squares[1])
#print(squares[2])
#print(squares[3])
#print(squares[4])
#print(squares[:])
#print(squares + [36, 49, 64, 81, 100])
#cubes = [1, 8, 27, 65, 125]
#print(cubes[3])
#cubes.append(216)
#cubes.append(7 ** 3)
#print(cubes)
#letters =['a', 'b', 'c', 'd', 'e', 'f', 'g']
#print(letters)
#letters[2:5] = ['C', 'D', 'E']
#print(letters)
#letters[2:5] = []
#print(letters)
#letters[:] = []
#print(letters)
#letters =['a', 'b', 'c', 'd']
#print(len(letters))
# Exchanging values
#a=int(input("Enter the first variable:"))
#b=int(input("Enter the second variable:"))
#a=a+b
#b=a-b
#a=a-b
#print("a is:",a,"b is:",b)
#n=int(input("Enter a number n:"))
#temp=str(n)
#t1=temp+temp
#t2=temp+temp+temp
#comp=n+int(t1)+int(t2)
#print("The value is:", comp)
n=int(input("Enter a number:"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:", rev)

