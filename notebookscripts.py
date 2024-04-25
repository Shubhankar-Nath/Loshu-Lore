import datetime
import fpdf

class PDF_Utils:

    WIDTH = 210
    HEIGHT = 297
    def generate_front_page(username, dob):
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 36)
        pdf.ln(120)
        pdf.write(5, "Your Numerology Guide")
        pdf.set_font("Arial", size = 12)
        pdf.ln(15)
        pdf.write(5, "Report For: " + username)
        pdf.ln(6)
        pdf.write(5, "Date of Birth: " + dob)
        pdf.ln(6)
        pdf.write(5, "Report generated on: " + str(datetime.datetime.now()))        
        pdf.image("./assets/front letterhead.png", 0, 0, PDF_Utils.WIDTH)
        return pdf

    def add_page(pdf):
        pdf.add_page()
        #code to add a footer to the page
        pdf.image("./assets/logo text.png", 0, 280, PDF_Utils.WIDTH/4)

    def save_pdf(filename, pdf):
        print(filename)
        pdf.output( "Report_"+filename + ".pdf")
    
    def add_disclaimer(text, pdf):
        pdf.set_fill_color(0, 0, 0)
        pdf.rect(10, 230, PDF_Utils.WIDTH - 10, 1, 'DF')
        pdf.set_font("Arial", size = 12)
        pdf.ln(75)
        pdf.write(5, "Disclaimer:")
        pdf.set_font("Courier", size = 8)
        pdf.ln(6)
        pdf.write(5, text)

class FILE_Utils:

    def get_disclaimer():
        with open('data/Disclaimer.txt', 'r') as file:
            return file.read()