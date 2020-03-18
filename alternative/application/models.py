from application import db, login
from sqlalchemy.sql import exists 
from flask_login import UserMixin

belongs = db.Table('belongs', 
    db.Column('pID', db.Integer, db.ForeignKey('Products.pID'), primary_key=True),
    db.Column('c_name', db.String(30), db.ForeignKey('Categories.c_name'), primary_key=True)
)   

class Includes(db.Model):
    __tablename__='includes'
    oID = db.Column(db.Integer, db.ForeignKey('Orders.oID'), primary_key=True)
    pID = db.Column(db.Integer, db.ForeignKey('Products.pID'), primary_key=True)
    quan = db.Column(db.Integer)
    order_includes = db.relationship('Orders', backref = db.backref('including', lazy='dynamic'))
    included_products = db.relationship('Products', backref = db.backref('included', lazy='dynamic'))

class Users(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.String(20), primary_key=True)
    u_password = db.Column(db.String(200))
    city = db.Column(db.String(20))
    country = db.Column(db.String(20))
    address = db.Column(db.String(50))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    u_role = db.Column(db.String(10))
    user_orders = db.relationship('Orders', backref='orders_users')

class Orders(db.Model):
    __tablename__ = 'Orders'
    oID = db.Column(db.Integer, primary_key=True)
    num_products = db.Column(db.Integer)
    order_date = db.Column(db.String(20))
    culm_price = db.Column(db.Integer)
    user = db.Column(db.String(20), db.ForeignKey('Users.id'))


class Products(db.Model):
    __tablename__ = 'Products'
    pID = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(50))
    supplier = db.Column(db.String(50))
    prod_quan = db.Column(db.Integer)
    price = db.Column(db.Integer)
    rel_year = db.Column(db.String(10))
    isbn = db.Column(db.String(20))
    image = db.Column(db.String(50))
    p_status = db.Column(db.String(10))
    p_description = db.Column(db.Text(400))

    
class Categories(db.Model):
    __tablename__ = 'Categories'
    c_name = db.Column(db.String(30), primary_key=True)
    cat_products = db.relationship('Products', secondary=belongs, backref=db.backref('products_cat', lazy='dynamic'))


db.create_all()

prod_exists = Products.query.first()
cat_exists = Categories.query.first()

if cat_exists is None:
    category = Categories(c_name='Electronics')
    db.session.add(category)
    category = Categories(c_name='Home')
    db.session.add(category)
    category = Categories(c_name='Car')
    db.session.add(category)
    category = Categories(c_name='Fashion')
    db.session.add(category)
    category = Categories(c_name='Sports')
    db.session.add(category)
    category = Categories(c_name='Media')
    db.session.add(category)
    db.session.commit()

if prod_exists is None:
    cats = tuple(Categories.query.all())
    elec, home, car, fash, sport, media = cats
    product = Products(p_name='Lenovo Thinkpad', supplier='Lenovo', prod_quan=100, price=899, rel_year='2018', isbn='437563952-0',
    image='thinkpad.png', p_status='new', p_description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    db.session.add(product)
    elec.cat_products.append(product)
    product = Products(p_name='PlayStation 4', supplier='Sony', prod_quan=250, price=1199, rel_year='2014', isbn='717523992-0',
    image='ps4.png', p_status='new', p_description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    db.session.add(product)
    elec.cat_products.append(product)
    home.cat_products.append(product)
    product = Products(p_name='Wilson Tennis Racket', supplier='Wilson', prod_quan=150, price=399, rel_year='2015', isbn='617563452-0',
    image='tennis.png', p_status='new', p_description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    db.session.add(product)
    sport.cat_products.append(product)
    product = Products(p_name='Green T-Shirt Men', supplier='Nike', prod_quan=500, price=199, rel_year='2019', isbn='237569342-0',
    image='tshirt.png', p_status='new', p_description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    db.session.add(product)
    fash.cat_products.append(product)
    sport.cat_products.append(product)
    product = Products(p_name="Legend of Zelda Link's Awakening", supplier='Nintendo', prod_quan=150, price=299, rel_year='2019', isbn='833523971-0',
    image='zelda.png', p_status='new', p_description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    db.session.add(product)
    media.cat_products.append(product)
    product = Products(p_name='"Electric Screwdriver', supplier='Bosch', prod_quan=250, price=799, rel_year='2016', isbn='943523921-0',
    image='drill.png', p_status='new', p_description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    db.session.add(product)
    elec.cat_products.append(product)
    home.cat_products.append(product)
    db.session.commit()



@login.user_loader
def load_user(id): 
    return Users.query.get(id)

    
 