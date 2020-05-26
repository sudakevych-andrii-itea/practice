from flask import Flask, render_template, request
from sqlite_context_manager import SQLite
from admin import Admin

app = Flask(__name__)

model_structures = {
    'category': ['category_id', 'category_name'],
    'product': ['product_id', 'product_name',
                'price', 'in_sale', 'in_stock',
                'description', 'product_url', 'category_id']
}


def get_categories():
    with SQLite('store.db') as cur:
        cur.execute("SELECT * FROM category")
        return [dict(zip(model_structures['category'], values)) for values in cur.fetchall()]


def get_category_id(category_name):
    with SQLite('store.db') as cur:
        cur.execute("SELECT category_id FROM category WHERE category_name = ?", (category_name,))
        return cur.fetchone()


def get_products(category_id):
    with SQLite('store.db') as cur:
        cur.execute("SELECT * FROM product WHERE category_id = ?", (category_id,))
        return [dict(zip(model_structures['product'], values)) for values in cur.fetchall()]


def get_product(product_url):
    with SQLite('store.db') as cur:
        cur.execute("SELECT * FROM product WHERE product_url=?", (product_url,))
        return dict(zip(model_structures['product'], cur.fetchone()))


@app.route('/')
def index():
    return render_template('index.html', categories=get_categories())


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    administrator = Admin()
    if request.method == 'POST':
        if 'add-category' in request.form:
            administrator.add_category(request.form.get('category_name'))
        elif 'add-product' in request.form:
            administrator.add_product(request.form.get('product-name'),
                                      request.form.get('price'),
                                      request.form.get('in-sale'),
                                      request.form.get('in-stock'),
                                      request.form.get('category-id'),
                                      request.form.get('description'),
                                      request.form.get('product-url'))
    return render_template('admin.html', categories=get_categories())


@app.route('/<category_name>')
def category(category_name):
    return render_template('category.html',
                           category_name=category_name,
                           products=get_products(*get_category_id(category_name)))


@app.route('/<category_name>/<product_name>')
def product(category_name, product_name):
    return render_template('product.html', category_name=category_name, product=get_product(product_name))


if __name__ == '__main__':
    app.run(debug=True)
