import pandas as pd
h = pd.read_csv('w1006-4.csv')
h['W1006'] = h['W1006'] - h.loc[0, 'W1006']
#h = h.drop(index=0)
print('postprocessing drawdown-unc')
h.to_csv('w1006-4.post.csv', index=False)