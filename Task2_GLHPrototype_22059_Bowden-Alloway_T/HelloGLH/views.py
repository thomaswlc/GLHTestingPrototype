from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from HelloGLH import app
from datetime import datetime
from models import DATABASE_URL, session, Producer, Product, User

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
@login_required
def market():
    return render_template("market.html", title="Markets")


@app.route('/products')
@login_required
def products():
    return render_template("products.html", title="Products")


@app.route('/about')
def about():
    return render_template("about.html", title="About Us")



@app.route('/signin', methods=['GET', 'POST'])
def signin():
    print("REQUEST METHOD:", request.method)

    if request.method == 'POST':
        print("FORM DATA:", request.form)

        username = request.form.get('username')
        password = request.form.get('password')

        print("USERNAME:", username)
        print("PASSWORD:", password)

    return render_template("signin.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password'] 

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

            print("User added:", username)

    return render_template("register.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))