import pandas as pd
import numpy as np
import datetime
from pandas_datareader import data
import os
from datetime import date



def data_sourcing(companies_dataframe, wealth, start_date, end_date):
    
    # Use pandas_reader.data.DataReader to load the desired data. 
    panel_data = data.DataReader(np.unique(companies_dataframe.symbol), 'yahoo', start_date, end_date)

    #Adj close, in order to get closing prices
    panel_data = panel_data.loc[:,'Adj Close']
    panel_data.reset_index(inplace=True,drop=False)

    #In order to get diversification assume that portfolio will have at least 5 potential stocks
    accessible = panel_data.iloc[-1,1:]<wealth

    #Filtering on accessible stocks
    panel_data = panel_data.iloc[:,1:].iloc[:,accessible.values]

    #Convert prices to returns and drop
    daily_returns = panel_data.pct_change().dropna()
    
    return daily_returns, panel_data

