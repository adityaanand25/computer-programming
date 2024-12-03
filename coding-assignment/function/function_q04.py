#Amit is trying to write a program to read data from a CSV file and display records based on a user-provided admission number. Help him complete the code.

def search_record(admission_number):
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == admission_number:  
                return row
    return "Record not found."
