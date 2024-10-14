import json

class FILE_Utils:

    def __init__(self):
    # If you want to do any initial processing, add it here.
        pass

    # Read the disclaimer file and return the content (600-700 character)
    def get_disclaimer(self):
        with open('data/Disclaimer.txt', 'r') as file:
            return file.read()
        
    # Read input file and return the Json content
    def read_input_file(self):
        with open('input.json', 'r') as file:
            return json.load(file)
        
    # Validate the input json file
    def validate_input_file(self, input_json):
        if input_json is None:
            print("Input file is empty")
            return False
        if input_json['First Name'] == "" or input_json['Last Name'] == "":
            print("First Name and Last Name cannot be empty")
            return False
        if (self.validate_date(input_json['D1'], input_json['D2']) is False):
            print("Invalid Date")
            return False
        if (self.validate_month(input_json['M1'], input_json['M2']) is False):
            print("Invalid Month")
            return False
        if (self.validate_year(input_json['Y1'], input_json['Y2'], input_json['Y3'], input_json['Y4']) is False):
            print("Invalid Year")
            return False
        return True
    
    # Function to validate DOB input
    def validate_date(self, D1, D2):
        date = int(D1*10 + D2)
        if date < 1 or date > 31:
            return False
        return True
    
    def validate_month(self, M1, M2):
        month = int(M1*10 + M2)
        if month < 1 or month > 12:
            return False
        return True
    
    def validate_year(self, Y1, Y2, Y3, Y4):
        year = int(Y1*1000 + Y2*100 + Y3*10 + Y4)
        if year < 1900 or year > 2050:
            return False
        return True
    
    def get_fulldate(self, input_json):
        return "{}{}-{}{}-{}{}{}{}".format(input_json['D1'], input_json['D2'], input_json['M1'], input_json['M2'], input_json['Y1'], input_json['Y2'], input_json['Y3'], input_json['Y4'])
    
    def get_fullname(self, input_json):
        return "{} {}".format(input_json['First Name'], input_json['Last Name'])