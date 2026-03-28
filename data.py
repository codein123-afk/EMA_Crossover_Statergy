import pandas as pd
import matplotlib.pyplot as plt 

def load_data():
    data=pd.read_excel('/Users/apple/QuantNew/Data/Sbi.xlsx')
    data = data.sort_values("DATE")

    data["Date"]=pd.to_datetime(data["DATE"])
    data["Close"]=pd.to_numeric(data["CLOSE"],errors="coerce")

    data["SMA_20"]=data["Close"].rolling(window=20).mean()
    data["SMA_50"]=data["Close"].rolling(window=50).mean()
    data["SMA_200"]=data["Close"].rolling(window=200).mean()

    data["EMA_20"] = data["Close"].ewm(alpha= 0.5, adjust=False).mean()
    data["EMA_50"] = data["Close"].ewm(span=50, adjust=False).mean()
    data["EMA_200"] = data["Close"].ewm(span=200, adjust=False).mean()    
    return data[["Date", "Close", "EMA_20", "EMA_50", "EMA_200"]]


#data=load_data()
#plt.plot(data["Date"], data["Close"], label="Close Price")
#plt.plot(data["Date"], data["EMA_20"], label="EMA 20")
#plt.plot(data["Date"], data["EMA_50"], label="EMA 50")
#plt.plot(data["Date"], data["EMA_200"], label="EMA 200")
#plt.show()
