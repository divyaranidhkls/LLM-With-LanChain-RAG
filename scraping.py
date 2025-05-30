import requests
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from textwrap import wrap

url = "https://en.wikipedia.org/wiki/Tally_Solutions"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

text = ""
for p in soup.find_all("p"):
    text += p.get_text() + "\n\n"


def save_to_pdf(text, filename):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER
    c.setFont("Helvetica", 12)

    margin = 50
    max_width = width - 2 * margin
    y = height - margin

    
    lines = []
    for paragraph in text.split('\n'):
        wrapped = wrap(paragraph, width=90) 
        if not wrapped:
            lines.append('')
        else:
            lines.extend(wrapped)

    for line in lines:
        if y < margin:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - margin
        c.drawString(margin, y, line)
        y -= 15

    c.save()


save_to_pdf(text, "output.pdf")
