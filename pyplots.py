# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:23:04 2017

@author: psideris
"""

import csv 
import matplotlib.pyplot as plt
#import numpy as np

count_male = 0;
count_female = 0;
ctr = 0;
m_mapper = [];
m_mapper_surv = [];
m_dict = {};
f_mapper = [];
f_mapper_surv = [];
f_dict = {};

with open('train.csv', 'rt') as csvfile:
    freader = csv.reader(csvfile)
    for row in freader:
        if(row[4]=='male'):
            m_mapper.append(row[0])
            m_mapper_surv.append(row[1])
            m_dict[row[0]] = row[1]
            ctr += 1;
        elif(row[4]=='female'):
            f_mapper.append(row[0])
            f_mapper_surv.append(row[1])
            f_dict[row[0]] = row[1]
            

#print(m_dict)
    print(f_mapper)

plt.plot(m_mapper, m_mapper_surv, 'ro')
plt.axis([0, 100, -1, 2])

plt.plot(f_mapper, f_mapper_surv, 'bx')
plt.axis([0, 100, -1, 2])
plt.show()