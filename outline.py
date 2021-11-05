# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 15:34:21 2021

@author: Jonat
"""

import numpy as np
import matplotlib.pyplot as plt


# plots / stylings
# plt.xlabel()
# plt.ylabel()
# plt.legend() #no arguments 
# plt.title()
# plt.grid(True)
# plt.styles.use()
# plt.tight_layout()
# plt.savefig("C:\Path\")

#Format strings
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
#use hex values for color color="#4444"
#use linewidth= 

# plt.plot(same x axis, use label= argument)



#Exercise 1

#create 2 arrays using given data

# h= np.array()

#or create 2 lists first, then convert to array like

# h_values= [-1,-2,-3]
# h= np.array(np.abs(h_values))

#plot, modify font, and save with specified size/resolution

# csfont = {'fontname':'Comic Sans MS'}
# hfont = {'fontname':'Helvetica'}

# plt.title('title',**csfont)
# plt.xlabel('xlabel', **hfont)
# plt.savefig(fname="test_plt.png", dpi=200, format="png", figsize=(10,10))



#Exercise 2 

#plot y-axis (SWC) in logarithmic scale

#plt.plot => plt.semilogy()


#Exercise 3

#plot VGE for theta(h)
#x-axis = matric potential [cm]
#y-axis = theta(h) [m**3*(m**(-3))]
#include if clause for theta(h)>= 0
# if np.any(h>=0): 
#     Theta[h>=0]=Theta_s

#plot for 3 given soil types in the same figure, stylise individually


#Exercise 4

#plot VGME for K(h, theta(h))
#x-axis = matric potential [cm]
#y-axis = K(h, theta(h)) [cm/s]
#include if clause for theta(h)>= 0
# if np.any(h>=0): 
#     Theta[h>=0]=Theta_s

#plot each curve in seperate subplot!
















