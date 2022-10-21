
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.demoblaze.com/index.html')
driver.maximize_window()
element=driver.find_element("id","login2")
element.click()
time.sleep(2)
username='Renana'
password='12345678'
driver.find_element(By.ID,"loginusername").send_keys(username)
driver.find_element(By.ID,"loginpassword").send_keys(password)
time.sleep(1)
driver.find_element(By.XPATH, '//button[text()="Log in"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[3]/div/a/img').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a').click()
driver.find_element(By.XPATH, '//*[@id="cartur"]').click()
time.sleep(2)
card=driver.find_element(By.XPATH,'//*[@id="tbodyid"]')
items=card.find_elements(By.TAG_NAME,'tr')
if len(items)==1:
    print(items)
    item=items[0]
    print(item)
    properties=item.find_elements(By.TAG_NAME,'td')
    print(properties)
    name=properties[1]
    print(name)
    print(name.text)
    if name.text=='Nexus 6':
        price=properties[2]
        print(price.text)
        if price.text=='650':
            print(item.id)
            print('success!!!')
        else:
            print('the price of item !=650')
    else:
        print('the name of the item != "Nexus 6"')
else:
    print('num items in the cart more than 1')
driver.quit()
