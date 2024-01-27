import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
categories = set(data['whoAmI'])
for category in categories:
  data[category] = (data['whoAmI'] == category).astype(int)
print(data.head())