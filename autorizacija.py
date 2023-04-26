from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def login_jasana():
    msg = ''
    if request.method == 'POST' and 'lietotajvards' in request.form and 'parole' in request.form:
        username = request.form['lietotajvards']
        password = request.form['parole']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM lietotaji WHERE lietotajvards = %s AND parole = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['ID'] = account['ID']
            session['lietotajvards'] = account['lietotajvards']
            return render_template('mainpage.html')
        else:
            msg = 'Nepareizi ievadīts lietotājvārds vai parole!'
    return render_template('/login.html', msg=msg)

