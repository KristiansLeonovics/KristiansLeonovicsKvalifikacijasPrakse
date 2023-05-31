from flask import Flask, Response
from io import BytesIO
from flask_mysqldb import MySQL
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from unidecode import unidecode
import datetime
import MySQLdb.cursors

mysql = MySQL()

def PDF_dokuments_lietotaji():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM lietotaji")
    data = cursor.fetchall()

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Arial', 'backend/arialuni.ttf'))
    document = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["ID", "Lietotājvārds", "E-pasts", "Parole", "Telefona numurs"]]

    for row in data:
        paragraph_cells = []
        for cell in row:
            if isinstance(cell, str):
                cell = unidecode(cell)
                paragraph_cells.append(Paragraph(cell, getSampleStyleSheet()['Normal']))
            else:
                paragraph_cells.append(Paragraph(str(cell), getSampleStyleSheet()['Normal']))
        table_data.append(paragraph_cells)

    table = Table(table_data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements = []
    header_text = "SIA \"Horsify\" Lietotaju Dati"
    header_paragraph = Paragraph(header_text, getSampleStyleSheet()['Heading1'])
    elements.append(header_paragraph)

    creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
    creation_date_style = getSampleStyleSheet()['Normal']
    creation_date_style.alignment = 2
    creation_date_paragraph = Paragraph(f"Documents Tika Izveidots: {creation_date}", creation_date_style)
    elements.append(creation_date_paragraph)

    elements.append(Spacer(1, 12))

    elements.append(table)
    elements.append(Spacer(1, 24))
    end_text = "PDF dokumenta noslegums"
    end_text_style = getSampleStyleSheet()['Normal']
    end_text_style.alignment = 1
    end_text_paragraph = Paragraph(end_text, end_text_style)
    elements.append(end_text_paragraph)

    document.build(elements)

    buffer.seek(0)

    return Response(buffer.getvalue(), mimetype='application/pdf')

def PDF_dokuments_skolas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM jasanasskolas")
    data = cursor.fetchall()

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Arial', 'backend/arialuni.ttf'))
    document = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["ID", "nosaukums", "atrasanasvieta", "darbalaiks", "WEBadrese", "telefonanumurs"]]

    for row in data:
        paragraph_cells = []
        for cell in row:
            if isinstance(cell, str):
                cell = unidecode(cell)
                paragraph_cells.append(Paragraph(cell, getSampleStyleSheet()['Normal']))
            else:
                paragraph_cells.append(Paragraph(str(cell), getSampleStyleSheet()['Normal']))
        table_data.append(paragraph_cells)

    table = Table(table_data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements = []
    header_text = "SIA \"Horsify\" Skolu Dati"
    header_paragraph = Paragraph(header_text, getSampleStyleSheet()['Heading1'])
    elements.append(header_paragraph)

    creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
    creation_date_style = getSampleStyleSheet()['Normal']
    creation_date_style.alignment = 2
    creation_date_paragraph = Paragraph(f"Documents Tika Izveidots: {creation_date}", creation_date_style)
    elements.append(creation_date_paragraph)

    elements.append(Spacer(1, 12))

    elements.append(table)
    elements.append(Spacer(1, 24))
    end_text = "PDF dokumenta noslegums"
    end_text_style = getSampleStyleSheet()['Normal']
    end_text_style.alignment = 1
    end_text_paragraph = Paragraph(end_text, end_text_style)
    elements.append(end_text_paragraph)

    document.build(elements)

    buffer.seek(0)

    return Response(buffer.getvalue(), mimetype='application/pdf')


def PDF_dokuments_veikali():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM veikali")
    data = cursor.fetchall()

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Arial', 'backend/arialuni.ttf'))
    document = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["ID", "Nosaukums", "Atrašanās vieta", "Darba Laiks", "WEBadrese", "Telefona Numurs"]]

    for row in data:
        paragraph_cells = []
        for cell in row:
            if isinstance(cell, str):
                cell = unidecode(cell)
                paragraph_cells.append(Paragraph(cell, getSampleStyleSheet()['Normal']))
            else:
                paragraph_cells.append(Paragraph(str(cell), getSampleStyleSheet()['Normal']))
        table_data.append(paragraph_cells)

    table = Table(table_data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements = []
    header_text = "SIA \"Horsify\" Veikalu Dati"
    header_paragraph = Paragraph(header_text, getSampleStyleSheet()['Heading1'])
    elements.append(header_paragraph)

    creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
    creation_date_style = getSampleStyleSheet()['Normal']
    creation_date_style.alignment = 2
    creation_date_paragraph = Paragraph(f"Documents Tika Izveidots: {creation_date}", creation_date_style)
    elements.append(creation_date_paragraph)

    elements.append(Spacer(1, 12))

    elements.append(table)
    elements.append(Spacer(1, 24))
    end_text = "PDF dokumenta noslegums"
    end_text_style = getSampleStyleSheet()['Normal']
    end_text_style.alignment = 1
    end_text_paragraph = Paragraph(end_text, end_text_style)
    elements.append(end_text_paragraph)

    document.build(elements)

    buffer.seek(0)

    return Response(buffer.getvalue(), mimetype='application/pdf')


def PDF_dokuments_pakavu_kaleji():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM pakavu_kaleji")
    data = cursor.fetchall()

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Arial', 'backend/arialuni.ttf'))
    document = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["ID", "Nosaukums", "Atrašanās vieta", "Darba Laiks", "WEBadrese", "Telefona Numurs"]]

    for row in data:
        paragraph_cells = []
        for cell in row:
            if isinstance(cell, str):
                cell = unidecode(cell)
                paragraph_cells.append(Paragraph(cell, getSampleStyleSheet()['Normal']))
            else:
                paragraph_cells.append(Paragraph(str(cell), getSampleStyleSheet()['Normal']))
        table_data.append(paragraph_cells)

    table = Table(table_data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements = []
    header_text = "SIA \"Horsify\" Pakavu Kaleju dati"
    header_paragraph = Paragraph(header_text, getSampleStyleSheet()['Heading1'])
    elements.append(header_paragraph)

    creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
    creation_date_style = getSampleStyleSheet()['Normal']
    creation_date_style.alignment = 2
    creation_date_paragraph = Paragraph(f"Documents Tika Izveidots: {creation_date}", creation_date_style)
    elements.append(creation_date_paragraph)

    elements.append(Spacer(1, 12))

    elements.append(table)
    elements.append(Spacer(1, 24))
    end_text = "PDF dokumenta noslegums"
    end_text_style = getSampleStyleSheet()['Normal']
    end_text_style.alignment = 1
    end_text_paragraph = Paragraph(end_text, end_text_style)
    elements.append(end_text_paragraph)

    document.build(elements)

    buffer.seek(0)

    return Response(buffer.getvalue(), mimetype='application/pdf')

def PDF_dokuments_zirgu_veterinarsti():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM zirgu_veterinararsti")
    data = cursor.fetchall()

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Arial', 'backend/arialuni.ttf'))
    document = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["ID", "Nosaukums", "Atrašanās Vieta", "Darba Laiks", "WEBadrese", "Telefona Numurs"]]

    for row in data:
        paragraph_cells = []
        for cell in row:
            if isinstance(cell, str):
                cell = unidecode(cell)
                paragraph_cells.append(Paragraph(cell, getSampleStyleSheet()['Normal']))
            else:
                paragraph_cells.append(Paragraph(str(cell), getSampleStyleSheet()['Normal']))
        table_data.append(paragraph_cells)

    table = Table(table_data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements = []
    header_text = "SIA \"Horsify\" Zirgu Veterinararstu Dati"
    header_paragraph = Paragraph(header_text, getSampleStyleSheet()['Heading1'])
    elements.append(header_paragraph)

    creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
    creation_date_style = getSampleStyleSheet()['Normal']
    creation_date_style.alignment = 2
    creation_date_paragraph = Paragraph(f"Documents Tika Izveidots: {creation_date}", creation_date_style)
    elements.append(creation_date_paragraph)

    elements.append(Spacer(1, 12))

    elements.append(table)
    elements.append(Spacer(1, 24))
    end_text = "PDF dokumenta noslegums"
    end_text_style = getSampleStyleSheet()['Normal']
    end_text_style.alignment = 1
    end_text_paragraph = Paragraph(end_text, end_text_style)
    elements.append(end_text_paragraph)

    document.build(elements)

    buffer.seek(0)

    return Response(buffer.getvalue(), mimetype='application/pdf')

def PDF_dokuments_sacensibas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM sacensibas")
    data = cursor.fetchall()

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Arial', 'backend/arialuni.ttf'))
    document = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["ID", "Nosaukums", "Atrašanās Vieta", "Sākuma Datums", "Beigu Datums", "Norises Vieta"]]

    for row in data:
        paragraph_cells = []
        for cell in row:
            if isinstance(cell, str):
                cell = unidecode(cell)
                paragraph_cells.append(Paragraph(cell, getSampleStyleSheet()['Normal']))
            else:
                paragraph_cells.append(Paragraph(str(cell), getSampleStyleSheet()['Normal']))
        table_data.append(paragraph_cells)

    table = Table(table_data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements = []
    header_text = "SIA \"Horsify\" Sacensibu dati"
    header_paragraph = Paragraph(header_text, getSampleStyleSheet()['Heading1'])
    elements.append(header_paragraph)

    creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
    creation_date_style = getSampleStyleSheet()['Normal']
    creation_date_style.alignment = 2
    creation_date_paragraph = Paragraph(f"Documents Tika Izveidots: {creation_date}", creation_date_style)
    elements.append(creation_date_paragraph)

    elements.append(Spacer(1, 12))

    elements.append(table)
    elements.append(Spacer(1, 24))
    end_text = "PDF dokumenta noslegums"
    end_text_style = getSampleStyleSheet()['Normal']
    end_text_style.alignment = 1
    end_text_paragraph = Paragraph(end_text, end_text_style)
    elements.append(end_text_paragraph)

    document.build(elements)

    buffer.seek(0)

    return Response(buffer.getvalue(), mimetype='application/pdf')