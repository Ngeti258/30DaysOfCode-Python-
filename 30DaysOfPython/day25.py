import pandas as pd
import numpy as np
nums=[1,2,3,4,5]
s=pd.Series(nums)
print(s)

r=pd.Series(nums,index=[1,2,3,4,5])
print(r)

fruits=['Orange','Banana','Mango']
fruits=pd.Series(fruits,index=[1,2,3])
print(fruits)

dict={'name':'Asabeneh','country':'Finland','city':'Helsinki'}
e=pd.Series(dict)
print(e)

s=pd.Series(10,index=[1,2,3])
print(s)

s=pd.Series(np.linspace(5,20,10))
print(s)

data=[['Asabeneh','Finland','Helsinki'],
['David','UK','London'],
['John','Sweden','Stockholm']]

df=pd.DataFrame(data,columns=['Names','Country','City'])
print(df)

#data={'Name':['Asabeneh','David','John'],'Country':['Finland','UK','Sweden'],'City':['Helsinki','london','Stockholm']}
df=pd.DataFrame(data)
print(df)

# import 
# df=pd.read_csv('weight_height.csv')
# print(df.shape)

import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
weights = [74, 78, 69]
df['Weight'] = weights
print(df)

df['Height']=[173,175,169]
df['Height']=df['Height']*0.01
print(df)

def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()
df['BMI']=bmi

birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)
