import pandas as pd

from pandas import Series
arr=[5,6,1,5]
s=Series(arr)
print (s)
import numpy as np
#________________________________________________________________
#파이썬 내장 딕트형
a={0:6,1:3,2:2}
print(a)
print(type(a))
print(a.keys())
print(a.values())
#----------------------------------
#판다스형
a=pd.Series([5,2,1]) 
print(a)
#또는
valuesA=[5,2,1]
indexA=[0,1,2]
s=Series(valuesA,indexA)
print(a)




