import numpy
import pandas as pd
import math
import csv

fields = ['Diameter','Weight','IV']
meanSigma = [0,0,0]

df = pd.DataFrame(columns = fields)
for n in range(1,1270):
    try:
        df2 = pd.read_csv("./Data/"+str(n)+".csv")
        
    except FileNotFoundError:
        continue
    
    #df2 = pd.DataFrame([df2['Diameter'].std(skipna=True),df2['Weight'].std(skipna = True),df2['IV'].std(skipna = True)],columns = fields)
    df.loc[len(df)] = [df2['Diameter'].std(skipna=True),df2['Weight'].std(skipna=True),df2['IV'].std(skipna=True)]
    
meanSigma = [df['Diameter'].mean(),df['Weight'].mean(),df['IV'].mean()]

with open('MeanSigmaValues', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
     
    write.writerow(fields)
    write.writerows([meanSigma])