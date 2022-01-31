from tvDatafeed import TvDatafeed,Interval
import os
import progressbar
from time import sleep

tv=TvDatafeed(auto_login=False)


path='C:\\Users\\suraj\\Desktop\\Total EOD DATA FROM TV'
if not os.path.exists(path):
    os.makedirs(path)

f=open("stocklist.txt","r")

#f=open("totalmarket.txt","r")
#f=open("other.txt","r")
ticker=f.readlines()


num_lines=len(ticker)

bar = progressbar.ProgressBar(maxval=num_lines,widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for x in range(num_lines):
    symboll=ticker[x].strip()
    try:
        dff = tv.get_hist(symbol=symboll,exchange='NSE',interval=Interval.in_daily,n_bars=10000,extended_session=False)
        print('Downloading........'+symboll)
        dff.to_csv(path +'\\%s.csv'%symboll)
        bar.update(x)
    except:
        try:
            dff = tv.get_hist(symboll,'CURRENCYCOM',interval=Interval.in_daily,n_bars=10000)
            print('Downloading........'+symboll)
            dff.to_csv(path +'\\%s.csv'%symboll)
            bar.update(x)
        except:
            print("Not able to download @@@   "+symboll) 
            continue

        continue

        


f.close()
bar.finish()

