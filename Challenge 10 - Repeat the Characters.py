def repeat (string):
    rep = ''
    for i in string:
        rep = rep + i + i
    return rep
print(repeat("bounce"))
