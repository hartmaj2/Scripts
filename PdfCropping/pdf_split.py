import pymupdf as pdf

# Splits the pdf page into two separate parts through the midpoint to upper and lower half

doc = pdf.open("cropped.pdf")
split_doc = pdf.open()
page = doc[0]

width = page.rect.width
height = page.rect.height
mid = height / 2

up = pdf.Rect(0,0,width,mid)
bot = pdf.Rect(0,mid,width,height)

split_doc.new_page(width=width, height = mid).show_pdf_page(up,doc,page.number,clip=bot)
split_doc.new_page(width=width, height = mid).show_pdf_page(up,doc,page.number,clip=up)

split_doc.save("split.pdf")