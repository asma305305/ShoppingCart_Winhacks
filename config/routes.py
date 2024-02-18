from init import app, db
from flask import render_template,redirect,url_for
from models import item,user
from auth import RegisterForm


#Registering user.
@app.route('/register',methods=['GET','POST'])
def register_page():
    form= RegisterForm()

    if form.validate_on_submit():
        user=User(
            username=form.username.data,
            email=form.email.data,
            password_hash=form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('market_page'))
    
    if form.errors != {}:
        for i in form.errors.values():
            print(i)
    return render_template('register.html',form=form)

# home
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

