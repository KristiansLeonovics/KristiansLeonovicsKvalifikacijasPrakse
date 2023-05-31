from flask import Flask, render_template, request, url_for, session, redirect, jsonify, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def calendar():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM lietotaju_darbibas WHERE lietotajsFK = %s", (session['lietotajvards'],))
    events = cursor.fetchall()
    mysql.connection.commit()
    return render_template('/personalizets_grafiks.html', events=events, loggedin = session.get('loggedin', False))

def get_horses():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT lietotajvards, epasts FROM lietotaji WHERE ID = %s', (session['ID'],))
    account = cursor.fetchone()
    cursor.execute("SELECT * FROM zirgi WHERE lietotajsFK = %s", (account['lietotajvards'],))
    horse = cursor.fetchall()
    mysql.connection.commit()
    return jsonify(horse)

def get_hospitals():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM zirgu_veterinararsti")
    hospital = cursor.fetchall()
    mysql.connection.commit()
    return jsonify(hospital)

def get_skolas():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM jasanasskolas")
    school = cursor.fetchall()
    mysql.connection.commit()
    return jsonify(school)

def get_sacensibas():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM sacensibas")
    sacensiba = cursor.fetchall()
    mysql.connection.commit()
    return jsonify(sacensiba)

def get_pakavu_kaleji():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM pakavu_kaleji")
    pakavu_kaleji = cursor.fetchall()
    mysql.connection.commit()
    return jsonify(pakavu_kaleji)

def save_appointment_horses():
    data = request.get_json()
    nosaukums = data['appointmentName']
    dateStart = data['appointmentStartDate']
    dateEnd = data['appointmentEndDate']
    darbibas_veids = data['darbibas_veids']
    horselietotajsFK = session['lietotajvards']
    iestade = data['iestade']
    ieraksts = data['ieraksts']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO lietotaju_darbibas (nosaukums, datums_sakums, datums_beigas, darbibas_veids, lietotajsFK, iestade, ieraksts) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (nosaukums, dateStart, dateEnd, darbibas_veids, horselietotajsFK, iestade, ieraksts))
    mysql.connection.commit()

    return jsonify({'message': 'Appointment saved successfully!'})

def save_appointment_skolas():
    data = request.get_json()
    nosaukums = data['trainingName']
    dateStart = data['trainingStartDate']
    dateEnd = data['trainingEndDate']
    darbibas_veids = data['darbibas_veids']
    horselietotajsFK = session['lietotajvards']
    iestade = data['iestade']
    ieraksts = data['ieraksts']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO lietotaju_darbibas (nosaukums, datums_sakums, datums_beigas, darbibas_veids, lietotajsFK, iestade, ieraksts) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (nosaukums, dateStart, dateEnd, darbibas_veids, horselietotajsFK, iestade, ieraksts))
    mysql.connection.commit()

    return jsonify({'message': 'Appointment saved successfully!'})


def save_appointment_sacensibas():
    data = request.get_json()
    cursor = mysql.connection.cursor()
    iestade = data['iestade']
    cursor.execute("SELECT datums_sakums, datums_beigas FROM sacensibas WHERE nosaukums = %s", [iestade])
    result = cursor.fetchone()
    datums_sakums = result[0]
    datums_beigas = result[1]
    nosaukums = data['lietotajanosaukums']
    darbibas_veids = data['darbibas_veids']
    horselietotajsFK = session['lietotajvards']
    ieraksts = data['ieraksts']

    cursor.execute("INSERT INTO lietotaju_darbibas (nosaukums, datums_sakums, datums_beigas, darbibas_veids, lietotajsFK, iestade, ieraksts) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (nosaukums, datums_sakums, datums_beigas, darbibas_veids, horselietotajsFK, iestade, ieraksts))
    mysql.connection.commit()

    return jsonify({'message': 'Appointment saved successfully!'})


def save_appointment_pakavu_kaleji():
    data = request.get_json()
    nosaukums = data['pakavu_kalejinosaukums']
    dateStart = data['pakavu_kalejiStartDate']
    dateEnd = data['pakavu_kalejiEndDate']
    darbibas_veids = data['darbibas_veids']
    horselietotajsFK = session['lietotajvards']
    iestade = data['iestade']
    ieraksts = data['ieraksts']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO lietotaju_darbibas (nosaukums, datums_sakums, datums_beigas, darbibas_veids, lietotajsFK, iestade, ieraksts) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (nosaukums, dateStart, dateEnd, darbibas_veids, horselietotajsFK, iestade, ieraksts))
    mysql.connection.commit()

    return jsonify({'message': 'Appointment saved successfully!'})

def deleteevent():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    data = request.get_json()
    eventid = data['eventid']
    cursor.execute("DELETE FROM lietotaju_darbibas WHERE ID = %s", [eventid])
    mysql.connection.commit()
    return jsonify({'message': 'Event deleted successfully'})
