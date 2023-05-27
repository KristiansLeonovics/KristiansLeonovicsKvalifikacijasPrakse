from flask import Flask, render_template, request, url_for, session, redirect, Response
from flask_mysqldb import MySQL
from fpdf import FPDF
import MySQLdb.cursors

mysql = MySQL()

def PDF_dokuments_lietotaji():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM lietotaji")
    result = cursor.fetchall()

    # Generate PDF
    pdf = FPDF()
    pdf.add_font('Arial', '', 'backend/arialuni.ttf', uni=True)
    pdf.add_page()
    pdf.set_font('Arial', '', 16)

    pdf.cell(0, 10, 'Lietotaju dati', ln=True, align='C')
    pdf.ln()

    col_widths = [30, 40, 40, 50]

    pdf.set_font('Arial', '', 12)
    pdf.cell(col_widths[0], 10, 'ID', border=1)
    pdf.cell(col_widths[1], 10, 'Vārds', border=1)
    pdf.cell(col_widths[2], 10, 'Parole', border=1)
    pdf.cell(col_widths[3], 10, 'E-pasts', border=1)
    pdf.ln()

    pdf.set_font('Arial', '', 12)
    for row in result:
        pdf.cell(col_widths[0], 10, str(row['ID']), border=1)
        pdf.cell(col_widths[1], 10, row['lietotajvards'], border=1)
        pdf.cell(col_widths[2], 10, row['parole'], border=1)
        pdf.cell(col_widths[3], 10, row['epasts'], border=1)
        pdf.ln()

    output = pdf.output(dest='S')

    return Response(output, mimetype='application/pdf')

def PDF_dokuments_skolas():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM jasanasskolas")
    result = cursor.fetchall()

    pdf = FPDF(orientation='L')
    pdf.add_page()

    page_width = pdf.w - 2 * pdf.l_margin

    pdf.add_font('Arial', '', 'backend/arialuni.ttf', uni=True)

    pdf.set_font('Arial', 'B', 14.0)
    pdf.cell(page_width, 0.0, 'Skolu dati', align='C')
    pdf.ln(10)

    pdf.set_font('Arial', '', 12)

    col_width = page_width / 6

    pdf.ln(1)

    th = pdf.font_size

    for row in result:
        pdf.cell(col_width, th, str(row['ID']), border=1)
        pdf.cell(col_width, th, row['nosaukums'], border=1)
        pdf.cell(col_width, th, row['atrasanasvieta'], border=1)
        pdf.cell(col_width, th, row['darbalaiks'], border=1)
        pdf.cell(col_width, th, row['WEBadrese'], border=1)
        pdf.cell(col_width, th, row['telefonanumurs'], border=1)
        pdf.ln(th)

    pdf.ln(10)

    pdf.set_font('Arial', '', 10.0)
    pdf.cell(page_width, 0.0, '- end of report -', align='C')

    return Response(
        pdf.output(dest='S'),
        mimetype='application/pdf',
        headers={'Content-Disposition': 'attachment;filename=skolas.pdf'}
    )