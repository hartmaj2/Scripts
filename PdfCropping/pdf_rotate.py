import pymupdf as pdf

# Rotates the pdf to the rotation in which we can read it

doc = pdf.open("split.pdf")


for page in doc:
    page.set_rotation(90)

doc.save("rotated.pdf")