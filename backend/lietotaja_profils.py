from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def profils():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT lietotajvards, epasts FROM lietotaji WHERE ID = %s', (session['ID'],))
        account = cursor.fetchone()
        return render_template('profile.html', account=account, loggedin=session.get('loggedin', False))
    return redirect(url_for('login'))