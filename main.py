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
    return {'message': 'Welcome to Simple Geocoding Service'}


# Get all geocoded addresses
@app.get('/addresses')
def get_addresses():
    return db


# Geocode Address
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

# Get Address based on ID
@app.get('/addresses/{address_id}')
def get_address(address_id: int):
    results = db[address_id]
    return results

# Delete Address
@app.delete('/addresses/{address_id}')
def get_address(address_id: int):
    db.pop(address_id)
    return {}


# Check if address posted already existed
def findExistingAddress(new_address):
    result = {}
    for address in db:
        if address['postcode'] == new_address['postcode']:
            result = address
    return result
