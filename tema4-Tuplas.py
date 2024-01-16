'''
    Las tuplas son inmutables
    ()
'''
tupla=("uno", "dos", "tres")
print(tupla)
print(type(tupla))

tuplasVariosDatos = (12,True,23.6,"Nombre",12+3j)
print(tuplasVariosDatos)

tuplasconTuplas=(1,2,3,4,(1,2,3))
print(tuplasconTuplas)

print(tuplasconTuplas[3])
print(tuplasconTuplas[-2])
print(tuplasconTuplas[0:2])

a,b,c = tupla
print(a)
print(b)
print(c)

