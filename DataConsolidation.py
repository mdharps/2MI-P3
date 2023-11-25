# importing module
from pandas import *
import csv

Diameter = []
Weight = []
IV = []
Year = []
n = 2
for n in range(1,1270):
    try:
        data = read_csv(str(n)+".csv")
        # converting column data to list
        Diameter =  Diameter + data['Diameter'].tolist()
        Weight = Weight + data['Weight'].tolist()
        IV = IV + data['IV'].tolist()
        Year = Year + data['Year'].tolist()
    except FileNotFoundError:
        continue

    
fields = ["Diameter","Weight","IV","Year"]
rows = zip(Diameter, Weight, IV, Year)
with open("ConsolidatedData.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    for row in rows:
        writer.writerow(row)

 
