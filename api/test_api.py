import requests
import math

from config import app, db
from util import build_or_refresh_db, build_large_db

def test_get_products():
    build_or_refresh_db

    response = requests.get('http://localhost:5001/api/products')
    data = response.json()
    assert len(data['products']) == 2


def test_get_product():
    build_or_refresh_db

    response = requests.get('http://localhost:5001/api/product?productId=1')
    data = response.json()
    assert len(data['orders']) == 4
    assert data['product']['id'] == 1


def test_get_revenue():
    build_or_refresh_db
    expectedTotalRevenue = 1400
    expectedProductRevenue = 400

    response = requests.get('http://localhost:5001/api/total-revenue')
    data = response.json()
    assert data['total'] == expectedTotalRevenue

    response = requests.get('http://localhost:5001/api/product?productId=1')
    data = response.json()
    assert data['revenue']['total'] == expectedProductRevenue


def test_pagination():
    dbLoad = 100
    elementsPerPage = 20
    build_large_db(dbLoad, dbLoad)

    response = requests.get('http://localhost:5001/api/products')
    data = response.json()
    assert data['totalPages'] == (math.ceil(dbLoad / elementsPerPage))
