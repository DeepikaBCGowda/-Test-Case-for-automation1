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
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='__next']/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div[3]/a").click()
if driver.title == "SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile":
    print('Title: ' ,driver.title)
    print('Url:', driver.current_url)    
class_count4 = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[4]/div[2]/div/div[1]/div[2]/button[5]").click()
class_count5 = driver.find_elements(By.CLASS_NAME, 'simo-card-ee_social_norm__3lfdT')
class_count6 = driver.find_elements(By.CLASS_NAME, 'simo-card-ee_plan_details__1G4nS')
count1=0
for i in class_count5:
    if i.text=="30% off and double data":
        count1=count1+1
for j in range(0,count1):
    name=class_count6[j].text
    name=name.replace("\n"," ")
    if name == "was 125GB 250GB Essential Plan was £27 £18.90 Per month":
        print("Validation successful")
    
          
