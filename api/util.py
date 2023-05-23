from datetime import datetime
from dateutil.relativedelta import relativedelta

from config import db
from models import Vendor, Product, Order

import random
from faker import Faker


def build_or_refresh_db():
    db.drop_all()
    db.create_all()
    load_db()
    print("data refreshed!")


def load_db():
    company = Vendor(name='company01')
    db.session.add(company)
    db.session.flush()

    product_a = Product(title="prod02",
                          listing_type="type01", price=100, vendor_id=company.id)
    product_b = Product(
        title="prod01", listing_type="type02", price=500, vendor_id=company.id)

    db.session.add(product_a)
    db.session.add(product_b)
    db.session.flush()

    orders = []
    orders.append(Order(full_name="Isaac Asimov", order_date=datetime.now(
    ) - relativedelta(months=1), quantity=1, product_id=product_a.id))
    orders.append(Order(full_name="Ian M. Banks", order_date=datetime.now(
    ) - relativedelta(months=1), quantity=2, product_id=product_a.id))
    orders.append(Order(full_name="Ursula Le Guin", order_date=datetime.now(
    ) - relativedelta(months=4), quantity=4, product_id=product_a.id))
    orders.append(Order(full_name="Terry Pratchett", order_date=datetime.now(
    ) - relativedelta(months=4), quantity=1, product_id=product_a.id))
    orders.append(Order(full_name="Margaret Atwood", order_date=datetime.now(
    ) - relativedelta(months=3), quantity=1, product_id=product_b.id))
    orders.append(Order(full_name="Octavia E. Butler", order_date=datetime.now(
    ) - relativedelta(months=6), quantity=3, product_id=product_b.id))

    for order in orders:
        db.session.add(order)

    db.session.commit()


def build_large_db(num_orders, num_products):
    if (num_products < 1):
        raise ValueError("Number of products much be greater than 0")

    try:
        db.drop_all()
        db.create_all()
        large_load_db(num_orders, num_products)

    except Exception as e:
        print(e)
        db.session.rollback()
        raise e

    print("database re-built with {} random orders and {} random products.".format(num_orders, num_products))


def large_load_db(num_orders, num_products):
    fake = Faker()

    company = Vendor(name='company01')
    db.session.add(company)
    db.session.flush()
    orders, products = [], []
    for _ in range(num_products):
        products.append(Product(title=fake.name(),
                                listing_type="type01", price=random.randint(1, 1000), vendor_id=company.id))
    for product in products:
        db.session.add(product)

    db.session.flush()
    for _ in range(num_orders):
        orders.append(Order(full_name=fake.name(),
                            order_date=datetime.now() - relativedelta(months=random.randint(1, 6)),
                            quantity=random.randint(1, 100),
                            product_id=random.randint(1, num_products)
                            ))
    for order in orders:
        db.session.add(order)

    db.session.commit()
