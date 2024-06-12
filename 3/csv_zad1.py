import csv

#pliki csv
#pliki ktorych dane oddzielone sa , tab / ;
#Radek, Zenek, Marek

filename = "records.csv"
row = ["radek", "cos", 3, "9.1"]
fields = ["name", "branch", "year", "cgpq"]

dictionary = dict(zip(fields,row))
print(dictionary)

dict_list = [
    {'name': 'radek', 'branch': 'cos', 'year': 3, 'cgpq': '9.1'},
    {'name': 'tomek', 'branch': 'cos', 'year': 1, 'cgpq': '9'},
    {'name': 'zenek', 'branch': 'cos', 'year': 2, 'cgpq': '9.7'},
    {'name': 'marek', 'branch': 'cos', 'year': 2, 'cgpq': '9.1'},
]

with open(filename, "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(row)
    csvwriter.writerow(fields)

filename = "nasze_dane2.csv"

with open(filename, "w", newline="") as fh:
    csvwriter = csv.DictWriter(fh,fieldnames=fields)
    csvwriter.writeheader()
    # csvwriter.writerow(dictionary)
    csvwriter.writerows(dict_list)