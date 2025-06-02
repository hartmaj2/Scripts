import pymupdf as pdf

# Crops unnecessary areas from the page

doc = pdf.open("PdfCropping/Grundeinkommen.pdf")
page = doc[0]

# page.set_rotation(0) uncomment if getting MediaBox errors

def crop_vertical(page : pdf.Page):
    width = page.rect.width
    height = page.rect.height

    page.set_cropbox(pdf.Rect(0,0,width-50,height-25))

def crop_horizontal(page : pdf.Page):
    width = page.rect.width
    height = page.rect.height

    page.set_cropbox(pdf.Rect(50,0,width,height-50))

crop_vertical(page)

doc.save("cropped.pdf")