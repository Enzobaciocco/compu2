import numpy as np
import matplotlib.pyplot as plt 
x = np.array([0.1, 1.0, np.pi/3])

x1 = 0.1
x2 = 1.0
x3 = np.pi/3

h =  np.geomspace(1, 1e-20,300)
eps= 2e-52 # tiene que ver con el valor minimo

def f(x):
    return np.sqrt(x)


def deriv2(f,x,h): 
    return (f(x+h)-2*f(x)+f(x-h))/h**2

          
def graf(f,x,h):
    valorreal = 1/4*x**(-3/2) #segunda derivada analitica
    valorformula = deriv2(f,x,h)
    
    error_an = 0.5*h*np.abs(np.sqrt(x))+2*eps*np.abs(np.sqrt(x))
    error_num = np.abs(valorreal-valorformula)
   
    b         = np.argmin(error_num)#donde esta el valor minimo 
    c         = (h[b])
    print(c)
    
    plt.scatter(h,error_num)
    plt.plot(h,error_an)
    
graf(f,x1,h)
graf(f,x2,h)
graf(f,x3,h)