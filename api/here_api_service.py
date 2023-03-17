import requests
import json

TOKEN = ""


def find_pharmacies(lat, lon):
    url = "https://discover.search.hereapi.com/v1/discover?in=circle:{0},{1};r=500&q=pharmacies&apiKey={2}".format(lat, lon, TOKEN)
    resp = requests.get(url)
    data = json.loads(resp.content)

    return list(map(lambda x: (x['title'], '{0}, {1}'.format(x['address']['street'], x['address']['city']), x['distance']), data['items']))


def get_coords(address):
    url = "https://geocode.search.hereapi.com/v1/geocode?q={0}&apiKey={1}".format(address, TOKEN)
    resp = requests.get(url)
    data = json.loads(resp.content)

    return data['items'][0]['position']
