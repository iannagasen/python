import csv
import sys
import os

def read_portfolio(filename):
  portfolio = [] 
  with open(filename) as file: 
    rows = csv.reader(file) 
    for row in rows: 
      try:
        name = row[0] 
        shares = int(row[1]) 
        price = float(row[2]) 
        holding = (name, shares, price) 
        portfolio.append(holding)
      except ValueError as err: 
        print('Bad row:', row) 
        print('Reason:', err)
  return portfolio


def read_portfolio_v2(filename):
  with open(f'{os.getcwd()}\{filename}') as file:
    return [(row[0], int(row[1]), float(row[2])) for row in csv.reader(file)]
  
def try_read_portfolio_recursive(filename):
  try:
    return read_portfolio_v2(filename)
  except FileNotFoundError as _:
    print(f'No file named {filename} was found in {os.getcwd()}')
    filename = input('Enter another filename or enter -1: ')
    if filename == '-1': 
      raise SystemExit('Script was halted. Thanks!')
    return try_read_portfolio_recursive(filename)

def main(argv):
  if len(argv) == 1:
    filename = input('Enter filename:')
  elif len(argv) == 2:
    filename = argv[1]
  else:
    raise SystemExit(f'Usage: {argv[0]} [ filename ]')
  
  for name, shares, price in try_read_portfolio_recursive(filename):
    print(f'{name:>10s} {shares:10d} {price:10.2f}')


# __name__ is a builtin variable that always contains the name of the enclosing module.
# if a program is run as the main script such as `python readport.py`,
#   the __name__ variable is set to '__main__'
# otherwise, if the code is imported using a statement such as `import readport`
#   the __name__ variable is set to 'readport'
if __name__ == '__main__':
  main(sys.argv)

####
# this program can be run in two different ways from the CLI
#
# 1. `python readport.py`
# >> Enter filename: portfolio.csv
#
# 2. `python readport.py portfolio.csv`
#
# 3. python readport a b c
# >> Usage: readport.py a b c