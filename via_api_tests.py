
import requests
import base64

# the url of the web application in the index
url = 'https://api.demoblaze.com/'

# I created user with this username and password
userName='Renana'
password='12345678'

# Login:
# post request, we need to send json of username and pass,
# password- in base 64
# convert pass to base 64:
b = base64.b64encode(bytes(password, 'utf-8')) # bytes
base64_pass = b.decode('utf-8') # convert bytes to string
# the post request get a json object:
login_json = {"username":userName, "password":base64_pass}
# post request- login:
response_login=requests.post(url+'login', json=login_json,verify=False)
# check if the request success:
if response_login.status_code==200:
    print(response_login.text) # "Auth_token: UmVuYW5hMTY2NzIxNQ=="
    # extract the token
    my_token=response_login.text[13:-2]
    print('token: ',my_token) #token:  UmVuYW5hMTY2NzIxNQ==
    
    my = {"cookie": my_token, "flag": True}
    cart=requests.post(url+'viewcart', json=my,verify=False)
    print(cart.text)
    print(cart.json()['Items'])
    print('len= ',len(cart.json()['Items']))
    my1 = {"id": 3}
    x3 = requests.post(url+'view', json=my1,verify=False)
    print(x3.json())
    print('title: ',x3.json()['title'])
    print('price: ',x3.json()['price'])
