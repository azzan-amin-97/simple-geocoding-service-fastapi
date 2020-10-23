from fastapi import FastAPI
from pydantic import BaseModel
import pgeocode

app = FastAPI()

db = []


class Address(BaseModel):
    address: str
    town: str
    postcode: str
    country: str


@app.get('/')
def index():
    return {'msg': 'Welcome to Simple Geocoding Service'}


@app.get('/addresses')
def get_addresses():
    return db


@app.post('/geocode')
def geocode_address(address: Address):
    nomi = pgeocode.Nominatim(address.country)
    place = nomi.query_postal_code(address.postcode)
    obj = address.dict()
    existing_address = findExistingAddress(obj)
    if existing_address:
        results = existing_address
    else:
        obj['latitude'] = place.latitude
        obj['longitude'] = place.longitude
        results = obj
        db.append(results)

    return results


@app.get('/addresses/{address_id}')
def get_address(address_id: int):
    results = db[address_id]
    return results


@app.delete('/addresses/{address_id}')
def get_address(address_id: int):
    db.pop(address_id)
    return {}


# Models
def findExistingAddress(new_address):
    result = {}
    for address in db:
        if address['postcode'] == new_address['postcode']:
            result = address
    return result
