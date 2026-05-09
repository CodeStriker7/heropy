print("-" * 40)
print("Today, we learn list and set difference")

bierce = {
 "day": "A period of twenty-four hours, mostly misspent",
 "positive": "Mistaken at the top of one's voice",
 "misfortune": "The kind of fortune that never misses",
}

b = []
d = ()
print(bierce)
print(type(b))
print(type(d))

# <class 'dict'>   == a
# <class 'list'>   == b
# <class 'tuple'>  == d

# but set not , why?
empty_set = set()
print(empty_set)

dino = set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] )
bigo = set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') )
dudo = set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} )
print(f"the best {dino} \nit is the {bigo} \nand the end {dudo}")