import ephem

mars = ephem.Mars('2018/09/23')
print(mars)

print(ephem.constellation(mars))