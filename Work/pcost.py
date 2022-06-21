# pcost.py
#
# Exercise 1.27

import csv
import sys
def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(f)
        for line in f:
            row = line.split(',')
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
        return total_cost

    
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)


#############################
#gzip files
'''
import gzip

with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')
'''