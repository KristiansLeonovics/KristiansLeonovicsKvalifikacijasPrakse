from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def zirgu_pievienosana_sistemai():
    if 'loggedin' in session:
        if request.method == 'POST' and 'vards' in request.form and 'skirne' in request.form:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            vards = request.form['vards']
            skirne = request.form['skirne']
            cursor.execute('SELECT lietotajvards, epasts FROM lietotaji WHERE ID = %s', (session['ID'],))
            account = cursor.fetchone()
            cursor.execute("INSERT INTO zirgi (vards, skirne, lietotajsFK) VALUES (%s, %s, %s)", (vards, skirne, account['lietotajvards']))
            cursor.execute("SELECT * FROM zirgi WHERE lietotajsFK = %s", (account['lietotajvards'],))
            datubaze = cursor.fetchall()
            mysql.connection.commit()
            return render_template('profile.html',account=account, datubaze=datubaze, loggedin=session.get('loggedin', False))
    return redirect(url_for('login'))

def get_zirgu_saraksts():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT lietotajvards, epasts FROM lietotaji WHERE ID = %s', (session['ID'],))
        account = cursor.fetchone()
        cursor.execute("SELECT * FROM zirgi WHERE lietotajsFK = %s", (account['lietotajvards'],))
        datubaze = cursor.fetchall()
        return render_template('profile.html', account=account, datubaze = datubaze, loggedin=session.get('loggedin', False))
    else:
        return redirect('/login_jasana', loggedin=session.get('loggedin', False))