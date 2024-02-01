from docxtpl import *
doc = DocxTemplate("test.docx")

values = {
    'name': "Miguel"
}
doc.render(values)
doc.save("generated.docx")