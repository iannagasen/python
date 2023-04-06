# readport.py
#
# read a file of 'NAME,SHARES,PRICE' data

def read_portfolio(filename):
  portfolio = []
  with open(filename) as file:
    for line in file:
      row = line.split(',')
      try:
        name = row[0]
        shares = int(row[1])
        price = float(row[2])
        holding = (name, shares, price)
        portfolio.append(holding)
      except ValueError as err:
        print('Bad row: ', row)
        print('Reason: ', err)
  return portfolio


# this version uses Tuple Unpacking
# to be more concise  
def read_portfolio_v2(filename):
  portfolio = []
  with open(filename) as file:
    for line in file:
      try: 
        name, shares, price = line.strip().split(',') # unpacking a tuple
        portfolio.append((name, int(shares), float(price))) # creates a TUPLE and append it
      except ValueError:
        print(f'Bad row: {line.strip()}')
  return portfolio



# This version of the function uses a list comprehension 
# to read the lines of the file, 
# split them into the individual fields, 
# convert the fields to the correct data types, 
# and pack them into tuples. 
# The resulting list of tuples is then returned directly.
def read_portfolio_v3(filename):
  with open(filename) as file:
    return [(name, int(shares), float(price))
      for name, shares, price in [line.strip().split(',') for line in file]]