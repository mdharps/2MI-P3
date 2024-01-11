import pandas as pd
import scipy.stats as stats
import numpy as np

#std = [0.0009597805444550236,0.07967685467782024,0.561138544011668]#The assumed standard deviations of Diameter Weight and IV respectively.

def KendalsTau(x,y):#Testing for correlation, which indicates systematic change
    try:
        res = stats.kendalltau(x, y)
        return [res.correlation,res.pvalue]
    except:
        return [float('nan'),float('nan')]

def Spearmansr(x,y):#Testing for correlation, which indicates systematic change
    try:
        res = stats.spearmanr(x, y)
        return [res.correlation,res.pvalue]
    except:
        return [float('nan'),float('nan')]

def Zscore(x,field):#Returns zscore of most recent year's data
    stds = [0.0009597805444550236,0.07967685467782024,0.561138544011668]#The assumed standard deviations of Diameter Weight and IV respectively.
    #x = x[np.logical_not(np.isnan(x))]
    if field == 'Diameter':
        std = stds[0]
    if field == 'Weight':
        std = stds[1]
    if field == 'IV':
        std = stds[2]
        
    z = (x[-1]-np.mean(x[0:-1]))/std
    return [z,stats.norm.sf(abs(z))*2]



df = pd.DataFrame(columns=['file','N','Kendall Tau Diameter Correlation', 'Kendall Tau Diameter Pvalue','SRCC Diameter','SRCC Diameter Pvalue','Zscore of latest sample Diameter','P of no change in mean Diameter','Kendall Tau Weight Correlation', 'Kendall Tau Weight Pvalue','SRCC Weight','SRCC Weight Pvalue','Zscore of latest sample Weight','P of no change in mean Weight','Kendall Tau IV Correlation', 'Kendall Tau IV Pvalue','SRCC IV','SRCC IV Pvalue','Zscore of latest sample IV','P of no change in mean IV'])

for n in range(1,1270):
    try:
        df2 = pd.read_csv("./Data/"+str(n)+".csv")
        
    except FileNotFoundError:
        continue
    #relevantColumn = df2[column].to_list()
    
    listToAppend = [int(n),df2.shape[0]]
    fields = ['Diameter','Weight','IV']
    for field in fields:
        listToAppend = listToAppend + KendalsTau(df2['Year'].to_list(),df2[field].to_list())+Spearmansr(df2['Year'].to_list(),df2[field].to_list())+Zscore(df2[field].to_list(),field)
    df.loc[len(df)] = listToAppend
    
df.to_csv('Results.csv',index=False)

