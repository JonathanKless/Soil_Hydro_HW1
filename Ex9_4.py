"""
@author: Jonathan Kless
Homework Assignment No.1 part 2 (Lecture Notes 2; Ex 9.4)
"""
import numpy as np
from matplotlib import pyplot as plt

csfont = {'fontname':'Comic Sans MS'}

"""
Exercise 9.4
"""

#values for matric potential are given as a range (-0.1, -15000) [cm] 
h = np.linspace(-0.1, -1500, 100)

#hydraulic parameters are given as such (lecture notes 2, p.35)
#and formatted as [Sand, Loam, Clay]
theta_s = [0.43, 0.44, 0.43]
theta_r = [0.04, 0.07, 0.09]
alpha = [0.14, 0.016, 0.008]
n = [2.56, 1.56, 1.4]
m = [1-1/value for value in n]
Ksat = [0.008, 0.002, 5*10**-5]
lambda_k = [0.5, 0.5, 0.5]

#deriving theta(h) by VGE 
theta = lambda i: theta_r[i]+(theta_s[i]-theta_r[i])/((1+(alpha[i]*np.absolute(h))**n[i])**m[i])

if np.any(h>=0): 
    theta[h>=0]=theta_s

#calculating Saturation degree from derived theta(h)
Theta = lambda i: (theta(i)-theta_r[i])/(theta_s[i]-theta_r[i])

#deriving K(h) by van-Genuchten-Mualem equation
K = lambda i: Ksat[i]*(Theta(i)**lambda_k[i])*(1-(1-Theta(i)**(1/m[i]))**m[i])**2

if np.any(h>=0): 
    K[h>=0]=Ksat
    
#plotting K(h) for given soil types, in seperate subplots
plt.figure("Exercise 9.4")


fig, axs = plt.subplots(3, figsize=(4,12))
fig.suptitle('Exercise 4', fontsize=15, x=0)
fig.tight_layout(h_pad=4)
axs[0].loglog(np.absolute(h), K(0), label="Sand", color="r")
axs[0].set_title("Sand")
axs[0].grid()
axs[1].loglog(np.absolute(h), K(1), label="Loam", color="b")
axs[1].set_title("Loam")
axs[1].grid()
axs[2].loglog(np.absolute(h), K(2), label="Clay", color="g")
axs[2].set_title("Clay")
axs[2].grid()

for ax in axs.flat:
    ax.set(xlabel='Matric potential [cm]', ylabel='Hydraulic conductivity [cm/s]')

#saving the plot to current directory
plt.savefig(fname="Exercise_4.png", dpi=200, format="png", bbox_inches='tight')









