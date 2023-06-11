from flask import Flask, render_template, send_from_directory, request, url_for, session, redirect, Response
from flask_socketio import SocketIO
from flask_mysqldb import MySQL
import MySQLdb.cursors

import backend.autorizacija as autorizacija
import backend.lietotaja_profils as lietotaja_profils
import backend.lietotaji as lietotaji
import backend.datu_atrade as datu_atrade
import backend.PDF as PDF
import backend.skolu_saraksts as skolu_saraksts
import backend.sacensibu_saraksts as sacensibu_saraksts
import backend.pakavu_kaleji_saraksts as pakavu_kaleji_saraksts
import backend.zirgu_veterinararsti_saraksts as zirgu_veterinararsti_saraksts
import backend.veikali_saraksts as veikali_saraksts
import backend.jaunumi_saraksts as jaunumi_saraksts
import backend.zirgu_pievienosana as zirgu_pievienosana
import backend.personalizets_grafiks as grafiks
import backend.kontakti as kontakti
import backend.kontaktu_saraksts as kontaktu_saraksts
from backend.register import register_jasana

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
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM jaunumi") 
    db = cursor.fetchall()
    return render_template('mainpage.html', jaunumilist = db, loggedin=session.get('loggedin', False))

@app.route('/skola', methods=['GET', 'POST'])
def skolas():
    return datu_atrade.skolas()

@app.route('/kaleji', methods=['GET', 'POST'])
def kaleji():
    return datu_atrade.pakavu_kaleji()

@app.route('/kontakti', methods=['GET', 'POST'])
def lietotajs_kontakti():
    return kontakti.pievienot_kontakti()

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

@app.route('/personalizets_grafiks', methods=['GET', 'POST'])
def personalizets_grafiks():
    if 'loggedin' in session:
        return grafiks.calendar()
    else:
        return autorizacija.login_jasana()

@app.route('/zirgu_pievienosana', methods=['GET', 'POST'])
def pievienosana():
    return zirgu_pievienosana.zirgu_pievienosana_sistemai()

@app.route('/get_horses', methods=['GET'])
def horses():
    return grafiks.get_horses()

@app.route('/get_hospitals', methods=['GET'])
def hospitals():
    return grafiks.get_hospitals()

@app.route('/get_skolas', methods=['GET'])
def skolas_personalizets_grafiks():
    return grafiks.get_skolas()

@app.route('/get_pakavu_kaleji', methods=['GET'])
def pakavu_kaleji_personalizets_grafiks():
    return grafiks.get_pakavu_kaleji()

@app.route('/get_sacensibas', methods=['GET'])
def sacensibas_personalizets_grafiks():
    return grafiks.get_sacensibas()

@app.route('/deleteEvent', methods=['POST'])
def delete_personalizets_grafiks():
    return grafiks.delete_event()

@app.route('/save_appointment_horses', methods=['POST'])
def save_appointment_horse():
    return grafiks.save_appointment_horses()

@app.route('/save_appointment_skolas', methods=['POST'])
def save_appointment_skola():
    return grafiks.save_appointment_skolas()

@app.route('/save_appointment_sacensibas', methods=['POST'])
def save_appointment_sacensiba():
    return grafiks.save_appointment_sacensibas()

@app.route('/save_appointment_pakavu_kaleji', methods=['POST'])
def save_appointment_pakavu_kalejs():
    return grafiks.save_appointment_pakavu_kaleji()


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'loggedin' in session:
        return zirgu_pievienosana.get_zirgu_saraksts()
    else:
        return autorizacija.login_jasana()

@app.route('/sacensibas')
def sacensibas():
    location = request.args.get('location', '')
    if location == 'Latvija':
        query = "SELECT * FROM sacensibas WHERE jasanas_norises_vieta = 'Latvija'"
    elif location == 'Ārzemes':
        query = "SELECT * FROM sacensibas WHERE jasanas_norises_vieta = 'Ārzemes'"
    else:
        query = "SELECT * FROM sacensibas"

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    return render_template('sacensibas.html', sacensibas=results, loggedin = session.get('loggedin', False))

@app.route('/amainpage')
def amainpage():
    if session['lietotajvards'] == 'adminlietotajs' and session['parole'] == 'adminparole123':
        loggedin = True
        is_admin = True
        return render_template('/admin/amainpage.html', loggedin=loggedin, is_admin=is_admin)

# Lietotāju funkcijas
@app.route('/lietotaju_saraksts', methods=['GET', 'POST'])
def lietotaju_saraksts():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM lietotaji") 
        datubaze = cursor.fetchall()
        return render_template('/admin/lietotaju_saraksts.html', datubaze = datubaze, loggedin=session.get('loggedin', False))
    else:
        return autorizacija.login_jasana()

@app.route('/lietotaji_labot', methods=['GET', 'POST'])
def lietotaji_labot():
    if session['lietotajvards'] == 'adminlietotajs':
        return lietotaji.rediget_lietotaju()
    else:
        return autorizacija.login_jasana()

@app.route('/lietotaji_pievienot', methods=['GET', 'POST'])
def lietotaji_pievienot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return lietotaji.pievienot_lietotaju()
    else:
        return autorizacija.login_jasana()
    
@app.route('/lietotaji_dzest', methods=['GET', 'POST'])
def lietotaji_dzest():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return lietotaji.izdzest_lietotaju()
    else:
        return autorizacija.login_jasana()

# Skolu funkcijas
@app.route('/skolas_saraksts', methods=['GET', 'POST'])
def skolas_saraksts():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM jasanasskolas") 
        datubaze = cursor.fetchall()
        return render_template('/admin/skolas_saraksts.html', datubaze = datubaze, loggedin=session.get('loggedin', False))
    else:
        return autorizacija.login_jasana()

@app.route('/skolas_labot', methods=['GET', 'POST'])
def skolas_labot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return skolu_saraksts.rediget_skolu()
    else:
        return autorizacija.login_jasana()
    
@app.route('/skolas_pievienot', methods=['GET', 'POST'])
def skolas_pievienot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return skolu_saraksts.pievienot_skolas()
    else:
        return autorizacija.login_jasana()
    
@app.route('/skolas_dzest', methods=['GET', 'POST'])
def skolas_dzest():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return skolu_saraksts.izdzest_skolas()
    else:
        return autorizacija.login_jasana()

#Pakavu kalēju funkcijas
@app.route('/pakavu_kaleji_saraksts', methods=['GET', 'POST'])
def pakavu_kaleju_saraksts():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM pakavu_kaleji") 
        datubaze = cursor.fetchall()
        return render_template('/admin/pakavu_kaleji_saraksts.html', datubaze = datubaze, loggedin=session.get('loggedin', False))
    else:
        return autorizacija.login_jasana()

@app.route('/pakavu_kaleji_labot', methods=['GET', 'POST'])
def pakavu_kaleji_labot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return pakavu_kaleji_saraksts.rediget_pakavu_kaleji()
    else:
        return autorizacija.login_jasana()
    
@app.route('/pakavu_kaleji_pievienot', methods=['GET', 'POST'])
def pakavu_kaleji_pievienot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return pakavu_kaleji_saraksts.pievienot_pakavu_kalejus()
    else:
        return autorizacija.login_jasana()
    
@app.route('/pakavu_kaleji_dzest', methods=['GET', 'POST'])
def pakavu_kaleji_dzest():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return pakavu_kaleji_saraksts.izdzest_pakavu_kalejus()
    else:
        return autorizacija.login_jasana()


#Zirgu veterinārārstu funkcijas
@app.route('/zirgu_veterinararstu_saraksts', methods=['GET', 'POST'])
def zirgu_veterinararstu_saraksts():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM zirgu_veterinararsti") 
        datubaze = cursor.fetchall()
        return render_template('admin/zirgu_veterinararsti_saraksts.html', datubaze = datubaze, loggedin=session.get('loggedin', False))
    else:
        return autorizacija.login_jasana()

@app.route('/zirgu_veterinararsti_labot', methods=['GET', 'POST'])
def zirgu_veterinararsti_labot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return zirgu_veterinararsti_saraksts.rediget_zirgu_veterinararstus()
    else:
        return autorizacija.login_jasana()
    
@app.route('/zirgu_veterinararsti_pievienot', methods=['GET', 'POST'])
def zirgu_veterinararsti_pievienot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return zirgu_veterinararsti_saraksts.pievienot_zirgu_veterinararstus()
    else:
        return autorizacija.login_jasana()
    
@app.route('/zirgu_veterinararsti_dzest', methods=['GET', 'POST'])
def zirgu_veterinararsti_dzest():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return zirgu_veterinararsti_saraksts.izdzest_zirgu_veterinararstus()
    else:
        return autorizacija.login_jasana()


#Veikalu funkcijas
@app.route('/veikalu_saraksts', methods=['GET', 'POST'])
def veikalu_saraksts():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM veikali") 
        datubaze = cursor.fetchall()
        return render_template('/admin/veikalu_saraksts.html', datubaze = datubaze, loggedin=session.get('loggedin', False))
    else:
        return autorizacija.login_jasana()

@app.route('/veikali_labot', methods=['GET', 'POST'])
def veikali_labot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return veikali_saraksts.rediget_veikali()
    else:
        return autorizacija.login_jasana()
    
@app.route('/veikali_pievienot', methods=['GET', 'POST'])
def veikali_pievienot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return veikali_saraksts.pievienot_veikalus()
    else:
        return autorizacija.login_jasana()
    
@app.route('/veikali_dzest', methods=['GET', 'POST'])
def veikali_dzest():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return veikali_saraksts.izdzest_veikalus()
    else:
        return autorizacija.login_jasana()

#Jāšanas sacensību funkcijas

@app.route('/sacensibu_saraksts', methods=['GET', 'POST'])
def sacensibas_saraksts():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM sacensibas") 
        datubaze = cursor.fetchall()
        return render_template('/admin/sacensibu_saraksts.html', datubaze=datubaze, loggedin=session.get('loggedin', False))
    else:
        return autorizacija.login_jasana()

@app.route('/sacensibas_labot', methods=['GET', 'POST'])
def sacensibas_labot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return sacensibu_saraksts.rediget_sacensibas()
    else:
        return autorizacija.login_jasana()

@app.route('/sacensibas_pievienot', methods=['GET', 'POST'])
def sacensibas_pievienot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return sacensibu_saraksts.pievienot_sacensibas()
    else:
        return autorizacija.login_jasana()

@app.route('/sacensibas_dzest', methods=['GET', 'POST'])
def sacensibas_dzest():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return sacensibu_saraksts.izdzest_sacensibas()
    else:
        return autorizacija.login_jasana()
    
# Jaunumu funkcijas
@app.route('/jaunumu_saraksts', methods=['GET', 'POST'])
def jaunumu_saraksts():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM jaunumi") 
        datubaze = cursor.fetchall()
        return render_template('/admin/jaunumu_saraksts.html', datubaze = datubaze, loggedin=session.get('loggedin', False))
    else:
        return autorizacija.login_jasana()

@app.route('/jaunumi_labot', methods=['GET', 'POST'])
def jaunumi_labot():
    if session['lietotajvards'] == 'adminlietotajs':
        return jaunumi_saraksts.rediget_jaunumi()
    else:
        return autorizacija.login_jasana()

@app.route('/jaunumi_pievienot', methods=['GET', 'POST'])
def jaunumi_pievienot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return jaunumi_saraksts.pievienot_jaunumus()
    else:
        return autorizacija.login_jasana()
    
@app.route('/jaunumi_dzest', methods=['GET', 'POST'])
def jaunumi_dzest():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return jaunumi_saraksts.izdzest_jaunumus()
    else:
        return autorizacija.login_jasana()
    
#Kontaktu funkcijas
@app.route('/kontakti_saraksts', methods=['GET', 'POST'])
def kontakti_saraksts():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM kontakti") 
        datubaze = cursor.fetchall()
        return render_template('/admin/kontakti_saraksts.html', datubaze = datubaze, loggedin=session.get('loggedin', False))
    else:
        return autorizacija.login_jasana()

@app.route('/kontakti_labot', methods=['GET', 'POST'])
def kontakti_labot():
    if session['lietotajvards'] == 'adminlietotajs':
        return kontaktu_saraksts.rediget_kontaktus()
    else:
        return autorizacija.login_jasana()

@app.route('/kontakti_pievienot', methods=['GET', 'POST'])
def kontakti_pievienot():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return kontaktu_saraksts.pievienot_kontaktus()
    else:
        return autorizacija.login_jasana()
    
@app.route('/kontakti_dzest', methods=['GET', 'POST'])
def kontakti_dzest():
    if 'lietotajvards' in session and session['lietotajvards'] == 'adminlietotajs':
        return kontaktu_saraksts.izdzest_kontaktus()
    else:
        return autorizacija.login_jasana()


@app.route('/PDF_lietotaji')
def PDF_dokuments_lietotaji():
    return PDF.PDF_dokuments_lietotaji()

@app.route('/PDF_skolas')
def PDF_dokuments_skolas():
    return PDF.PDF_dokuments_skolas()

@app.route('/PDF_veikali')
def PDF_dokuments_veikali():
    return PDF.PDF_dokuments_veikali()

@app.route('/PDF_pakavu_kaleji')
def PDF_dokuments_pakavu_kaleji():
    return PDF.PDF_dokuments_pakavu_kaleji()

@app.route('/PDF_zirgu_veterinararsti')
def PDF_dokuments_zirgu_veterinararsti():
    return PDF.PDF_dokuments_zirgu_veterinarsti()

@app.route('/PDF_sacensibas')
def PDF_dokuments_sacensibas():
    return PDF.PDF_dokuments_sacensibas()

@app.route('/PDF_jaunumi')
def PDF_dokuments_jaunums():
    return PDF.PDF_dokuments_jaunumi()

@app.route('/PDF_personalizets_grafiks_lietotaji')
def PDF_personalizets_grafiks_lietotaji():
    return PDF.PDF_dokuments_personalizets_grafiks()

@app.route('/PDF_kontakti')
def PDF_kontakti():
    return PDF.PDF_dokuments_kontakti()

@app.route('/PDF_sacensibas_lietotaji', methods=['GET', 'POST'])
def PDF_sacensibas_lietotaji():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM sacensibas")
    events = cursor.fetchall()
    mysql.connection.commit()
    pdf_buffer = PDF.sacensibas_lietotajiem(events)
    return Response(pdf_buffer, mimetype='application/pdf')


if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0", port=80, debug=True)