import re

def check_data_validation(full_name,father_name,mother_name):
    if not full_name.replace(" ", "").isalpha() or mother_name.replace(" ", "").isalpha() or father_name.replace(" ", "").isalpha():
        message, status = "Full name should contain only characters.", False
    else:
        message, status = "Student added successfully.", True
    
    return message, status
