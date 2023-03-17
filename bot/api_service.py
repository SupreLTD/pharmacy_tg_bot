import requests
import json

API_URL = 'http://localhost:3001'


def search(query):
    resp = requests.get('{0}/search?query={1}'.format(API_URL, query))
    return json.loads(resp.content)


def search_by_words(words):
    resp = requests.get('{0}/searchByWords?words={1}'.format(API_URL, '|'.join(words)))
    return json.loads(resp.content)


def find_pharmacies(lat, lon):
    resp = requests.get('{0}/findPharmacies?lat={1}&lon={2}'.format(API_URL, lat, lon))
    return json.loads(resp.content)


def add_to_basket(user_id, product_id):
    resp = requests.post('{0}/addToBasket?user_id={1}&product_id={2}'.format(API_URL, user_id, product_id))
    return resp.content


def get_basket(user_id):
    resp = requests.get('{0}/getBasket?user_id={1}'.format(API_URL, user_id))
    return json.loads(resp.content)


def remove_from_basket(user_id, product_id):
    requests.post('{0}/removeFromBasket?user_id={1}&product_id={2}'.format(API_URL, user_id, product_id))


def make_order(user_id):
    requests.post('{0}/makeOrder?user_id={1}'.format(API_URL, user_id))