from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

mysql = MySQL()

def register_jasana():
    msg = ''
    if request.method == 'POST' and 'lietotajvards' in request.form and 'parole' in request.form and 'epasts' in request.form and 'telefona_numurs' in request.form:
        username = request.form['lietotajvards']
        password = request.form['parole']
        email = request.form['epasts']
        telefona_numurs = request.form['telefona_numurs']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM lietotaji WHERE lietotajvards = %s OR epasts = %s OR telefona_numurs = %s', (username, email, telefona_numurs,))
        account = cursor.fetchone()
        if account:
            msg = 'Izvēlētais konts jau eksistē!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Nepareizi ievadīta e-pasta adrese!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Lietotājvārdā izmantojiet tikai burtus un ciparus!'
        elif not username or not password or not email or not telefona_numurs:
            msg = 'Lūdzu aizpildiet visus laukus!'
        else:
            cursor.execute('INSERT INTO lietotaji VALUES (NULL, %s, %s, %s, %s)', (username, email, password, telefona_numurs,))
            mysql.connection.commit()
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Lūdzu aizpildiet visus laikus!'
    return render_template('/register.html', msg=msg)