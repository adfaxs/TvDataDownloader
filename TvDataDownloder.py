from credentials import get_cred
from tvDatafeed import TvDatafeed,Interval
import os
import progressbar
from time import sleep

username,password=get_cred('tradingview')
tv=TvDatafeed(username=username,password=password)

path='C:\\Users\\suraj\\Desktop\\EOD DATA FROM TV'
if not os.path.exists(path):
    os.makedirs(path)

f=open("stocklist.txt","r")
ticker=f.readlines()

num_lines=len(ticker)

bar = progressbar.ProgressBar(maxval=num_lines,widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

for x in range(num_lines):
     df = tv.get_hist(ticker[x].strip(),'NSE',interval=Interval.in_daily,n_bars=10000)
     df.to_csv(path +'\\%s.csv'%ticker[x].strip())
     bar.update(x)
    
f.close()
bar.finish()

