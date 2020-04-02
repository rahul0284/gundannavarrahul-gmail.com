from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("C:/Users/Lenovo/Downloads/chromedriver_win32/chromedriver")
products=[]
prices=[]
driver.get("https://www.goibibo.com/hotels/find-hotels-in-Hubli/4175146706007535451/4175146706007535451/%7B%22ci%22:%2220200407%22,%22co%22:%2220200408%22,%22r%22:%221-2-0%22%7D/?{%22filter%22:{}}&sec=dom")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div', attrs={'class':'Layouts__Column-sc-1yzlivq-1 HotelCardstyles__HeadingInfoWrapperDiv-sc-1s80tyk-8 kRLydM'}):
    name=a.find('div', attrs={'class':'HotelCardstyles__HotelNameWrapperDiv-sc-1s80tyk-13 jbBSpQ'})
    #price=a.find('div', attrs={'class':'latoBlack font26 blackText appendBottom5'})
    products.append(name.text)
    #prices.append(price.text)
for a in soup.findAll('div', attrs={'class':'HotelCardstyles__PriceInfoWrapperDiv-sc-1s80tyk-28 hONQHN'}):
    #name=a.find('div', attrs={'class':'latoBlack font22 blackText appendBottom12'})
    price=a.find('span', attrs={'class':'HotelCardstyles__CurrentPrice-sc-1s80tyk-32 cPOgJy'})
    #products.append(name.text)
    prices.append(price.text)
df = pd.DataFrame({'Hotel Name':products,'Price':prices}) 
df.to_csv('Hotels.csv', index=False, encoding='utf-8')