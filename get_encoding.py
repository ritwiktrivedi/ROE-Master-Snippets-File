import chardet

file = "path/to/file"
with open(file, 'rb') as f:
    result = chardet.detect(f.read())

print(result)