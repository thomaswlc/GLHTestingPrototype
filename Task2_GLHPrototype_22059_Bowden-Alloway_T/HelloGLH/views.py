from flask import render_template
from HelloGLH import app
from datetime import datetime
from models import session, Producer, Product


@app.route('/')
@app.route('/home')
def home():
    producers = session.query(Producer).all()
    products = session.query(Product).all()

    producers = [
        {
            "name": "John Smith",
            "profession": "Vegetable Farmer",
            "story": "Growing organic vegetables for 20 years."
        },
        {
            "name": "Sarah Green",
            "profession": "Dairy Producer",
            "story": "Family-run dairy farm with fresh milk."
        },
        {
            "name": "Tom Baker",
            "profession": "Baker",
            "story": "Artisan bread made daily."
        },
        {
            "name": "Emma Fields",
            "profession": "Fruit Grower",
            "story": "Seasonal fruits grown locally."
        }

    ]

    return render_template(
        "index.html",
        title="Home",
        producers=producers,
        products=products
    )

@app.route('/market')
def market():
    return render_template("market.html", title="Markets")


@app.route('/products')
def products():
    return render_template("products.html", title="Products")


@app.route('/about')
def about():
    return render_template("about.html", title="About Us")


@app.route('/signin')
def signin():
    return render_template("signin.html", title="Sign In")
