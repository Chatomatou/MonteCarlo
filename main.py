from math import *
import sys 
import random 

try: 
    import matplotlib.pyplot as plt
except:
    print("-> Please install matplotlib with : pip install matplotlib")

# function 
x = []
y = []

# point 
px = []
py = []



def generate_point_in_interval(a, b):
    return [random.uniform(a, b), random.uniform(a, abs(a*a))]

def under_the_curve(point):
    return point[1] <= f(point[0]) and point[1] > 0

def generation(n, a, b):
    count = 0
    for i in range(n):
        point = generate_point_in_interval(a, b)
        if under_the_curve(point):
            px.append(point[0])
            py.append(point[1])
            count += 1
    return count


function = input("[+] Enter the the function x:->f(x) : ")

try:
    f = lambda x : eval(function)
    
    while True:
        try:
            a = int(input("Enter the interval a : "))
            b = int(input("Enter the interval b : "))
            n = int(input("Enter the maximum generation n : "))
        except:
            print("Please : enter a number !")
        else:
            break
except SyntaxError:
    print("Error : Please enter a function like python used in source code !")
    sys.exit()

axisX = []
axisY = []

for i in range(a-10, b+10):
    x.append(i)
    y.append(f(i))
    
    axisX.append(i)
    axisY.append(0);
    
 


print(generation(n, a , b))
plt.title("Monte-Carlo Method")
plt.xlim(a-5, b+5)
plt.scatter(px, py, c="green", s=0.1, alpha=0.5)
plt.plot(x, y, c="black")
plt.plot(axisX, axisY, c="red")

plt.show()
 
 




