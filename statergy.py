import data

df=data.load_data()

def Crossover(df):
    df["EMA_diff"] = df["EMA_20"] - df["EMA_200"]


    # Diff shifts from negative to positive---Buy
    # Diff shifts from positive to negative---sell
    
    df["Buy"] = (( df["EMA_diff"].shift(1) < 0) & (df["EMA_diff"] > 0))

    df["Sell"] = ((df["EMA_diff"].shift(1) > 0) & (df["EMA_diff"] < 0))

    df["Position"] = 0
    position = 0

    for i in range(len(df)):
        if df["Buy"].iloc[i] and position == 0:
            position = 1
        elif df["Sell"].iloc[i] and position == 1:
            position = 0
    
        df.iloc[i, df.columns.get_loc("Position")] = position

    return df



