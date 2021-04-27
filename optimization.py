import cvxpy as cp
import numpy as np
import pandas as pd
def no_short_markovitz(df,wealth,num_asset):
    stock_sample = df.dropna().rolling(window = 15).mean().iloc[-1,:].sort_values()[-num_asset:].index
    df = df.loc[:,stock_sample]
    Sigma = df.cov().values
    mu = df.mean().values

    w = cp.Variable(num_asset)
    gamma = cp.Parameter(nonneg=True)
    ret = mu.T@w 
    risk = cp.quad_form(w, Sigma)
    prob = cp.Problem(cp.Maximize(ret - gamma*risk), 
                   [cp.sum(w) == 1, 
                    cp.norm(w,1) <= 4,
                    w >= 0])
    values = []
    risk_level = []
    for i in np.arange(100):
        gamma.value = abs(np.random.normal(1,0.5))
        prob.solve()
        values.append(w.value)
        risk_level.append(gamma.value)

    return values, stock_sample,risk_level

