#------------------------------------------
# Fitting experimental data using a Voigt
# function with a given gamma; the 
# Gaussian parameter alpha is optimized
#------------------------------------------
def func (x, alpha):
    v1 = voigt(gamma, alpha, peak1_pos)
    v2 = voigt(gamma, alpha, peak2_pos)
    vtot = int1 * v1.at(x) + int2 * v2.at(x) + shift * np.ones(len(xdata))
    return vtot

def func_2 (x, alpha, i1, i2):
    v1 = voigt(gamma, alpha, peak1_pos)
    v2 = voigt(gamma, alpha, peak2_pos)
    vtot = i1 * v1.at(x) + i2 * v2.at(x) + shift * np.ones(len(xdata))
    return vtot

#------------------------------------------
# MAIN
#------------------------------------------


    import sys
    import numpy as np 
    import scipy.optimize as optimization
    from voigt import *
    import matplotlib.pyplot as plt
    from input import *


    ifile = open(data_file, 'r')
    lns = ifile.readlines()
    ifile.close()

    lns = lns[2:]

    xdata = []
    ydata = []

    for i in range(len(lns)):
        xdata.append(float(lns[i].split()[0]))
        ydata.append(float(lns[i].split()[1]))

    # Initial guess
    x0 = 1.0

    # Data errors 
    sigma = np.ones(len(xdata))

    popt, pcov = optimization.curve_fit(func, xdata, ydata, x0, sigma)

    alpha = popt[0]
    stdev = np.sqrt(np.diag(pcov))

    v1 = voigt(gamma, alpha, peak1_pos)
    v2 = voigt(gamma, alpha, peak2_pos)

    v1_x = int1 * v1.at(xdata) + shift * np.ones(len(xdata))
    v2_x = int2 * v2.at(xdata) + shift * np.ones(len(xdata))


    plt.plot (xdata, ydata, label="experiment")
    plt.plot (xdata, func(xdata, alpha), label="alpha = %4.2f, stdev = %5.4f" % (alpha, stdev))
    plt.plot (xdata, v1_x, label="en = %6.2f, int = %5.3f" % (peak1_pos, int1))
    plt.plot (xdata, v2_x, label="en = %6.2f, int = %5.3f" % (peak2_pos, int2))
    plt.legend()
    plt.savefig("%s_fit_p1_%6.2f_i1_%5.3f_p2_%6.2f_i2_%5.3f.png" % (mol,peak1_pos, int1, peak2_pos, int2))
    plt.gcf().clear()

    # Initial guess
    x0 = [1.0, int1, int2]

    # Data errors 
    sigma = np.ones(len(xdata))

    popt, pcov = optimization.curve_fit(func_2, xdata, ydata, x0, sigma)

    print popt

    alpha = popt[0]
    i1 = popt[1]
    i2 = popt[2]
    stdev = np.sqrt(np.diag(pcov))

    print alpha
    print i1
    print i2
    print stdev

    v1 = voigt(gamma, alpha, peak1_pos)
    v2 = voigt(gamma, alpha, peak2_pos)

    v1_x = i1 * v1.at(xdata) + shift * np.ones(len(xdata))
    v2_x = i2 * v2.at(xdata) + shift * np.ones(len(xdata))


    plt.plot (xdata, ydata, label="experiment")
    plt.plot (xdata, func_2(xdata, alpha, i1, i2), label="alpha = %4.2f, stdev = %5.4f" % (alpha, np.sum(stdev)/3))
    plt.plot (xdata, v1_x, label="en = %6.2f, int = %5.3f" % (peak1_pos, i1))
    plt.plot (xdata, v2_x, label="en = %6.2f, int = %5.3f" % (peak2_pos, i2))
    plt.legend()
    plt.savefig("%s_fit_p1_%6.2f_i1_%5.3f_p2_%6.2f_i2_%5.3f.png" % (mol, peak1_pos, i1, peak2_pos, i2))
