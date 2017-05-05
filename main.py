import sys
from country import Country
from country import City

x = 0

a1 = City('Los Angeles', '4 million')
b1 = ['New York', 'Virginia', 'California', 'Florida', 'Hawaii']
c1 = Country('USA','350 million', b1, a1)

a2 = City('Cancun', '700,000')
b2 = ['Durango', 'Puebla', 'Guerrero', 'Quintana Roo']
c2 = Country('Mexico', '127 million', b2, a2)

countries = [c1, c2]

sys.stdout = open('log.txt', 'w')

print
while x < len(countries):
    print 'Name: ' + countries[x].name
    print 'Population: ' + countries[x].population
    print 'Best States: ' + ', '.join(countries[x].states)
    print 'Top State Count: ' + str(countries[x].fav_cnt())
    print 'Best City: ' + countries[x].best_city.name
    print countries[x].best_city.name + ' Population: ' + countries[x].best_city.population
    print
    x += 1

sys.stdout.close()
