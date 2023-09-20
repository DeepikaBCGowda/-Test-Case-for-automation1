from selenium import webdriver
from selenium .webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.bt.com")
driver.maximize_window()
time.sleep(5)
driver.switch_to.frame("trustarc_cm")
driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div[3]/a[1]').click()
driver.switch_to.default_content()
time.sleep(5)
uname1=driver.find_element(By.XPATH,'//*[@id="bt-navbar"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[4]/a').click()
driver.find_element(By.XPATH,'//*[@id="bt-navbar"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[4]/ul/li/ul/li[2]/a').click()
class_count = driver.find_elements(By.CLASS_NAME, 'flexpay-card_card_wrapper__Antym')
count=0
for item in class_count:
    count=count + 1
print(count)
if count>=3:
    print("'See Handset details' are greater than 3")
else:
    print("'See Handset details' are less than 3")

sim_only = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div[3]/a")
driver.execute_script("arguments[0].scrollIntoView();",sim_only)
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='__next']/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div[3]/a").click()
if driver.title == "SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile":
    print('Title: ' ,driver.title)
    print('Url:', driver.current_url)    
class_count1 = driver.find_elements(By.CLASS_NAME, 'simo-card-ee_social_norm__3lfdT')
class_count2 = driver.find_elements(By.CLASS_NAME, 'simo-card-ee_text_container__30ltg')

count=0
for item in class_count1:
    if item.text=="30% off and double data":
        for i in class_count2:
            if ("was 125GB" and "250GB") in i.text:
                count=count+1  
print(count)  
driver.close() 
