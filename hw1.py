import pandas as pd
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument("--disable-notifications")

csvfile="hw1.csv"
tmp=[["" for _ in range(1)]for _ in range(1)]
with open(csvfile,'w+') as fp:
    writer=csv.writer(fp)
    tmp[0][0]="日期"
    df=pd.DataFrame()
    df=pd.date_range('20200122','20230314')
    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://covid-19.nchc.org.tw/city_confirmed.php?mycity=%E5%85%A8%E9%83%A8%E7%B8%A3%E5%B8%82")
    
    
    for the_date in df.date:
        print(the_date)
        
        soup=BeautifulSoup(driver.page_source,"lxml")
        County=soup.find_all(class_="btn btn-outline-secondary btn-lg")
        if((len(tmp[0])==1)): 
            for item in County: #建立所有的country
                tmp[0].append(item.text)   
            writer.writerow(tmp[len(tmp)-1])
        time.sleep(1)

        #輸入
        try:
            element1=driver.find_element(By.XPATH,"//*[@id='myTable03_wrapper']/div[4]/div[3]/div/table/tfoot/tr/th[1]/input")
            element1.click()
            element1.clear()
            element1.send_keys(str(the_date))
            
            element2=driver.find_element(By.XPATH,"//*[@id='myTable03_wrapper']/div[4]/div[3]/div/table/tfoot/tr/th[3]/input")
            if len(tmp)==1: #判斷是否為第一次輸入(後續不需要再填入'全區')
                element2.click()
                element2.send_keys('全區')
            time.sleep(1)    
            soup=BeautifulSoup(driver.page_source,"lxml")
            print("I'm ready~.~")
        except NoSuchElementException:
            print("Loading too long")
            continue

        #找位置
        Target_table=soup.find(attrs={"aria-describedby":"myTable03_info"})    
        Target_table=Target_table.find("tbody").find_all("tr")
        
        tmp.append("0")    #增加一行
        for i in range(len(tmp[0])) :  #新增該行的列數     
            tmp[len(tmp)-1]=["0" for _ in range(len(tmp[0]))]     
        tmp[len(tmp)-1][0]=the_date
        
        for each_tr in Target_table:    #每行資料
            col=each_tr.find_all("td")  #每格資料
            if(col[0].text=="No matching records found"):
                break

            for con in range(len(tmp[0])): #判斷地區
                 if(tmp[0][con]==col[1].text):
                     tmp[len(tmp)-1][con]=col[3].text   #填入該區的疫情 
                     break
        writer.writerow(tmp[len(tmp)-1])
    driver.quit()            
    print("okkk")
