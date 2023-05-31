from flask import Flask, render_template, request, url_for, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

mysql = MySQL()

def izdzest_sacensibas():
    if request.method == 'POST' and 'nosaukums' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        nosaukums = request.form['nosaukums']
        cursor.execute("DELETE FROM sacensibas WHERE nosaukums = %s", (nosaukums, ))
        mysql.connection.commit()
        return redirect(url_for('sacensibas_saraksts'))
    return redirect(url_for('sacensibas_saraksts'))

def pievienot_sacensibas():
    if request.method == 'POST' and 'nosaukums' in request.form and 'atrasanasvieta' in request.form  and 'datums_sakums' in request.form and 'datums_beigas' in request.form and 'jasanas_norises_vieta' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        nosaukums = request.form['nosaukums']
        atrasanasvieta = request.form['atrasanasvieta']
        datums_sakums = request.form['datums_sakums']
        datums_beigas = request.form['datums_beigas']
        jasanas_norises_vieta = request.form['jasanas_norises_vieta']
        cursor.execute("INSERT INTO sacensibas (nosaukums, atrasanas_vieta, datums_sakums, datums_beigas, jasanas_norises_vieta) VALUES (%s, %s, %s, %s, %s)", (nosaukums, atrasanasvieta, datums_sakums, datums_beigas, jasanas_norises_vieta,))
        mysql.connection.commit()
        return redirect(url_for('sacensibas_saraksts'))
    return redirect(url_for('sacensibas_saraksts'))

def rediget_sacensibas():
    if request.method == 'POST' and 'nosaukums' in request.form and 'jaunais_nosaukums' in request.form and 'atrasanasvieta' in request.form and 'datums_sakums' in request.form and 'datums_beigas' in request.form and 'jasanas_norises_vieta' in request.form:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        nosaukums = request.form['nosaukums']
        jaunais_nosaukums = request.form['jaunais_nosaukums']
        atrasanasvieta = request.form['atrasanasvieta']
        datums_sakums = request.form['datums_sakums']
        datums_beigas = request.form['datums_beigas']
        jasanas_norises_vieta = request.form['jasanas_norises_vieta']

        cursor.execute("SELECT * FROM sacensibas WHERE nosaukums = %s", (nosaukums,))
        datubazes_dati = cursor.fetchone()

        if datubazes_dati:
            if jaunais_nosaukums:
                datubazes_dati['nosaukums'] = jaunais_nosaukums
            if atrasanasvieta:
                datubazes_dati['atrasanas_vieta'] = atrasanasvieta
            if datums_sakums:
                datubazes_dati['datums_sakums'] = datums_sakums
            if datums_beigas:
                datubazes_dati['datums_beigas'] = datums_beigas
            if jasanas_norises_vieta:
                datubazes_dati['jasanas_norises_vieta'] = jasanas_norises_vieta

            cursor.execute("UPDATE sacensibas SET nosaukums = %s, atrasanas_vieta = %s, datums_sakums = %s, datums_beigas = %s, jasanas_norises_vieta = %s WHERE nosaukums = %s", (datubazes_dati['nosaukums'], datubazes_dati['atrasanas_vieta'], datubazes_dati['datums_sakums'], datubazes_dati['datums_beigas'], datubazes_dati['jasanas_norises_vieta'], nosaukums,))
            mysql.connection.commit()

        return redirect(url_for('sacensibas_saraksts'))

    return redirect(url_for('sacensibas_saraksts'))
