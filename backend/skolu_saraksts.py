from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def izdzest_skolas():
    if request.method == 'POST' and 'nosaukums' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        nosaukums = request.form['nosaukums']
        cursor.execute("DELETE FROM jasanasskolas WHERE nosaukums = %s", (nosaukums, ))
        mysql.connection.commit()
        return redirect(url_for('skolas_saraksts'))
    return redirect(url_for('skolas_saraksts'))

def pievienot_skolas():
    if request.method == 'POST' and 'nosaukums' in request.form and 'atrasanasvieta' in request.form and 'darbalaiks' in request.form and 'WEBadrese' in request.form  and 'telefonanumurs' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        nosaukums = request.form['nosaukums']
        atrasanasvieta = request.form['atrasanasvieta']
        darbalaiks = request.form['darbalaiks']
        WEBadrese = request.form['WEBadrese']
        telefonanumurs = request.form['telefonanumurs']
        cursor.execute("INSERT INTO jasanasskolas (nosaukums, atrasanasvieta, darbalaiks, WEBadrese, telefonanumurs) VALUES (%s, %s, %s, %s, %s)", (nosaukums, atrasanasvieta, darbalaiks, WEBadrese, telefonanumurs,))
        mysql.connection.commit()
        return redirect(url_for('skolas_saraksts'))
    return redirect(url_for('skolas_saraksts'))

def rediget_skolu():
    if request.method == 'POST' and 'nosaukums' in request.form and 'jaunais_nosaukums' in request.form and 'atrasanasvieta' in request.form and 'darbalaiks' in request.form and 'WEBadrese' in request.form and 'telefonanumurs' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        nosaukums = request.form['nosaukums']
        jaunais_nosaukums = request.form['jaunais_nosaukums']
        atrasanasvieta = request.form['atrasanasvieta']
        darbalaiks = request.form['darbalaiks']
        WEBadrese = request.form['WEBadrese']
        telefonanumurs = request.form['telefonanumurs']

        cursor.execute("SELECT * FROM jasanasskolas WHERE nosaukums = %s", (nosaukums,))
        datubazes_dati = cursor.fetchone()

        if datubazes_dati:
            if jaunais_nosaukums:
                datubazes_dati['nosaukums'] = jaunais_nosaukums
            if atrasanasvieta:
                datubazes_dati['atrasanasvieta'] = atrasanasvieta
            if darbalaiks:
                datubazes_dati['darbalaiks'] = darbalaiks
            if WEBadrese:
                datubazes_dati['WEBadrese'] = WEBadrese
            if telefonanumurs:
                datubazes_dati['telefonanumurs'] = telefonanumurs

            cursor.execute("UPDATE jasanasskolas SET nosaukums = %s, atrasanasvieta = %s, darbalaiks = %s, WEBadrese = %s, telefonanumurs = %s WHERE nosaukums = %s", (datubazes_dati['nosaukums'], datubazes_dati['atrasanasvieta'], datubazes_dati['darbalaiks'], datubazes_dati['WEBadrese'], datubazes_dati['telefonanumurs'], nosaukums,))
            mysql.connection.commit()

        return redirect(url_for('skolas_saraksts'))

    return redirect(url_for('skolas_saraksts'))
