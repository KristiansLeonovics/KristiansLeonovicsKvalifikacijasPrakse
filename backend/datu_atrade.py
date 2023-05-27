from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

mysql = MySQL()


def skolas():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM jasanasskolas") 
    db = cursor.fetchall()
    
    if request.method == 'POST':
        search = request.form.get('search')
        location = request.form.get('location')
        
        if search or location:
            filtered_skolas = []
            for skola in db:
                if (search and search.lower() in skola['nosaukums'].lower()) or (location and location.lower() in skola['atrasanasvieta'].lower()):
                    filtered_skolas.append(skola)
            skolaslist = filtered_skolas
        else:
            skolaslist = db
    else:
        skolaslist = db
    return render_template("skolas.html", skolaslist=skolaslist, loggedin=session.get('loggedin', False))

def veikali():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM veikali") 
    db = cursor.fetchall()
    
    if request.method == 'POST':
        search = request.form.get('search')
        location = request.form.get('location')
        
        if search or location:
            filtered_veikali = []
            for veikali in db:
                if (search and search.lower() in veikali['nosaukums'].lower()) or (location and location.lower() in veikali['atrasanasvieta'].lower()):
                    filtered_veikali.append(veikali)
            veikalilist = filtered_veikali
        else:
            veikalilist = db
    else:
        veikalilist = db
    return render_template("veikali.html", veikalilist=veikalilist, loggedin=session.get('loggedin', False))

def pakavu_kaleji():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM pakavu_kaleji") 
    db = cursor.fetchall()
    
    if request.method == 'POST':
        search = request.form.get('search')
        location = request.form.get('location')
        
        if search or location:
            filtered_pakavu_kaleji = []
            for pakavu_kaleji in db:
                if (search and search.lower() in pakavu_kaleji['nosaukums'].lower()) or (location and location.lower() in pakavu_kaleji['atrasanasvieta'].lower()):
                    filtered_pakavu_kaleji.append(pakavu_kaleji)
            pakavu_kaleji_list = filtered_pakavu_kaleji
        else:
            pakavu_kaleji_list = db
    else:
        pakavu_kaleji_list = db
    return render_template("pakavu_kaleji.html", pakavu_kaleji_list=pakavu_kaleji_list, loggedin=session.get('loggedin', False))

def zirgu_veterinararsti():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM zirgu_veterinararsti") 
    db = cursor.fetchall()
    
    if request.method == 'POST':
        search = request.form.get('search')
        location = request.form.get('location')
        
        if search or location:
            filtered_zirgu_veterinararsti = []
            for zirgu_veterinararsti in db:
                if (search and search.lower() in zirgu_veterinararsti['nosaukums'].lower()) or (location and location.lower() in zirgu_veterinararsti['atrasanasvieta'].lower()):
                    filtered_zirgu_veterinararsti.append(zirgu_veterinararsti)
            zirgu_veterinararsti_list = filtered_zirgu_veterinararsti
        else:
            zirgu_veterinararsti_list = db
    else:
        zirgu_veterinararsti_list = db
    return render_template("zirgu_veterinararsti.html", zirgu_veterinararsti_list=zirgu_veterinararsti_list, loggedin=session.get('loggedin', False))