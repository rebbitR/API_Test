
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
456
# chromedriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# search in google chrome: https://www.demoblaze.com/
driver.get('https://www.demoblaze.com/')
# # maximize window browser
# driver.maximize_window()
# # click on 'Log in' tab
# element=driver.find_element("id","login2")
# element.click()
# time.sleep(2)
# # send the username and password
# username='Renana'
# password='12345678'
# driver.find_element(By.ID,"loginusername").send_keys(username)
# driver.find_element(By.ID,"loginpassword").send_keys(password)
# time.sleep(1)
# # find the 'Log in' button an click on it
# driver.find_element(By.XPATH, '//button[text()="Log in"]').click()
# time.sleep(5)
# # choose the product Nexus 6
# driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[3]/div/a/img').click()
# time.sleep(2)
# # add to cart (find the 'Add to cart' button an click on it)
# driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a').click()
# # click on 'Cart' tab
# driver.find_element(By.XPATH, '//*[@id="cartur"]').click()
# time.sleep(2)
# # find the list of items in the cart
# card=driver.find_element(By.XPATH,'//*[@id="tbodyid"]')
# items=card.find_elements(By.TAG_NAME,'tr')
# # check if number of items in the card == 1
# if len(items)==1:
#     # pop the element in the cart
#     item=items.pop()
#     # find the properties list of element by tag name
#     properties=item.find_elements(By.TAG_NAME,'td')
#     # check if the title of the selected phone == “Nexus 6”
#     title=properties[1]
#     if title.text=='Nexus 6':
#         # check if the price of the selected phone == 650
#         price=properties[2]
#         if price.text=='650':
#             print('success!!!')
#         else:
#             print('the price of item !=650')
#     else:
#         print('the name of the item != "Nexus 6"')
# else:
#     print('num items in the cart more than 1')
# # assert:
# assert len(items)==1
# driver.quit()

# # ---import requests
# import requests
# import xmltojson
#
# import flask
# # https://www.demoblaze.com/prod.html?idp_=3
# response = requests.get("https://www.demoblaze.com/cart.html",verify=False)
# print(type(response))
# json_ = xmltojson.parse(response.text)
# print(json_)

# print(response.status_code)
# print(response.text)
# print(response.request.url)
# if (
#     response.status_code != 204 and
#     response.headers["content-type"].strip().startswith("application/json")
# ):
#     try:
#         print(response.json())
#     except ValueError:
#         print("kkk")
# # print(response.json())
import xmltojson
import json

# import requests
# import html_to_json
#
# # Sample URL to fetch the html page
# url = "https://www.demoblaze.com/"
# myobj = {'username': 'Renana',
#          'password':'12345678'}
#
# res=requests.post('https://www.demoblaze.com/login',verify=False,data=myobj)
# if res.status_code==200:
#     print(res.json())
#     res2=requests.get(res.url,verify=False)
#     if res.text==res2.text:
#         print('jkj')
# # Get the page through get() method
# html_response = requests.get(url=url,verify=False)
# print(html_response.headers)
# print(html_response.text)
# output_json = html_to_json.convert(html_response.text)
# print(type(output_json))
# print(output_json)