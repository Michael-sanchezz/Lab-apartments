"""
Task: Create and call several functions, using a combination of default parameters,
 named arguments, and lambda functions.

Write a function named apt_search1. It takes a city parameter (string)
, a max_rent parameter (int), a min_beds parameter (int),
and a pets_allowed parameter (boolean). It simply returns a string similar to one of these examples:
"""

def apt_search1(city, max_rent, min_beds, pets_allowed=False):
    if pets_allowed:
        print(f"welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments"
              f" that allows pets within a budget of {max_rent} ")
    else:
        print(f"welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments "
              f"within a budget of {max_rent}")
apt_search1("NY","$3000", 1,True)


def apt_search2(city, max_rent, min_beds =3, pets_allowed=True):
    if pets_allowed:
        print(f"welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments"
              f" that allows pets within a budget of {max_rent} ")
    else:
        print(f"welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments "
              f"within a budget of {max_rent}")
apt_search2("Florida","$2000")
apt_search2("Florida","$2000", 2,False)
apt_search2(city="Florida",max_rent="$2000",min_beds=0,pets_allowed=True)

"""
Finally, let’s finish up with some simple lambda functions held in variables. You will get warnings here—for this assignment, you should ignore those.
plus_one_hundred
Write a lambda function that adds 100 to any given number
square_num
Write a lambda function that squares any given number
concatenate
Write a lambda function that concatenates “- “ before any string
divide_by_three
Write a lambda function that divides any number by 3
"""

lamb_100 = lambda x: x+100
print(lamb_100(10))

lamb_squared = lambda x:x*x
print(lamb_squared(3))

lamb_concat = lambda x: "- " + x
print(lamb_concat("hello"))

lamb_div3 = lambda x:x/3
print(lamb_div3(12))