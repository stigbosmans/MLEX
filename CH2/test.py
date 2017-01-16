import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;
from sklearn.model_selection import StratifiedShuffleSplit;

houses=pd.read_csv("housing.csv");
houses["income_cat"]=np.ceil(houses["median_income"]/1.5);
houses["income_cat"].where(houses["income_cat"]<5,5.0,inplace=True);
houses["income_cat"].hist(bins=1)
print(houses.describe())
plt.show();

split=StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
for traini, testi in split.split(houses,houses["median_income"]):
    trainset=houses.loc(traini)
    testset=houses.loc(testi)

testset.hist(bins=50);

plt.show();