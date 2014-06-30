import random

items = ['Columbia','Cote d lvoire',
         'Brazil','Mexico',
         'Neitherland','Chile',
         'Uruguay','Costa rica',
         'Switzerland','France','Ecuador','Honduras',
         'Argentina','Nigeria',
         'Germany','USA',
         'Belgium','Algeria']

# random.shuffle(items)



item1 = ['Belgium','Korea']
item2 = ['under','over']
item3 = ['Russia','Algeria']         
item4 = ['under','over']

random.shuffle(item1)
random.shuffle(item2)
random.shuffle(item3)
random.shuffle(item4)

print "Belgium vs Korea : bat %s" %item1[0]
print "under over Bel vs Korea bat %s" %item2[0]
print "Russia vs Algeria: bat %s" %item3[0]
print "Russia vs Algeria: bat %s" %item4[0]