
# the import statement creates a new `namespace` (or environment)
# and executes all the statements in the associated .py file within that name space.
# to access the contents of the namespace after import, use the name of the module as prefix
# Ex: readport.read_portfolio

import readport

def portfolio_cost(filename):
  '''
  Compute the total shares * price of a portfolio
  '''
  port = readport.read_portfolio(filename)
  # port is the a tuple of list
  # the list contains: [1] -> name, [2] -> shares, [3] -> price
  # in this case we use _(underscore) to indicate `dont care`
  return sum(shares * price for _, shares, price in port)
