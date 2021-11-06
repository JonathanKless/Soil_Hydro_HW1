"""
@author: Jonathan Kless
Homework Assignment No.1 part 2 (Lecture Notes 2; Ex 9.3)
"""
import numpy as np
from matplotlib import pyplot as plt

csfont = {'fontname':'Comic Sans MS'}

"""
Exercise 9.3
"""

#values for matric potential are given as a range (-0.1, -15000) [cm] 
h = np.linspace(-0.1, -15000, 100)

#hydraulic parameters are given as such (lecture notes 2, p.35)
#and formatted as [Sand, Loam, Clay]
theta_s = [0.43, 0.44, 0.43]
theta_r = [0.04, 0.07, 0.09]
alpha = [0.14, 0.016, 0.008]
n = [2.56, 1.56, 1.4]
m = [1-1/value for value in n]


# Van Genuchten Equation, solved for volumetric Soil water content [cm3/cm3]
theta = lambda i: theta_r[i]+(theta_s[i]-theta_r[i])/((1+(alpha[i]*np.absolute(h))**n[i])**m[i])

if np.any(h>=0): 
    theta[h>=0]=theta_s

#plotting volumetric Soil water content for given soil textures [Sand, Loam, Clay]
plt.figure("Exercise 3")
plt.semilogy(theta(0), np.absolute(h), label="Sand", color="r")
plt.semilogy(theta(1), np.absolute(h), label="Loam", color="g")
plt.semilogy(theta(2), np.absolute(h), label="Clay", color="b")
plt.xlabel("SWC [cm3/cm3]", **csfont)
plt.ylabel("Matric potential [cm]", **csfont)
plt.title("Exercise 3", **csfont)
plt.legend(loc="best", fancybox=True)
plt.grid()

#saving the plot to current directory
plt.savefig(fname="Exercise_3.png", dpi=200, format="png")