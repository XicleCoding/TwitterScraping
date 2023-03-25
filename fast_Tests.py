aux = '70.4K'

aux2 = aux.split('.')
aux3 = aux2[1].split('K')
final = aux2[0] + ',' + aux3[0] + '00'
print(final)