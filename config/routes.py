from .init import app, db, bcrypt
from .models import *
from .authform import *
from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user

#Authenticating user
@app.route('/register',methods=['GET','POST'])
def register_page():
    if current_user.is_authenticated:
        redirect(url_for('home'))
    form = RegisterForm()

    if form.validate_on_submit():
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(
            name = form.name.data,
            email = form.email.data,
            password_hash = password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form = form, title = 'Register')

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', form = form, title = 'Login')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# Routes
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


# add item
@app.route('/add', methods=['GET', 'POST'])
def add():
    # if a form is submitted
    if request.method == 'POST':
        name = request.form['name']
        item = Item(name=name)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('add'))
    # if a user is going to the page
    else:
        return render_template('add.html')

# view all items
@app.route('/view')
def view():
    items = Item.query.all()
    return render_template('view.html', items=items)

# delete item
@app.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('view'))

# update item
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Item.query.get_or_404(id)

    # if a form is submitted
    if request.method == 'POST':
        item.name = request.form['name']
        db.session.commit()
        return redirect(url_for('view'))
    # if a user is going to the page
    else:
        return render_template('update.html', item=item)

