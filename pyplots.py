"""
Created on Sat Feb 11 11:23:04 2017

@author: psideris
"""

import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt

"""
count_male = 0;
count_female = 0;
ctr = 0;

m_mapper = [];
m_mapper_surv = [];
m_mapper_age = [];
m_dict = {};

f_mapper = [];
f_mapper_surv = [];
f_mapper_age = [];
f_dict = {};

with open('train.csv', 'rt') as csvfile:
    freader = csv.reader(csvfile)
    for row in freader:
        print(row["Sex"])
        if(row[4]=='male' and row[5].isdigit()):            
            m_mapper.append(row[0])
            m_mapper_surv.append(row[1])
            m_mapper_age.append(round(row[5]))
            #m_dict[row[0]] = row[1]
        elif(row[4]=='female' and row[5].isdigit()):
            f_mapper.append(row[0])
            f_mapper_surv.append(row[1])
            f_mapper_age.append(row[5])
            #f_dict[row[0]] = row[1]
"""            

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

survived  = train["Survived"]
age_males_surv = train["Age"][train["Sex"] == "male"][train["Survived"] == 1]
age_males_dead = train["Age"][train["Sex"] == "male"][train["Survived"] == 0]
age_females_surv = train["Age"][train["Sex"] == "female"][train["Survived"] == 1]
age_females_dead = train["Age"][train["Sex"] == "female"][train["Survived"] == 0]

sex = train["Sex"]

features  = train.drop("Survived", axis = 1)
age_clear = features["Age"].fillna(0)

plt.hist([age_males_surv, age_males_dead, age_females_surv, age_females_dead],
         bins=[0,10,20,30,40,50,60,70,80,90], color=['green', 'blue', 'red', 'brown'], label=['Male Survived', 'Male Deceased', 'Female Survived', 'Female Deceased'])

#plt.legend(handles=[blue_line])
plt.legend()
plt.xlabel('Age')
plt.ylabel('Quantity')
plt.title('Correlating age and gender with survival')
plt.grid(True)
