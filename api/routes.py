from config import app
from flask import request
from models import Order, Product

@app.route('/test')
def hello_world():
    return "hello world"


@app.route('/api/products')
def get_products():
    page = request.args.get('page', 1, type=int)
    paginatedProducts = Product.query.paginate(page, per_page=20)
    return {
        'products': [product.serialize for product in paginatedProducts.items],
        'currentPage': paginatedProducts.page,
        'totalPages': paginatedProducts.pages
    }


@app.route('/api/product')
def get_product():
    page = request.args.get('page', 1, type=int)
    productId = request.args.get('productId')
    if not productId:
        raise ValueError("No product id given")

    product = Product.query.get(productId)
    paginatedOrders = Order.query.filter(
        Order.product_id == productId).paginate(page, per_page=20)
    totalRevenue = get_revenue(product.id)

    return {
        'product': product.serialize,
        'orders': [order.serialize for order in paginatedOrders.items],
        'currentPage': paginatedOrders.page,
        'totalPages': paginatedOrders.pages,
        "revenue": totalRevenue
    }


@app.route('/api/total-revenue')
def get_revenue(productId=None):
    productId = request.args.get('productId', productId, type=int)
    if productId:
        products = Product.query.filter(Product.id == productId)
    else:
        products = Product.query.all()
    totalRevenue = 0
    for product in products:
        orders = Order.query.filter(Order.product_id == product.id)
        totalRevenue += orders.count() * product.price
    return {
        'total': totalRevenue
    }
