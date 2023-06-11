from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def izdzest_kontaktus():
    if request.method == 'POST' and 'ID' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        ID = request.form['ID']
        cursor.execute("DELETE FROM kontakti WHERE ID = %s", (ID, ))
        mysql.connection.commit()
        return redirect(url_for('kontakti_saraksts'))
    return redirect(url_for('kontakti_saraksts'))

def pievienot_kontaktus():
    if request.method == 'POST' and 'virsraksts' in request.form and 'teksts' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        virsraksts = request.form['virsraksts']
        teksts = request.form['teksts']
        cursor.execute("INSERT INTO kontakti (lietotajvards, virsraksts, teksts) VALUES (%s, %s, %s)", (session['lietotajvards'], virsraksts, teksts,))
        mysql.connection.commit()
        return redirect(url_for('kontakti_saraksts'))
    return redirect(url_for('kontakti_saraksts'))

def rediget_kontaktus():
    if request.method == 'POST' and 'ID' in request.form and 'jaunais_virsraksts' in request.form and 'teksts' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        ID= request.form['ID']
        jaunais_virsraksts = request.form['jaunais_virsraksts']
        teksts= request.form['teksts']

        cursor.execute("SELECT * FROM kontakti WHERE ID = %s", (ID,))
        datubazes_dati = cursor.fetchone()

        if datubazes_dati:
            if jaunais_virsraksts:
                datubazes_dati['virsraksts'] = jaunais_virsraksts
            if teksts:
                datubazes_dati['teksts'] = teksts

            cursor.execute("UPDATE kontakti SET virsraksts = %s, teksts= %s WHERE ID = %s", (datubazes_dati['virsraksts'], datubazes_dati['teksts'], ID,))
            mysql.connection.commit()

        return redirect(url_for('kontakti_saraksts'))

    return redirect(url_for('kontakti_saraksts'))
