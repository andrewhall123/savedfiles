from bs4 import BeautifulSoup
import requests, urllib
import numpy as np

def but(url):
    soup=BeautifulSoup(url,"lxml")
    return soup 

def getSymbols(soup):
    symbols=[]
    company=soup.find_all('td', {'class':'ds_symbol'})
    for i in company:
        symbols.append(i.get_text())
    return symbols
    
def getPrices(soup):
    prices=[]
    price=soup.find_all('td', {'class':'ds_last'})
    for i in price:
        prices.append(float(i.get_text()))
    return prices
    
def getVolume(soup):
    volumes=[]
    volume=soup.find_all('td', {'class':'ds_volume'})
    for i in volume:
        volumes.append(int(i.get_text().replace(',','')))
    return volumes


def getLiquid(prices, volumes,symbols):
    liquid=prices*volumes
    relation={}
    for i, liquidy in enumerate(liquid):
        if liquidy>=25000000:
            relation[symbols[i]]=(float("%.2f" %liquidy), float("%.2f" %prices[i]))
    return relation

def __init__():
    url=requests.get('http://www.barchart.com/stocks/gapup.php')
    data=url.text
    soup=but(data)
    symbols=np.array(getSymbols(soup))
    prices=np.array(getPrices(soup))
    volume=np.array(getVolume(soup))
    liquid=getLiquid(prices, volume,symbols)
    print(liquid)
    return liquid
    
    
if __name__=="__main__":
    __init__()
