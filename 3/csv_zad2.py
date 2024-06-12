import csv

fields = []
rows = []

filename = "nasze_dane2.csv"

with open(filename, "r") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter,dialect.quotechar)
    f.seek(0) # odczyt na poczatek pliku
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    print(csvreader)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(fields)
print(rows)