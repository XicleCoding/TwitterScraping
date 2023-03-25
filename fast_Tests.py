'''
aux = '70.4K'
aux2 = aux.split('.')
aux3 = aux2[1].split('K')
final = aux2[0] + ',' + aux3[0] + '00'
print(final)
'''

def countFormat(count):
    if '.' in count:
        split1 = count.split('.')
        split2 = split1[1].split('K')
        finalCount = split1[0] + ',' + split2[0] + '00'
    elif ',' in count or count == '':
        return count
    elif 'K' not in count:
        return count
    else:
        split1 = count.split('K')
        finalCount = split1[0] + ',000'
    return finalCount



print(countFormat('70.4K'))
print(countFormat('61K'))
print(countFormat(''))
print(countFormat('3,861'))
print(countFormat('602'))


