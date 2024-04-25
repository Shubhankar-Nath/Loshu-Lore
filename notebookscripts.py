import datetime
import fpdf

class PDF_Utils:

    WIDTH = 210
    HEIGHT = 297
    def generate_front_page(username, dob):
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 26)
        pdf.ln(85)
        pdf.write(5, "Your Numerology Guide")
        pdf.set_font("Arial", size = 12)
        pdf.ln(15)
        pdf.write(5, "Report For: " + username)
        pdf.ln(10)
        pdf.write(5, "Date of Birth: " + dob)
        pdf.ln(10)
        pdf.write(5, "Report generated on: " + str(datetime.datetime.now()))
        return pdf

    def add_page(pdf):
        pdf.add_page()
        #code to add a footer to the page
        pdf.image("./assets/logo text.png", 0, 280, PDF_Utils.WIDTH/4)


    def save_pdf(filename, pdf):
        pdf.output(filename+'_report.pdf')

