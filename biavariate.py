# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:12:30 2022

@author: SPTINT-16
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("C:/Users/SPTINT-16/Desktop/Nithya/train_and_test2.csv")

#g=sns.countplot(x='Sex',hue='Survived',data=data)

#g=sns.countplot(x='Embarked',hue='Survived',data=data)

#g=sns.countplot(x='Embarked',hue='Pclass',data=data)

#g=sns.countplot(x='Pclass',hue='Survived',data=data)

def add_family(df):
    df['FamilySize']=df['sibsp']+df['Parch']+1
    return df
data=add_family(data)
#print(data.head(10))

g=sns.countplot(x='FamilySize',hue='Survived',data=data)