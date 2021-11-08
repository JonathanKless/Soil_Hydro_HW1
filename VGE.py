import numpy as np
from matplotlib import pyplot as plt
csfont = {'fontname':'Comic Sans MS'}

h = np.linspace(-0.1, -15000, 100)
theta_s1 = [0.43, 0.44, 0.43]
theta_r1 = [0.04, 0.07, 0.09]
alpha1 = [0.14, 0.016, 0.008]
n1 = [2.56, 1.56, 1.4]
m1 = [1-1/value for value in n1]

Dic = {"theta_s": theta_s1, "theta_r": theta_r1, "alpha": alpha1, "n": n1, "m": m1}


def VGE(Dic,i):
    theta_s = Dic["theta_s"][i]
    theta_r = Dic["theta_r"][i]
    alpha = Dic["alpha"][i]
    n = Dic["n"][i]
    m = Dic["m"][i]
    
    # print(theta_s)
    # print(theta_r)
    # print(alpha)
    # print(n)
    # print(m)
    # print(h)
    
    theta = theta_r[i]+(theta_s[i]-theta_r[i])/((1+(alpha[i]*np.absolute(h))**n[i])**m[i])
    figure_title = "Data for //file name, row:" + str(i)
    plt.figure(figure_title)
    plt.semilogy(theta, np.absolute(h), label="Derived Values")
    plt.xlabel("SWC [cm3/cm3]", **csfont)
    plt.ylabel("Matric potential [cm]", **csfont)
    plt.title(figure_title, **csfont)
    plt.legend(loc="best", fancybox=True)
    plt.grid()
    plt.show()
    

