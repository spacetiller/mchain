""" 
Created on Sat Jan 14 14:33:26 2017 
 
@author: yunjinqi 
 
E-mail:yunjinqi@qq.com 
 
Differentiate yourself in the world from anyone else. 
"""  
#######################################################布林带突破策略  
#原理：突破95日均线，方差为2的布林带，进场；价格跌破34日均线的时候离场  
######################################################引入相应模块  
from OkcoinSpotAPI import *  
import pandas as pd  
import numpy as np  
import datetime  
import time  
#####################################################初始数据  
okcoinRESTURL = 'www.okcoin.cn'    
apikey='a3c363bd-28c7-4f6d-a04d-ac4a58e929b9'  
secretkey='83782FBD5E365EFC511EC739C0B54103'  
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)  
#####################################################构建布林带、移动平均线指标  
def bbands_MA(M,N):  
    m=str(M)  
    n=str(N)  
    try:  
        kline=pd.DataFrame(okcoinSpot.getKline('1min',m,'0'))  
    except ValueError as e:  
        print('json错误')  
    mid=kline.iloc[::,4].mean()  
    std=kline.iloc[::,4].std()  
    upper=mid+N*std  
    lower=mid-N*std  
    ma=kline.iloc[::,4].mean()  
    result=[upper,mid,lower]  
    return result  
######################################################交易  
try:  
      ref_boll=bbands(94,2)  
      ref_upper=boll[0]  
      ref_lower=boll[2]    
      ref_close=okcoinSpot.getKline('1min','1','0')[0][4]  
      ref_ma34=pd.DataFrame(okcoinSpot.getKline('1min','34','0')).iloc[::,4].mean()  
except:  
      print('json错误')  
        
time.sleep(58)  
while True:  
    try:  
      boll=bbands(94,2)  
      upper=boll[0]  
      lower=boll[2]    
      close=okcoinSpot.getKline('1min','1','0')[0][4]  
      ma34=pd.DataFrame(okcoinSpot.getKline('1min','34','0')).iloc[::,4].mean()  
    except:  
      print('json错误')  
      continue  
    if close>upper and ref_close<ref_upper:  
      print('买入信号',okcoinSpot.trade('btc_cny','buy','7500','0.01'))  
    if close<ma34 and ref_close>ref_ma34:  
      print('卖出信号',okcoinSpot.trade('btc_cny','sell','1','0.01'))  
      
    try:  
      ref_boll=bbands(94,2)  
      ref_upper=boll[0]  
      ref_lower=boll[2]    
      ref_close=okcoinSpot.getKline('1min','1','0')[0][4]  
      ref_ma34=pd.DataFrame(okcoinSpot.getKline('1min','34','0')).iloc[::,4].mean()  
    except:  
      print('json错误')  
      continue  
    time.sleep(58)  
    now=datetime.datetime.now()  
    now=now.strftime('%Y-%m-%d %H:%M:%S')   
    i=i+1  
    print(now,i)