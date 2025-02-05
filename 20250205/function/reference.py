def foo(param):
    print(id(param))
    param.append(1)

let = []
print(id(let))
foo(param=let)

print(let) # le changement se produit ici car la fonction modifie la liste passée en argument