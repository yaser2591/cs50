yas = input('camel Case: ')
akhar = ''
aval = yas[0]
if aval.isupper():
    aval = aval.lower()
    yas = yas[1:]
    yas = aval + yas

for nam in yas:
    if nam.isupper():
        akhar = akhar + '_' + nam.lower()
    else:
        akhar = akhar + nam

print(akhar)
