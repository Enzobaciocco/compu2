
import numpy as np
import matplotlib.pyplot as plt 
x = np.array([0.1, 1, np.pi/3]),
def f(x):
    return np.sqrt(x)
def deriv2(f,x,h): 
    return (f(x+h)-2*f(x)+f(x-h))/h**2
df   = (1/2)*x**(-1/2)#primera derivada analitica
valorreal = 1/4*x**(-3/2) #segunda derivada analitica
h =  np.geomspace(1, 1e-20,300) # 300 valores para h 
eps= 2e-52 # tiene que ver con el valor minimo que puede guardar un computador 

error_an = 0.5*h*np.abs(np.sqrt(x))+2*eps*np.abs(np.sqrt(x))
valordelaformula = deriv2(f,x,h)
error_num = np.abs(valorreal-valordelaformula)
#np.argmin(error_num)#donde esta el valor minimo 

plt.plot(error_an,error_num)

