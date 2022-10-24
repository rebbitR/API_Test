
import requests
import base64

# the url of the web application in the index
url = 'https://api.demoblaze.com/'

# I created user with this username and password
userName='Renana'
password='12345678'

# Login:

# function logIn() {
#   var pass = b64EncodeUnicode(document.getElementById("loginpassword").value);
#   var username = document.getElementById("loginusername").value;
#   if (pass == "" || username == "") {
#     alert("Please fill out Username and Password.");
#   } else {
#     $.ajax({
#       type: 'POST',
#       url: API_URL + '/login',
#       data: JSON.stringify({ "username": username, "password": pass }),
#       contentType: "application/json",


# post request, we need to send json of username and pass,
# password- in base 64
# convert pass to base 64:
b = base64.b64encode(bytes(password, 'utf-8')) # bytes
base64_pass = b.decode('utf-8') # convert bytes to string
# the post request get a json object:
login_json = {"username":userName, "password":base64_pass}
# the API_URL= https://api.demoblaze.com/login
# post request- login:
response_login=requests.post(url+'login', json=login_json,verify=False)
# check if the request success:
if response_login.status_code==200:
    print(response_login.text) # "Auth_token: UmVuYW5hMTY2NzIxNQ=="
    # extract the token
    my_token=response_login.text[13:-2]
    print('token: ',my_token) #token:  UmVuYW5hMTY2NzIxNQ==

    # sign in to the cart- I nead the token for my user cart

    #     if (token.length > 0) {
    #       $.ajax({
    #         type: 'POST',
    #         url: API_URL + '/viewcart',
    #         data: JSON.stringify({ "cookie": token, "flag": true }),

    # the API_URL= https://api.demoblaze.com/viewcart
    cart_json = {"cookie": my_token, "flag": True}
    response_cart=requests.post(url+'viewcart', json=cart_json,verify=False)
    # check if the request success:
    if response_cart.status_code==200:
        # I get properties of my cart
        print(response_cart.text)
        # extract the list of items from json
        list_items=response_cart.json()['Items']
        print(list_items)
        # print('len= ',len(cart.json()['Items']))
        # 1. Number of items in the card == 1:
        assert len(list_items)==1

        # extract the item
        item=list_items.pop()
        print(item)# {'cookie': 'Renana', 'id': '77065f64-7e07-b43b-7452-d8711345b18b', 'prod_id': 3}
        # 4. Item’s id == 3:
        assert item['prod_id']==3

        # post request to view the properties of product that his id=3:

        #           } else {
        #             data.Items.forEach(function (articleItem) {
        #               $.ajax({
        #                 type: 'POST',
        #                 url: API_URL + '/view',
        #                 data: JSON.stringify({ "id": articleItem.prod_id }),
        #                 contentType: "application/json",
        
        # API_URL: https://api.demoblaze.com/view
        # the json object need num of id product
        item_json = {"id": 3}
        response_item = requests.post(url+'view', json=item_json,verify=False)
        # the properties of product in json:
        print(response_item.json())
        # {'cat': 'phone',
        # 'desc': 'The Motorola Google Nexus 6 is powered by 2.7GHz quad-core Qualcomm Snapdragon 805 processor and it comes with 3GB of RAM.',
        # 'id': 3,
        # 'img': 'imgs/Nexus_6.jpg',
        # 'price': 650.0,
        # 'title': 'Nexus 6'}

        # 2. The price of the selected phone == 650:
        assert response_item.json()['price']==650.0
        # 3. The title of the selected phone == “Nexus 6”:
        assert response_item.json()['title']=='Nexus 6'

        print('title: ',response_item.json()['title'])
        print('price: ',response_item.json()['price'])
