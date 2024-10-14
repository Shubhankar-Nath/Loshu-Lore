# Import Statements (Do not Edit the block of code below)

import ipywidgets as widgets
import IPython.display as display
from utils.pdf_helper import PDF_Utils
from utils.file_helper import FILE_Utils

LO_SHU_GRID = [[4,9,2],[3,5,7],[8,1,6]]



# Main Code (Do not Edit the block of code below)
if __name__ == "__main__":
    file_util_agent = FILE_Utils()
    input_json = file_util_agent.read_input_file()
    if file_util_agent.validate_input_file(input_json) is False:
        exit()
    doc = PDF_Utils.add_cover(file_util_agent.get_fullname(input_json), file_util_agent.get_fulldate(input_json))
    PDF_Utils.save_pdf(file_util_agent.get_fullname(input_json), doc)