from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import here_api_service, search as elastic_search, repository, basket

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/extendSearch')
async def extendSearch(query):
    drugs = elastic_search.find_drugs(query, 7)
    for i in drugs:
        p = repository.get_pharmacy(i['id'])
        p_address = p["address"]
        coords = here_api_service.get_coords(p_address)
        i["lat"] = coords['lat']
        i["lon"] = coords['lng']
        i["address"] = p["address"]

    return drugs



@app.get('/search')
async def search(query):
    return elastic_search.find_drugs(query)


@app.get('/searchByWords')
async def search_by_words(words):
    query = elastic_search.get_query_from_words(words.split('|'))
    return elastic_search.find_drugs(query)


@app.get('/findPharmacies')
async def find_pharmacies(lat, lon):
    return here_api_service.find_pharmacies(lat, lon)


@app.post('/addToBasket')
async def add_to_basket(user_id, product_id):
    return basket.add(user_id, product_id)


@app.post('/removeFromBasket')
async def remove_from_basket(user_id, product_id):
    basket.remove(user_id, product_id)


@app.get('/getBasket')
async def get_basket(user_id):
    return basket.get_basket(user_id)


@app.post('/makeOrder')
async def make_order(user_id):
    basket.make_order(user_id)


uvicorn.run(app, host="0.0.0.0", port=3001)
