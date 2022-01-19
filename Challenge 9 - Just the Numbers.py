def jnum (list = []):
    justnum = []
    for i in list:
        if type(i) == int:
          justnum.append(i)
    return justnum

print(jnum(['pop', 2, 3, 'pap', 0, 8, 'pip', 'pep', 0, 7]))
