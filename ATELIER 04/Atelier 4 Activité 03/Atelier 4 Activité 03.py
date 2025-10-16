import csv
with open('C:\data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:

        print(line)
