import pymupdf as pdf

# Crops unnecessary areas from the page

doc = pdf.open("orig_text.pdf")
page = doc[0]

width = page.rect.width
height = page.rect.height

page.set_cropbox(pdf.Rect(0,0,width-50,height-25))
doc.save("cropped.pdf")