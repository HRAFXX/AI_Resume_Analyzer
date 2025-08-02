from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(filename, user_name, matches):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, f"Resume Analysis Report for {user_name}")
    c.setFont("Helvetica", 12)
    y = 700
    for job in matches:
        c.drawString(100, y, f"Job Title: {job['title']}")
        c.drawString(100, y-20, f"Match Score: {job['score']}%")
        y -= 50
    c.save()
