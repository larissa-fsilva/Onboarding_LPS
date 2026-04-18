import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def printDataframe(dataframe):
    df = pd.read_csv(dataframe)
    print(df)

def plotHistogram(variable,dataframe):
    df = pd.read_csv(dataframe)
    if variable == 'et':
        data= df['TrigEMClusterContainer.et']
    elif variable == 'eta':
        data= df['TrigEMClusterContainer.eta']
    elif variable == 'phi':
        data = df['TrigEMClusterContainer.phi']
    elif variable == 'avgmu':
        data = df['EventInfoContainer.avgmu']
    
    if variable == 'et':
        plt.hist(data, bins=50 ,color = 'lightblue', edgecolor = 'black') 
        plt.xlabel(r'$E_T$')
        plt.title(r'Distribuição de $E_T$')
    elif variable == 'eta':
        plt.hist(data, bins=50 ,color = 'lightblue', edgecolor = 'black') 
        plt.xlabel(r'$\eta$')
        plt.title(r'Distribuição de $\eta$')
    elif variable == 'phi':
        plt.hist(data, bins=50 ,color = 'lightblue', edgecolor = 'black') 
        plt.xlabel(r'$\phi$')
        plt.title(r'Distribuição de $\phi$')
    elif variable == 'avgmu':
        plt.hist(data, bins=100 ,color = 'lightblue', edgecolor = 'black') 
        plt.xlabel(r'$avg(\mu)$')
        plt.title(r'Distribuição de $avg(\mu)$')
    plt.ylabel('frequency')
    plt.show()

print(plotHistogram('et','subset.csv'))
print(plotHistogram('eta','subset.csv'))
print(plotHistogram('phi','subset.csv'))
print(plotHistogram('avgmu','subset.csv'))