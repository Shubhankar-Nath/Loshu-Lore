import datetime
import pymupdf 

class PDF_Utils:

    WIDTH = 600
    HEIGHT = 400

    def add_cover(name, dob):
        doc = pymupdf.Document()
        coverpage = doc.new_page(-1, PDF_Utils.WIDTH, PDF_Utils.HEIGHT)
        covertext_html = "<h1 style>Numerology Guide</h1><p>Report for: " + name + " <br>Date of Birth:" + dob + " <br><sub>Report Timestamp:" + str(datetime.datetime.now()) + "</sub> </p>"
        covertext_rect = pymupdf.Rect(50, 50, 450, 250)
        coverpage.insert_html(covertext_rect, covertext_html )
        return doc

    def add_page(doc):
        page = doc.new_page(-1, PDF_Utils.WIDTH, PDF_Utils.HEIGHT)

    def save_pdf(filename, doc):
        print(filename)
        doc.save( "Report_"+filename + ".pdf")
    