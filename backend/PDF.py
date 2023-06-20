from flask import Response, session
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
import locale

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

def PDF_dokuments_jaunumi():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM jaunumi")
    data = cursor.fetchall()

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Arial', 'backend/arialuni.ttf'))
    document = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["ID", "Virsraksts", "Teksts"]]

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
    header_text = "SIA \"Horsify\" jaunumu dati"
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


def PDF_dokuments_kontakti():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM kontakti")
    data = cursor.fetchall()

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Arial', 'backend/arialuni.ttf'))
    document = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["ID", "Lietotājvārds", "Virsraksts", "Teksts"]]

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
    header_text = "SIA \"Horsify\" kontaktu dati"
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

#Lietotāja funkcionalitāte


def get_menesis():
    now = datetime.datetime.now()
    return now.strftime("%B")

def sacensibas_menesi(events, month):
    filtered_events = []
    for event in events:
        event_month = event['datums_sakums'].strftime("%B")
        if event_month.lower() == month.lower():
            filtered_events.append(event)
    return filtered_events

def sacensibas_lietotajiem(events):
    filtered_events = sacensibas_menesi(events, get_menesis())

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Arial', 'backend/arialuni.ttf'))
    document = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["Nosaukums", "Atrašanās Vieta", "Sākuma Datums", "Beigu Datums", "Norises Vieta"]]

    for row in filtered_events:
        row_values = [
            Paragraph(unidecode(row['nosaukums']), getSampleStyleSheet()['Normal']),
            Paragraph(unidecode(row['atrasanas_vieta']), getSampleStyleSheet()['Normal']),
            row['datums_sakums'],
            row['datums_beigas'],
            Paragraph(unidecode(row['jasanas_norises_vieta']), getSampleStyleSheet()['Normal'])
        ]
        table_data.append(row_values)

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
    locale.setlocale(locale.LC_TIME, 'lv_LV')
    current_month = datetime.datetime.now().strftime("%B")
    header_text = f"SIA \"Horsify\" Sacensibu dati, kuri notiek šaja menesi - {current_month.capitalize()}"
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
    return buffer


def PDF_dokuments_personalizets_grafiks():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nosaukums, datums_sakums, datums_beigas, iestade, ieraksts FROM lietotaju_darbibas WHERE lietotajsFK = %s", (session['lietotajvards'],))
    data = cursor.fetchall()

    buffer = BytesIO()
    pdfmetrics.registerFont(TTFont('Arial', 'backend/arialuni.ttf'))
    document = SimpleDocTemplate(buffer, pagesize=letter)
    table_data = [["Nosaukums", "Sākuma datums", "Beigu datums", "iestāde", "ieraksts"]]

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
    header_text = "SIA \"Horsify\" personalizeta grafika dati"
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
