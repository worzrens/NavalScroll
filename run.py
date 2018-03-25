#!/usr/bin/env python
from flask import Flask, render_template, request, abort, redirect,url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required, RoleMixin, UserMixin, utils,roles_required
from flask.ext.admin import Admin
from flask_login import LoginManager, current_user,login_user, logout_user
from database import db,roles_users, User ,Role,UserAdmin,RoleAdmin, init_db
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import datetime
import MySQLdb


app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

"""
Login managment

"""
db1 = MySQLdb.connect(host="localhost", user="q", passwd="1", db="NavalScroll")
db.init_app(app)

login = LoginManager(app)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

def __str__(self):
    return self.name

@app.before_first_request
def before_first_request():
    db.create_all()
    
def __hash__(self):
    return hash(self.name)





"""

    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='end-user', description='End user')
    
    #encrypted_password = utils.encrypt_password('password')
    
    if not user_datastore.get_user('someone@example.com'):
        user_datastore.create_user(email='someone@example.com', password=123)
    if not user_datastore.get_user('admin@example.com'):
        user_datastore.create_user(email='admin@example.com', password=1234)
    db.session.commit()
    user_datastore.add_role_to_user('someone@example.com', 'end-user')
    user_datastore.add_role_to_user('admin@example.com', 'admin')
    db.session.commit()
"""

admin = Admin(app)
admin.add_view(UserAdmin(User, db.session))
admin.add_view(RoleAdmin(Role, db.session))

 

class Form(Form):
    name = TextField('ID:')
    email = TextField('Email:')
    password = TextField('Password:')
 
    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)
        


"""
ROUTES
"""

@app.route('/')
@login_required
def show_main():
    return "Тишина"

@app.route('/button')
@login_required
def show_button():
    return render_template('button.html');

@app.route('/button2')
@roles_required('admin')
def show_button2():
    return render_template('button2.html');

@app.route("/register", methods=['POST','GET'])
def reg():
    form = Form(request.form)
    if request.method == 'POST':
        fid=request.form['id']
        fpassword=request.form['password']
        femail=request.form['email']        
        if form.validate():
            cur = db1.cursor()
            cur.execute("INSERT INTO user(id,email,password,active,cofirmed_at,roles) VALUES (%s,%s,%s,%s,%s,%s)",(fid,femail,set_password(fpassword),1,datetime.datetime.now(),'user')) 
            db1.commit()
            flash('Thanks for registration ' + femail)
        elif len(femail)<1:
            flash('Error: Too short email')
        elif (len(fid)<1)or(len(fpassword)<1):
            flash('Error: All the form fields are required. ')
    return render_template('register.html', form=form)


@app.route('/log', methods=['GET', 'POST'])
def log():
    if current_user.is_authenticated:
        return redirect(url_for('view'))
    form=Form(request.form)
    error=None
    if request.method == 'POST' and form.validate():
        femail = request.form['email']
        password=request.form['password']
        user = User.query.filter_by(email=femail).first()
        if user is None or not user.check_password(password):
            error = 'Invalid username or password.'
            flash(error)
            return redirect(url_for('log'))
        print(user)
        login_user(user)
        return redirect(url_for('view'))
    return render_template('login.html', error=error, form=form)

"""
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('/'))
"""
@app.route('/add', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        cursor = db1.cursor()
        try:
            if 1==1:#session.get('user'):
                _ID = request.form['inputID']
                _description = request.form['inputDescription']
                #_user = session.get('user')
                cursor.execute("INSERT INTO posts(body,user_id) VALUES (%s,%s)",(_description,_ID)) 
                db1.commit()
                data = cursor.fetchall()
 
                if len(data) is 0:
                    db1.commit()
                    flash('Added')
                    return redirect('/add')
                else:
                    return "error"#render_template('error.html',error = 'An error occurred!')
 
            #else:
                #return render_template('error.html',error = 'Unauthorized Access')
        except Exception as e:
            return e#render_template('error.html',error = str(e))
        finally:
            cursor.close()
    return render_template('add.html')



@app.route('/posts')       
def posts():
    try:
        cursor = db1.cursor()
        #cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'posts';") 
        #data_names = cursor.fetchall()
        data_names = ['№','Body','Time','User']
        cursor.execute("SELECT * FROM posts;")
        data = cursor.fetchall()
        return render_template("posts.html",data_names=data_names, data=data)

    except Exception as e:
        return (str(e))





if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=int('5000'),
        debug=app.config['DEBUG']
    )