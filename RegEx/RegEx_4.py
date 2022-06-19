import re

def cenzura(tekstas, *keiksmai):
    str = tekstas
    for keiksmas in keiksmai:
        cenzuruotas_pattern = re.compile(r'\B[a-z]\B')
        cenzuruotas = cenzuruotas_pattern.sub('*', keiksmas)
        str = re.sub(keiksmas, cenzuruotas, str)
    print(str)

cenzura('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')