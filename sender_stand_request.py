import configuration
import data
import requests

def new_order(order_body): # Создаем заказ
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_POST,
                    json=order_body,
                    headers=data.headers)
response = new_order(data.orders_conten)

track_id = response.json()["track"] # Сохранение трекера

def get_order_track(track): # Получаем заказ по трекеру
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_ORDER,
                        params={"t": track})