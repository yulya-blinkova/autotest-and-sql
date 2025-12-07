import configuration
import requests
import data

def post_new_order():
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                        json=data.order_body,
                        headers=data.headers)



def get_order(track):
    return requests.get(url=f"{configuration.URL_SERVICE}{configuration.CREATE_NEW_ORDER}/track?t={track}")