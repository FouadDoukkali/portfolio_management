# =============================================================================
#  Hyper-parameters
# =============================================================================

import os
from datetime import date

import numpy as np
import pandas as pd
from pandas_datareader import data

import import_data as imd
import sensitivities as sv
import optimization as opt

#List of companies
companies = pd.read_excel('C:/Users/Fouad/Downloads/available_companies.xlsx')
#Wealth that should be invested 
wealth = 300

#Get data as returns and spots
X = imd.data_sourcing(companies, wealth, '2021-01-02', date.today())
X_returns = X[0]
X_spot = X[1]


#Solve problem 
solved_problem = opt.no_short_markovitz(X_returns,wealth,4)
#Weights
weights = solved_problem[0]
#On what
invest_on = solved_problem[1]
#Risk levels
levels = solved_problem[2]
print(invest_on,weights)