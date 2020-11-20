from app import app
from flask import request
import csv, os

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/outputcsv', methods=['POST'])
def output_to_csv():
    d_json = request.json

    # gets headers
    headers = []
    for key in d_json[0]:
        headers.append(key)

    # checks if output file exists
    def checkfile(file):
        return os.path.isfile(file)
    
    # defines filename
    filename = 'output.csv'

    # checks if filename exists
    if checkfile(filename):
        print('file exists')
    else:
        # creates file and inputs headers
        with open(filename, mode='w') as outputfile:
            output_writer = csv.writer(outputfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            reader = csv.reader(outputfile)
            output_writer.writerow(headers)

    # open csv in append mode and insert data
    with open(filename, mode='a') as outputfile:
        output_writer = csv.writer(outputfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        reader = csv.reader(outputfile)

        # loops through each row of request data
        for i in d_json:
            new_row = []
            for key in i:
                new_row.append(i[key])

            # writes a new row
            output_writer.writerow(new_row)


    return "you've reach the csv endpoint"
