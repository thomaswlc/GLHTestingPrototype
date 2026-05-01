from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from HelloGLH import app, login_manager
from datetime import datetime
from models import DATABASE_URL, session, Producer, Product, User

@login_manager.user_loader
def load_user(user_id):
    return session.get(User, int(user_id))
@app.route('/')
@app.route('/home')
def home():
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
    products = [
        {"name": "Sourdough Bread", "category": "Baked Goods", "price": 3.50},
        {"name": "Cheddar Cheese", "category": "Dairy", "price": 4.00},
        {"name": "Milk", "category": "Dairy", "price": 1.50},
        {"name": "Apples", "category": "Fruit & Veg", "price": 2.00},
        {"name": "Carrots", "category": "Fruit & Veg", "price": 1.20},
        {"name": "Croissant", "category": "Baked Goods", "price": 2.20},
        {"name": "Chocolate Croissant", "category": "Baked Goods", "price": 2.30},
        {"name": "Potatoes", "category": "Fruit & Veg", "price": 1.10},
        {"name": "Banana", "category": "Fruit & Veg", "price": 1.00},
        {"name": "Orange", "category": "Fruit & Veg", "price": 2.20},
        {"name": "Cream", "category": "Dairy", "price": 2.20},
        {"name": "Butter", "category": "Dairy", "price": 2.20},
        {"name": "Baguette", "category": "Baked Goods", "price": 2.20},

    ]

    # Get filter + sort from URL
    category = request.args.get('category')
    sort = request.args.get('sort')

    # Filter
    if category:
        products = [p for p in products if p["category"] == category]

    # Sort
    if sort == "price_asc":
        products = sorted(products, key=lambda x: x["price"])
    elif sort == "price_desc":
        products = sorted(products, key=lambda x: x["price"], reverse=True)
    elif sort == "name":
        products = sorted(products, key=lambda x: x["name"])

    return render_template("products.html", products=products)

@app.route('/about')
def about():
    return render_template("about.html", title="About Us")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = session.query(User).filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password")
            return redirect(url_for('signin'))

    return render_template("signin.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        if not email:
            flash("Email is required")
            return redirect(url_for('register'))
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Check passwords match
        if password != confirm_password:
            flash("Passwords do not match")
            return redirect(url_for('register'))

        # Check if user already exists
        existing_user = session.query(User).filter_by(username=username).first()

        if existing_user:
            flash("Username already taken")
            return redirect(url_for('register'))

        # Hash password
        hashed_pw = generate_password_hash(password)

        # Create user
        new_user = User(
            username=username,
            email=email,
            password_hash=hashed_pw
        )
        try:
            session.add(new_user)
            session.commit()
        except Exception as e:
            print("ERROR:", e)
            session.rollback() 
            flash("An error occurred while creating your account. Please try again.")
            return redirect(url_for('signin'))

    return render_template("register.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))