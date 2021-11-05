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
h = np.linspace(-0.1, -1500, 100)

#hydraulic parameters are given as such (lecture notes 2, p.35)
#Formated as [Sand, Loam, Clay]
theta_s = [0.43, 0.44, 0.43]
theta_r = [0.04, 0.07, 0.09]
alpha = [0.14, 0.016, 0.008]
n = [2.56, 1.56, 1.4]
m = [1-1/value for value in n]


# Van Genuchten Equation, solved for volumetric Soil water content [cm3/cm3]
theta = lambda i: theta_r[i]+(theta_s[i]-theta_r[i])/((1+(alpha[i]*np.absolute(h))**n[i])**m[i])

if np.any(h>=0): 
    theta[h>=0]=theta_s

