from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def pievienot_kontakti():
    if request.method == 'POST' and 'virsraksts' in request.form and 'teksts' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        virsraksts = request.form['virsraksts']
        teksts = request.form['teksts']
        cursor.execute("INSERT INTO kontakti (lietotajvards, virsraksts, teksts) VALUES (%s, %s, %s)", (session['lietotajvards'], virsraksts, teksts,))
        mysql.connection.commit()
        return render_template('/kontakti.html', loggedin = session.get('loggedin', False))
    return render_template('/kontakti.html', loggedin = session.get('loggedin', False))