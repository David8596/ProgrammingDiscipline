from itertools import product

k = 0
for i in product("АИНОПТУЯ", repeat=6):
    glas = [l for l in i if l in 'АИУОЯ']
    soglas = [l for l in i if l in 'НТП']
    
    if glas == sorted(glas) and soglas == sorted(soglas, reverse=True):
        k += 1

print(k * 7)