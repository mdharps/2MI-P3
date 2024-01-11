import numpy
import pandas as pd
import math
import csv

fields = ['Diameter','Weight','IV']

for n in range(1,1270):
    try:
        df = pd.read_csv("./Data/"+str(n)+".csv")
        
    except FileNotFoundError:
        continue
    
    for i in range(0,len(df)):
        if (not(math.isnan(df.Diameter[i])) and not(df.Diameter[i] < 1.7 and df.Diameter[i] > 1.67)):
            print("\nSurprising value in",n,".csv on row",i)
            print("\n Diameter ",df.Diameter[i])
        if (not(math.isnan(df.Weight[i])) and not(df.Weight[i] < 46 and df.Weight[i] > 42)):
            print("\nSurprising value in",n,".csv on row",i)
            print("\n Weight ",df.Weight[i])
        if (not(math.isnan(df.IV[i])) and not(df.IV[i] < 256 and df.IV[i] > 243)):
            print("\nSurprising value in",n,".csv on row",i)
            print("\n IV ",df.IV[i])
        
    
