from scipy.optimize import curve_fit
import numpy as np
import pickle

with(open('mixture1.dat', "rb")) as OF:
    fileData = pickle.Unpickler(OF).load()
mixture1=np.array(fileData, dtype='float')
with(open('mixture2.dat', "rb")) as OF:
    fileData = pickle.Unpickler(OF).load()
mixture2=np.array(fileData, dtype='float')
with(open('mixture3.dat', "rb")) as OF:
    fileData = pickle.Unpickler(OF).load()
mixture3=np.array(fileData, dtype='float')
with(open('mixture4.dat', "rb")) as OF:
    fileData = pickle.Unpickler(OF).load()
mixture4=np.array(fileData, dtype='float')

def findFluorescense(time, lifetime, ampl):
    return ampl*np.exp(-time/lifetime)

yRange = np.arange(0, pow(10, (-6)), pow(10, (-10)))
molecules=[
	['Naphtalene', 200.9e-9],
	['Anthracene', 5.8e-9], 
	['Benzopyrene', 38.6e-9],
	['Pyrene', 516.2e-9],
	['Chrysene', 57.8e-9],
	['Benzofluoranthene', 8.9e-9]
]

def findFluorescenseSum(time, ampl1, ampl2, ampl3, ampl4, ampl5, ampl6):
    sum = 0
    sum += findFluorescense(time, molecules[0][1], ampl1)
    sum += findFluorescense(time, molecules[1][1], ampl2)
    sum += findFluorescense(time, molecules[2][1], ampl3)
    sum += findFluorescense(time, molecules[3][1], ampl4)
    sum += findFluorescense(time, molecules[4][1], ampl5)
    sum += findFluorescense(time, molecules[5][1], ampl6)
    return sum

def myCurveFit(time, ampl1, ampl2, ampl3, ampl4, ampl5, ampl6):
    return findFluorescenseSum(time, ampl1, ampl2, ampl3, ampl4, ampl5, ampl6)

popt1, pcov1 = curve_fit(myCurveFit, yRange, mixture1)
popt2, pcov2 = curve_fit(myCurveFit, yRange, mixture2)
popt3, pcov3 = curve_fit(myCurveFit, yRange, mixture3)
popt4, pcov4 = curve_fit(myCurveFit, yRange, mixture4)

print("\nIn the first mixture:")
for i,popt in enumerate(popt1):
    print(f'\t{molecules[i][0]} - {round(popt, 2)}')
print("\nIn the second mixture:")
for i,popt in enumerate(popt2):
    print(f'\t{molecules[i][0]} - {round(popt, 2)}')
print("\nIn the third mixture:")
for i,popt in enumerate(popt3):
    print(f'\t{molecules[i][0]} - {round(popt, 2)}')
print("\nIn the fourth mixture:")
for i,popt in enumerate(popt4):
    print(f'\t{molecules[i][0]} - {round(popt, 2)}')