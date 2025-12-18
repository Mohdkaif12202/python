from flask import Flask,redirect,render_template,request,session,flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from werkzeug.utils import secure_filename
from uuid import uuid4
import os

app = Flask(__name__, static_folder='static')
bcrypt = Bcrypt(app)

UPLOAD_FOLDER='static/upload'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///data.db"
db=SQLAlchemy(app)

app.secret_key="secret_key"

class User(db.Model):
    NAME = db.Column(db.String(100) , nullable = False)
    EMAIL = db.Column(db.String(200), unique = False)
    USERNAME = db.Column(db.String(200), primary_key = True)
    PASSWORD = db.Column(db.String(100), unique = True )
    PHOTO = db.Column(db.String(250))
with app.app_context(): 
    db.create_all()


@app.route('/',methods = ['GET' , 'POST'])
def home():
    if 'info' in session:
        return render_template("home.html")
    else:
        return render_template('/login0.html')


@app.route('/login',methods = ['GET' , 'POST'])
def login():
    if request.method =='POST':
        name = request.form["f_username"]
        password = request.form["f_password"]
        
        info = User.query.filter_by(USERNAME=name).first()
        if info and bcrypt.check_password_hash(info.PASSWORD,password):
                session['info']=info.USERNAME
                return redirect('/')
        return render_template("/login.html" ,error="invalid password and username")
    return render_template("login.html")

@app.route('/signup',methods = ['GET' , 'POST'])
def signup():
    if request.method=='POST':
        name =request.form['f_name']
        email =request.form['f_email']
        username =request.form['f_username']
        password = request.form['f_password']
        has_pass = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(
            NAME = name,
            EMAIL = email,
            USERNAME = username,
            PASSWORD= has_pass
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template("signup.html")

@app.route('/free_ride',methods = ['GET','POST'])
def free_ride():        
        username = session['info']
        INFO=User.query.filter_by(USERNAME=username).first()
        return render_template("free_ride.html", info = INFO)


@app.route('/profile' , methods = ['GET','POST'])
def profile():
     name=session['info']
     INFO = User.query.filter_by(USERNAME=name).first()
     return render_template("profile.html",info=INFO)

@app.route('/update', methods = ['GET','POST'])
def update():
     name=session['info']
     INFO= User.query.filter_by(USERNAME = name).first()
     if request.method == 'POST':
          email = request.form['email']
          temp = request.files['Image']
          password = request.form['password']

          if bcrypt.check_password_hash(INFO.PASSWORD,password):
            image_name = f"{uuid4().hex}_{secure_filename(temp.filename)}"
            INFO.PHOTO= image_name
            INFO.EMAIL= email
            db.session.add(INFO)
            db.session.commit()
            temp.save(os.path.join(app.config['UPLOAD_FOLDER'],image_name))
            return redirect("/profile")
          else:
            flash("Incorrect password", "danger")
            return redirect('/update')
                    
     return render_template('update.html',info=INFO)

                    

@app.route('/bill' , methods = ['GET','POST'])
def bill():
     name=session['info']
     INFO = User.query.filter_by(USERNAME=name).first()
     return render_template("bill.html",info=INFO)


@app.route('/contact' , methods = ['GET','POST'])
def contact():
     name=session['info']
     INFO = User.query.filter_by(USERNAME=name).first()
     return render_template("contact.html",info=INFO)


@app.route('/logout',methods = ['GET','POST'])
def logout():
    session.clear()
    return render_template("/login0.html")

if __name__ =="__main__":
    app.run(debug=True)
