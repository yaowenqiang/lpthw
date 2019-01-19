from reportlab.pdfgen import canvas

def hello():
    c = canvas.Canvas("helloworld.pdf")

    c.drawString(100, 100, 'hello world, you are beautiful')

    c.showPage()
    c.save()

hello()
