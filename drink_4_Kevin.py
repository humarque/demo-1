# Hey Kevin!!!! Let's do a caipirinha (Brazilian Drink for Tonight's dinner!)

Type = "Caninha of Belo Horizonte"
Ingredient = 'sugar'
Drink = 'caipirinha'

def cachaca_and_lemons(cachaca_count, boxes_of_lemons):
	print "You have %d cachaca!" %  cachaca_count
	print "You have %d boxes of lemons!" % boxes_of_lemons
	print "Man, that's enogh for a Alejandro party!!!"
	print "Get a drunk tonight with our friends after Python training.\n"	
	
print "We can just give the functions numbers direclty as well: "
cachaca_and_lemons(20, 30)

print "OR, we can use variables from our scripts: "
amount_of_cachaca = 10
amount_of_lemons = 50

cachaca_and_lemons(amount_of_cachaca, amount_of_lemons)

print "We can even do macth inside of the expression below:"
cachaca_and_lemons(12 + 23, 4 + 1)

print "we can combine variables and macth, like %s, %s and %r:" % (Type, Ingredient, Drink)
cachaca_and_lemons(amount_of_cachaca + 100, amount_of_lemons + 1000)

