#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from woocommerce import API
import json

wcapi = API(
    url="https://hollajack.com/",
    consumer_key="ck_4cb10c586b18be0419f8ba53e8f9ab4c3c8ce576",
    consumer_secret="cs_3dd50c2b150169c14db0c6c7af021f76766f16b7"
)

orders = json.loads(wcapi.get("orders").text)
print(orders)

