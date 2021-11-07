def sortlist (list,sort):
  if sort == "asc":
    list.sort()
  elif sort == "dsc":
    list.sort(reverse = True)
  elif sort == "none":
    list = list
  return list

alist = ["Eren","Mikasa","Jean","Armin","Sasha","Conny","Levi","Erwin","Hange"]
sort = "dsc"
print(sortlist(alist,sort))