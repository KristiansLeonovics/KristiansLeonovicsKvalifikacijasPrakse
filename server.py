from flask import Flask, render_template, send_from_directory, request, url_for, session, redirect, Response
from flask_socketio import SocketIO
from flask_mysqldb import MySQL
import MySQLdb.cursors

from autorizacija import login_jasana
from register import register_jasana

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['SECRET_KEY'] = 'asdg GR ARTG AERYH AGVBsde  et Tty WEYwy4YE54Y67 5Yy'
socketio = SocketIO(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kartupeliarsipoliem12'
app.config['MYSQL_DB'] = 'jasanassistema'

mysql = MySQL(app)
@app.route('/')
def home():
    return render_template('mainpage.html')

@app.route('/skola')
def skolas():
    return render_template('skolas.html')

@app.route('/kaleji')
def kaleji():
    return render_template('kaleji.html')

@app.route('/veikali')
def veikali():
    return render_template('veikali.html')

@app.route('/arsti')
def arsti():
    return render_template('arsti.html')

@app.route('/autorizacija', methods=['GET', 'POST'])
def login():
    return login_jasana()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_jasana()

if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0", port=80, debug=True)