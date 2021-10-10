from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver

class ParseArticle:
    def collectInformation(self,nameOfCurrency):

        URL='https://coinmarketcap.com/currencies/'+nameOfCurrency+'/news/'
        r = requests.get(URL, 'html.parser').text
        soup= BeautifulSoup(r,'lxml')
        header=soup.h2.text
        print(header,'\n')
        wholeText=soup.text.strip()
        count=0
        for i in range(len(wholeText)):
            print(wholeText[i],end='')
            if wholeText[i]==' ':
                count+=1
            if count==6:
                print('\n',end='')
                count=0
        print()
        print('\n')