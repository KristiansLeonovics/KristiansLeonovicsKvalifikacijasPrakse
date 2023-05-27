from flask import Flask, render_template, request, url_for, session, redirect, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
from datetime import datetime

mysql = MySQL()

def get_events():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM sacensibas") 
    rows = cursor.fetchall()
    sacensibas = []

    for row in rows:
        sacensiba = {
            'nosaukums': row['nosaukums'],
            'atrasanas_vieta': row['atrasanas_vieta'],
            'datums_sakums': row['datums_sakums'],
            'datums_beigas': row['datums_beigas'],
        }
        sacensibas.append(sacensiba)

    return render_template('sacensibas.html', sacensibas=sacensibas, competition_type='latvija', loggedin=session.get('loggedin', False))

