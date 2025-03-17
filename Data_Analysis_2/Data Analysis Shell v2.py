#import numpy to handle arrays
import numpy as np

#import matplotlib to create plots
import matplotlib.pyplot as plt

#allows for curve fitting
import scipy.optimize as opt;

#import data. assumes comments are # are data is separated by white space
#the unpack is required to read in vertical data arrayss

xdata,ydata, yerror = np.loadtxt('tempdata.txt' ,unpack=True)



#the function we are fitting, called func

def func(x,s,b):
     return s*x+b


#fit the data
#The sigma = means you will be doing a fit weighted by the uncertainty in y
parameters, covariance = opt.curve_fit(func, xdata, ydata,sigma = yerror)

#Plots the data.  You can play around with the paramters of the plot to change color, shape, etc
#You will likely want to give it a better name than 'data' and will want to change colors, etc
# when you have multiple fits ont he same page
plt.errorbar(xdata,ydata,yerr=yerror,capsize = 5,marker = 'o',linestyle = 'None', label = 'temp')

#Plots the fit
plt.plot(xdata,func(xdata,*parameters),label = 'fit')

#insert the legend
plt.legend(loc = 'upper left')


#This prints the fitting parameter
print(f"Fitting Parameters: s = {parameters[0]}, b = {parameters[1]}")

#calculate the error on the fits from the covariacne matrix
perr = np.sqrt(np.diag(covariance))

#Print the erros on the fits


print(f"Error: s = {perr[0]}, b = {perr[1]}")

#print(covariance)


#plt.yscale('log')
#plt.yscale('linear') 

chi_squared = np.sum((func(xdata, *parameters) - ydata)**2/yerror**2)
red_chi_squared = chi_squared/(np.size(ydata)-np.size(parameters))

print("Chi Squared:",chi_squared)
print("Reduced Chi Squared:",red_chi_squared)



#axes titles
plt.xlabel('Time (s)', fontsize = 16)
plt.ylabel('Temp. (C)', fontsize = 16)

plt.title('Temperature Data', fontsize = 18)


#Show the plot!
#plt.show()

