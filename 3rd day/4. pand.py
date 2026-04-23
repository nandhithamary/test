import pandas as pd

mydataset ={
    "cars": ("bmw","volvo","ford"),
    "passengers":(3,7,3)
}

mycar=pd.DataFrame(mydataset)
print(mycar)