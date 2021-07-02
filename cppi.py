import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

#! safe asset is 3  month treasurey bond 
def cppi(returns, cppi=100, floor_percent=0.7, m=4):
    TreasueryBond = yf.Ticker('^IRX')
    safe_asset_rate = pd.DataFrame(TreasueryBond.history("1D"))['Close'].values[0]
    safe_assets = pd.DataFrame().reindex_like(returns)
    safe_assets[:] = safe_asset_rate / 12

    #Initial portfolio value
    CPPI = cppi
    # This is the minimum value I want to preserve
    F = CPPI * floor_percent

    CPPI_values = pd.DataFrame().reindex_like(returns)
    floor_values = pd.DataFrame().reindex_like(returns)
    floor_values[:] = F
    for i in range(len(returns)):
        C = CPPI - F
        risky_asset_e = max(min(m * C, CPPI),0) 
        risklet_asset = CPPI - risky_asset_e 
        CPPI = risky_asset_e * (1 + returns.iloc[i].item()) + risklet_asset * (1 + safe_assets.iloc[i].item())
        CPPI_values.iloc[i] = CPPI
    return CPPI_values, floor_values

def tipp(returns, cppi=100, floor_percent=0.7, m=4, safe_asset_rate=0.02, gap=1):
    safe_assets = pd.DataFrame().reindex_like(returns)
    safe_assets[:] = safe_asset_rate / 12

    #Initial portfolio value
    CPPI = cppi
    # This is the minimum value I want to preserve
    F = CPPI * floor_percent

    CPPI_values = pd.DataFrame().reindex_like(returns)
    floor_values = pd.DataFrame().reindex_like(returns)
    floor_values[:] = F
    CPPI_max = CPPI
    for i in range(len(returns.index)):
        F_updated = CPPI * floor_percent
        if F < F_updated:
            F = F_updated
            
        if i % gap != 0 and i != 0:
            CPPI = risky_asset_e * (1 + returns.iloc[i].item()) + risklet_asset * (1 + safe_assets.iloc[i].item())
            CPPI_values.iloc[i] = CPPI
            continue  
        C = CPPI - F
        risky_asset_e = max(min(m * C, CPPI),0) 
        risklet_asset = CPPI - risky_asset_e
        CPPI = risky_asset_e * (1 + returns.iloc[i].item()) + risklet_asset * (1 + safe_assets.iloc[i].item())
        CPPI_values.iloc[i] = CPPI
        floor_values.iloc[i] = F

    return CPPI_values, floor_values


data = pd.read_csv('StockData/S&P.csv')
data.set_index('Date', inplace=True)
data.index = pd.to_datetime(data.index, format='%Y-%m-%d')

returns = data['Adj Close']['2000':'2020'].resample('M').ffill().pct_change()

returns = returns.dropna()
returns =  returns.to_frame()
returns.reset_index(inplace=True)
returns.set_index('Date', inplace=True)
tipp, floor_values_Adj = tipp(returns,m=4,gap=1)
cppi, floor_values = cppi(returns)
normal = 100*(1+returns).cumprod()
#  !Plot CPPI ,  Normal, Floor
fig = plt.figure()
fig.suptitle('Using CPPI')
plt.plot(cppi, color="blue", label="With CPPI")
plt.plot(normal, "--", color='green', label="Without CPPI")
plt.plot(floor_values, color='red', label="Floor")
plt.legend(loc=True)
plt.show()

#! Plot TIPP, Normal, Adjusted Floor
fig = plt.figure()
fig.suptitle('Using TIPP')
plt.plot(tipp, color="blue", label="With TIPP")
plt.plot(normal, "--", color='green', label="Without TIPP")
plt.plot(floor_values_Adj, color='red', label="Adj Floor")
plt.legend(loc=True)
plt.show()

