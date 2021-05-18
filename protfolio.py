def Sharpe_Ratio(data,months): #Donwside Risk
    # Calculate total return and annualized return from price data 
    total_return = (data[-1] - data[0]) / data[0]

    # Annualize the total return over 4 year 
    annualized_return = ((1 + total_return)**(12/months))-1

    # Create the returns data 
    pf_returns = data.pct_change()

    # Calculate annualized volatility from the standard deviation
    vol_pf = pf_returns.std()*np.sqrt(250)

    # Calculate the Sharpe ratio 
    sharpe_ratio = (( annualized_return - rfr) / vol_pf)
    print (sharpe_ratio)



def  attribution():
        # Group dataframe by GICS sectors 
    grouped_df=portfolio_data.groupby('GICS Sector').sum()

    # Calculate active weights of portfolio
    grouped_df['active_weight']=grouped_df['pf_weights']-grouped_df['bm_weights']
    print (grouped_df['active_weight'])

def  correlation():
    data['corr'] = data['pf'].rolling(30).corr(df['quality'])