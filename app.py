from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

bakery_products = [
    Product("Bread", 2.5, 100),
    Product("Cake", 20, 20),
    Product("Jilapi", 1.5, 50),
]

@app.route('/')
def index():
    return render_template('index.html', products=bakery_products)

@app.route('/sale/<product_name>', methods=['POST'])
def make_sale(product_name):
    quantity = int(request.form['quantity'])

    for product in bakery_products:
        if product.name == product_name:
            if product.quantity >= quantity:
                product.quantity -= quantity

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
