from flask import Flask, render_template, send_from_directory, request, url_for, session, redirect, Response
from flask_socketio import SocketIO
from flask_mysqldb import MySQL
import MySQLdb.cursors

import autorizacija
import lietotaja_profils
import lietotaji
import datu_atrade
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

@app.route('/skola', methods=['GET', 'POST'])
def skolas():
    return datu_atrade.skolas()

@app.route('/kaleji', methods=['GET', 'POST'])
def kaleji():
    return datu_atrade.pakavu_kaleji()

@app.route('/veikali', methods=['GET', 'POST'])
def veikali():
    return datu_atrade.veikali()

@app.route('/arsti', methods=['GET', 'POST'])
def arsti():
    return datu_atrade.zirgu_veterinararsti()

@app.route('/website/<string:website>')
def website(website):
    return redirect('http://' + website)

@app.route('/autorizacija', methods=['GET', 'POST'])
def login():
    return autorizacija.login_jasana()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_jasana()

@app.route('/logout')
def logout():
    return autorizacija.atslegsanas_no_sistemas(loggedin = False)

@app.route('/profile')
def profile():
    return lietotaja_profils.atslegsanas_no_sistemas()

@app.route('/sacensibas')
def sacensibas():
    return render_template('sacensibas.html')

if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0", port=80, debug=True)