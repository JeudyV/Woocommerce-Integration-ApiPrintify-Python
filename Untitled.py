#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from woocommerce import API
import json
import requests
import os

Authorization = os.getenv('AUTHORIZATION', default='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjhmNmE5OTY1ZmUwZWEwY2Q4ZTQyNDhlOTVmMWZhMzRjYWZjN2Q2M2JhZGQxMmI1YTE0YTRmODM2MjBiNGM2Njg5NTM5MWIzZDc5MmMyMWNjIn0.eyJhdWQiOiIzN2Q0YmQzMDM1ZmUxMWU5YTgwM2FiN2VlYjNjY2M5NyIsImp0aSI6IjhmNmE5OTY1ZmUwZWEwY2Q4ZTQyNDhlOTVmMWZhMzRjYWZjN2Q2M2JhZGQxMmI1YTE0YTRmODM2MjBiNGM2Njg5NTM5MWIzZDc5MmMyMWNjIiwiaWF0IjoxNTg0MTM5NjgzLCJuYmYiOjE1ODQxMzk2ODMsImV4cCI6MTYxNTY3NTY4Mywic3ViIjoiNzAwMDg0OSIsInNjb3BlcyI6WyJzaG9wcy5tYW5hZ2UiLCJzaG9wcy5yZWFkIiwiY2F0YWxvZy5yZWFkIiwib3JkZXJzLnJlYWQiLCJvcmRlcnMud3JpdGUiLCJwcm9kdWN0cy5yZWFkIiwicHJvZHVjdHMud3JpdGUiLCJ3ZWJob29rcy5yZWFkIiwid2ViaG9va3Mud3JpdGUiLCJ1cGxvYWRzLnJlYWQiLCJ1cGxvYWRzLndyaXRlIiwicHJpbnRfcHJvdmlkZXJzLnJlYWQiXX0.Aen4A0Q0fulBDpjCEoAjYrkbM8KS-o_NrvLachcV96fB5xvScQ4fFnVfmPvEMgxR1Jdl4yloa38EWwJGbwY'
)


# In[1]:


# wcapi = API(
#     url="https://hollajack.com/",
#     consumer_key="ck_4cb10c586b18be0419f8ba53e8f9ab4c3c8ce576",
#     consumer_secret="cs_3dd50c2b150169c14db0c6c7af021f76766f16b7"
# )

# orders = json.loads(wcapi.get("products").text)
# print(orders)
# print(type(orders))


# In[ ]:


def Get_shops():

    url = "https://api.printify.com/v1/shops.json"
    
    headers = {
      'Authorization': Authorization
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    
    response = json.loads(response.text)

    print(response)
    
#Get_shops()


# In[ ]:


def Get_products(id_shops):

    url = "https://api.printify.com/v1/shops/{}/products.json".format(id_shops)
    
    headers = {
      'Authorization': Authorization
    }

    response = requests.request("GET", url, headers=headers)

    response = json.loads(response.text)

    print(response)
    
#Get_products('1601711')


# In[ ]:


def Get_all_blueprints():
    url = "https://api.printify.com/v1/catalog/blueprints.json"
    
    headers = {
      'Authorization': Authorization
    }

    response = requests.request("GET", url, headers=headers)
    
    response = json.loads(response.text)

    print(response)
    
#Get_all_blueprints()


# In[ ]:


def Create_products(id_shops, data):

    url = "https://api.printify.com/v1/shops/{}/products.json".format(id_shops)

    payload = data  #'symbol={}&side={}&orderQty={}&price={}&ordType={}'.format(symbol, side, orderQty, price, ordType)
    headers = {
      'Authorization': Authorization
    }
    
    response = requests.request("POST", url, headers=headers, data = payload)

    response = json.loads(response.text)

    print(response)
    


data = {
            "title": "Product3",
            "description": "Good product",
            "blueprint_id": 384,
            "print_provider_id": 1,
            "variants": [
                  {
                      "id": 45740,
                      "price": 400,
                      "is_enabled": True
                  },
                  {
                      "id": 45742,
                      "price": 400,
                      "is_enabled": True
                  },
                  {
                      "id": 45744,
                      "price": 400,
                      "is_enabled": True
                  },
                  {
                      "id": 45746,
                      "price": 400,
                      "is_enabled": False
                  }
              ],
              "print_areas": [
                {
                  "variant_ids": [45740,45742,45744,45746],
                  "placeholders": [
                    {
                      "position": "front",
                      "images": [
                          {
                            "id": "5e6c1887f64599000701e054", 
                            "x": 0.5, 
                            "y": 0.5, 
                            "scale": 1,
                            "angle": 0
                          }
                      ]
                    }
                  ]
                }
              ]
          }
    
Create_products('1601711', data)

