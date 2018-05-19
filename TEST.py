import ephem

mars = ephem.Mars('2018/09/23')
print(mars)

print(ephem.constellation(mars))
str_analyse = 'maaama fsdk aaaaa'
while 'aa' in str_analyse:
    str_analyse = str_analyse.replace('aa', 'a')
    print(str_analyse)