# context manager do usp pracy z plikami
# with - dedykowany do plikow

with open("test.log", "w", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("kolejna\n")
    fh.write("jeszcze jedna\n")

with open("test.log", "w", encoding="utf-8") as f:
    f.write("Nadpisane\n")

with open("test.log", "a", encoding="utf-8") as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dośdane\n")

with open("test.log", "r", encoding="utf-8") as f:
    lines = f.read()

print(lines)