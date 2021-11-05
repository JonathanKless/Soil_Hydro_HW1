"""
@author: Jonathan Kless
Homework Assignment No.1 part 1 (Lecture Notes 2; Ex 9.1-9.2)
"""
import numpy as np
from matplotlib import pyplot as plt

csfont = {'fontname':'Comic Sans MS'}

#example values for matric potential [cm] 
h = np.array([-1, -10, -60, -100, -300, -1000, -3000, -15000])

#example values for volumetric Soil water content [cm3/cm3]
theta = np.array([0.43, 0.40, 0.31, 0.25, 0.19, 0.09, 0.07, 0.06])

"""
Exercise 9.1
"""

#creating the plot
plt.figure("Exercise 1")
plt.plot(theta, np.absolute(h), label="Measured Values")
plt.xlabel("SWC [cm3/cm3]", **csfont)
plt.ylabel("Matric potential [cm]", **csfont)
plt.title("Exercise 1", **csfont)
plt.legend(loc="best", fancybox=True)
plt.grid()
plt.show()

#saving the plot to current directory
#plt.savefig(fname="Exercise_1.png", dpi=200, format="png", figsize=(20,20))

"""
Exercise 9.2
"""

#plotting the values in a better visualisation
plt.figure("Exercise 1")
plt.semilogy(theta, np.absolute(h), label="Measured Values")
plt.xlabel("SWC [cm3/cm3]", **csfont)
plt.ylabel("Matric potential [cm]", **csfont)
plt.title("Exercise 1", **csfont)
plt.legend(loc="best", fancybox=True)
plt.grid()
plt.show()