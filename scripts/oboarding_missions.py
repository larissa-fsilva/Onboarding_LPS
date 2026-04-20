import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker  

def printDataframe(dataframe):
    df = pd.read_csv(dataframe)
    print(df)

def getRing(data,n_ring):
    ring = []
    pos = 0
    l_data = len(data)

    while pos < l_data:
        line =  [float(item.strip()) for item in data[pos].strip("[]").split(",")]
        value = line[n_ring]
        ring.append(value)
        pos += 1
    return ring

def plotHistogram(variable,n_ring,dataframe):
    df = pd.read_csv(dataframe)
    if variable == 'et':
        data= df['TrigEMClusterContainer.et']
    elif variable == 'eta':
        data= df['TrigEMClusterContainer.eta']
    elif variable == 'phi':
        data = df['TrigEMClusterContainer.phi']
    elif variable == 'avgmu':
        data = df['EventInfoContainer.avgmu']
    elif variable == 'energy':
        data = df['TrigEMClusterContainer.ringsE'].tolist()
        ring = getRing(data,n_ring)

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
    elif variable == 'energy':
        plt.hist(ring, bins=100 ,color = 'lightblue', edgecolor = 'black') 
        plt.xlabel(r'Energy')
        plt.xlim(0,10000)
        plt.title(r'Distribuição de Energia')
    plt.ylabel('frequency')
    plt.show()

def plotBoxplot(dataset,n_rings):
    n = 0
    data = []
    while n < n_rings:
        data += [getRing(dataset,n)]
        n += 1

    outliers_style = dict(marker='.', markersize=2, markerfacecolor='black', markeredgecolor='none')

    bp = plt.boxplot(data, labels  = [f"Ring {i}" for i in range(len(data))],patch_artist=True,notch=False,flierprops=outliers_style)

    for box in bp['boxes']:
        box.set(facecolor='blue', color='lightblue') 

    plt.xticks(rotation=90, fontsize=8) 
    plt.yscale('symlog') 
    plt.ylim(-100000, 100000) 

    plt.margins(x=0.1)

    plt.xticks(rotation=90, fontsize=8)
    plt.title('All Rings Boxplot')
    plt.ylabel('Values')
    plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.show()
