import chardet

with open("test.log", "rb") as f:
    lines = f.read()
    print(lines)

result = chardet.detect(lines)
print(result)

encoding = result["encoding"]
print(encoding)
print(lines.decode(encoding))