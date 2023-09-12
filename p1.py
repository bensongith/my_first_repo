import pandas as pd

d = {'Visit': ["SCREENING","Cycle1/Day1","Cycle1/Day4","Cycle1/Day8","Cycle1/Day15","Cycle1/Day22"],}

df = pd.DataFrame(data=d)

df['scanned'] = df['Visit'].str.split('/').str[-1]

df["New"]=df.scanned.str.extract('(\d+)')


ser = pd.Series(df['New'])
pd.to_numeric(ser, downcast ='signed')

# df.diff(periods = 1,axis = 0)

# df = df.apply(pd.to_numeric, errors='coerce')
print(df)
# DataType = df.dtypes
# print(DataType)
