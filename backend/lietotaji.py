from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def izdzest_lietotaju():
    if request.method == 'POST' and 'lietotajvards' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        lietotajvards = request.form['lietotajvards']
        cursor.execute("DELETE FROM lietotaji WHERE lietotajvards = %s", (lietotajvards, ))
        mysql.connection.commit()
        return redirect(url_for('lietotaju_saraksts'))
    return redirect(url_for('lietotaju_saraksts'))

def pievienot_lietotaju():
    if request.method == 'POST' and 'lietotajvards' in request.form and 'parole' in request.form and 'epasts' in request.form and 'telefona_numurs' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        lietotajvards = request.form['lietotajvards']
        parole = request.form['parole']
        epasts = request.form['epasts']
        telefonanumurs = request.form['telefona_numurs']
        cursor.execute("INSERT INTO lietotaji (lietotajvards, epasts, parole, telefona_numurs) VALUES (%s, %s, %s, %s)", (lietotajvards, parole, epasts, telefonanumurs,))
        mysql.connection.commit()
        return redirect(url_for('lietotaju_saraksts'))
    return redirect(url_for('lietotaju_saraksts'))

def rediget_lietotaju():
    if request.method == 'POST' and 'lietotajvards' in request.form and 'jaunais_lietotajvards' in request.form and 'parole' in request.form and 'epasts' in request.form and 'telefona_numurs' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        lietotajvards = request.form['lietotajvards']
        jaunais_lietotajvards = request.form['jaunais_lietotajvards']
        parole = request.form['parole']
        epasts = request.form['epasts']
        telefona_numurs = request.form['telefona_numurs']

        cursor.execute("SELECT * FROM lietotaji WHERE lietotajvards = %s", (lietotajvards,))
        datubazes_dati = cursor.fetchone()

        if datubazes_dati:
            if jaunais_lietotajvards:
                datubazes_dati['lietotajvards'] = jaunais_lietotajvards
            if parole:
                datubazes_dati['parole'] = parole
            if epasts:
                datubazes_dati['epasts'] = epasts
            if telefona_numurs:
                datubazes_dati['telefona_numurs'] = telefona_numurs

            cursor.execute("UPDATE lietotaji SET lietotajvards = %s, parole = %s, epasts = %s, telefona_numurs = %s WHERE lietotajvards = %s", (datubazes_dati['lietotajvards'], datubazes_dati['parole'], datubazes_dati['epasts'], datubazes_dati['telefona_numurs'], lietotajvards,))
            mysql.connection.commit()

        return redirect(url_for('lietotaju_saraksts'))

    return redirect(url_for('lietotaju_saraksts'))

