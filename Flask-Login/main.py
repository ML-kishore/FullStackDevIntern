from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = '8956rurjfu'  # Needed for session management

# MySQL Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'X9JXXXX'
app.config['MYSQL_DB'] = 'dbname'

mysql = MySQL(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect users to login if not authenticated


# User Model for Flask-Login
class User(UserMixin):
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password


# Load User from Database
@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    
    if user:
        return User(id=user[0], email=user[1], password=user[2])
    return None


# Home Page (Protected)
@app.route('/')
@login_required
def home():
    return f"Welcome, {current_user.email}! <a href='/logout'>Logout</a>"


# Register User
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
        mysql.connection.commit()
        cursor.close()

        flash("Registration Successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')


# Login User
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user[2], password):  # user[2] is the stored hashed password
            user_obj = User(id=user[0], email=user[1], password=user[2])
            login_user(user_obj)
            flash("Login Successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials!", "danger")

    return render_template('login.html')


# Logout User
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)


#Database Creation

#Step 1 : Open MySQL Workbench

#Step2 : Type this for creating database -> 'CREATE DATABASE FLASKAUTH;'

#Step3 : Use Database - > 'USE FLASKAUTH;'

#STEP4 : TABLE CREATION -> create table users(id int auto_increment primary key,email varchar(100) unique not null,password varchar(255) not null);

#STEP5 : RUN 'PYTHON APP.PY'
