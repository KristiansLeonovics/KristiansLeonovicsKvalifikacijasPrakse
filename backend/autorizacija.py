from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def login_jasana():
    msg = ''
    loggedin = False
    is_admin = False
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
            loggedin = True

            if account['lietotajvards'] == 'adminlietotajs' and account['parole'] == 'adminparole123':
                is_admin = True
                return render_template('/admin/amainpage.html',is_admin=is_admin, loggedin=loggedin)
            else:
                return render_template('mainpage.html', loggedin=loggedin)
        else:
            msg = 'Nepareizi ievadīts lietotājvārds vai parole!'

    return render_template('/login.html', msg=msg)


def atslegsanas_no_sistemas(loggedin = True):
   session.pop('loggedin', None)
   session.pop('ID', None)
   session.pop('lietotajvards', None)
   session.pop('parole', None)
   return redirect(url_for('home'))
