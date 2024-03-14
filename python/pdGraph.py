import pandas as pd


x = {'Mon': 1100, 'Tue': 900, 'Wed': 1100, 'Thu': 400, 'Fri': 2000}
y = {'Mon': 900, 'Tue': 900, 'Wed': 900, 'Thu': 900, 'Fri': 900}
i = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

revenue = pd.Series(data = x, index = i)
expenses = pd.Series(data = y, index = i)

print(revenue['Wed'])
print(expenses['Tue':'Thu'])

net_profit = revenue - expenses

print(net_profit.mean())


