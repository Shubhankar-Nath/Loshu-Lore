import datetime
import pymupdf 

class PDF_Utils:

    WIDTH = 600
    HEIGHT = 400

    def __init__(self):
    # If you want to do any initial processing, add it here.
        pass

    def add_cover(self, name, dob):
        doc = pymupdf.Document()
        coverpage = doc.new_page(-1, PDF_Utils.WIDTH, PDF_Utils.HEIGHT)
        covertext_html = "<h1 style>Numerology Guide</h1><p>Report for: " + name + " <br>Date of Birth:" + dob + " <br><sub>Report Timestamp:" + str(datetime.datetime.now()) + "</sub> </p>"
        covertext_rect = pymupdf.Rect(50, 50, 450, 250)
        coverpage.insert_htmlbox(covertext_rect, covertext_html )
        return doc

    def add_page(self, doc):
        page = doc.new_page(-1, PDF_Utils.WIDTH, PDF_Utils.HEIGHT)

    def save_pdf(self, filename, doc):
        filename = "Report for {}.pdf".format(filename)
        print('SUCCESS: Report with file name \'' + filename + '\' saved')
        doc.save( filename)