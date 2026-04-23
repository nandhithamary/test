import pandas as pd

data={
    "students":["alice","bob","charlie","dony","eve","femi","george","heaven","iza","john"],
    "marks": [90,89,98,97,87,88,92,94,96,95]
}

df=pd.DataFrame(data)
print(df.loc[0],df.loc[5])