from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def auserdelete():
    if request.method == 'POST' and 'username' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        lietotajvards = request.form['lietotajvards']
        cursor.execute("DELETE FROM lietotaji WHERE lietotajvards = %s", (lietotajvards, ))
        mysql.connection.commit()
        return redirect(url_for('auserpage'))
    return redirect(url_for('auserpage'))

def auseradd():
    if request.method == 'POST' and 'lietotajvards' in request.form and 'parole' in request.form and 'epasts' in request.form and 'telefona_numurs' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        lietotajvards = request.form['lietotajvards']
        parole = request.form['parole']
        epasts = request.form['epasts']
        telefonanumurs = request.form['telefona_numurs']
        cursor.execute("INSERT INTO lietotaji (lietotajvards, epasts, parole, telefona_numurs) VALUES (%s, %s, %s)", (lietotajvards, parole, epasts, telefonanumurs,))
        mysql.connection.commit()
        return redirect(url_for('auserpage'))
    return redirect(url_for('auserpage'))

def auseredit():
    if request.method == 'POST' and 'ID' in request.form and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        idforuser = request.form['idforuser']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor.execute("UPDATE accounts SET username = %s, password = %s, email = %s WHERE id = %s", (username, password, email, idforuser, ))
        mysql.connection.commit()
        return redirect(url_for('auserpage'))
    return redirect(url_for('auserpage'))